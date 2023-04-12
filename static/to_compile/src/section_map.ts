import "ol/ol.css"

import { Map as OLMap, View } from "ol"
import {
    FullScreen,
    MousePosition,
    ScaleLine,
    defaults as defaultControls,
} from "ol/control"
import { Coordinate, toStringHDMS } from "ol/coordinate"
import { click, noModifierKeys, pointerMove } from "ol/events/condition.js"
import { getArea, isEmpty } from "ol/extent"
import GeoJSON from "ol/format/GeoJSON.js"
import Select from "ol/interaction/Select.js"
import TileLayer from "ol/layer/Tile"
import VectorLayer from "ol/layer/Vector"
import { useGeographic } from "ol/proj.js"
import { TileWMS, Vector as VectorSource } from "ol/source.js"
import { Circle, Fill, Stroke, Style } from "ol/style.js"

useGeographic()

function buildStyle({ strokeColor, fillColor, width }) {
    const stroke = new Stroke({ color: strokeColor, width })
    const fill = new Fill({ color: fillColor })
    return new Style({
        fill,
        stroke,
        image: new Circle({ radius: 5, stroke, fill }),
    })
}

export class SectionMap {
    #map: OLMap
    #geojsonLayer: VectorLayer<VectorSource>
    #selectInteraction: Select
    #hoverSectionInteraction: Select
    #source: TileWMS

    #maxZoom: number
    #padding = [20, 20, 20, 20]
    #duration = 300

    #initialStrokeColor = "#ff000099"
    #initialFillColor = "transparent"
    #initialWidth = 1.5

    #hoveredStrokeColor = "red"
    #hoveredFillColor = "transparent"
    #hoveredWidth = 3

    #selectedStrokeColor = "#000091"
    #selectedFillColor = "#00009108"
    #selectedWidth = 2

    constructor({
        target,
        initialCenter,
        maxZoom,
        geojson,
        wmsUrl,
        fullscreenElement,
    }: {
        target: HTMLElement
        initialCenter: Coordinate
        maxZoom: number
        geojson: string
        wmsUrl: string
        fullscreenElement: HTMLElement
    }) {
        this.#maxZoom = maxZoom
        this.#map = this.#initMap(
            maxZoom,
            initialCenter,
            target,
            geojson,
            wmsUrl,
            fullscreenElement,
        )
        this.#initHoverMapInteraction()
        this.#hoverSectionInteraction = this.#initHoverSectionInteraction()
        this.#selectInteraction = this.#initSelectInteraction()
        this.#map.on("click", this.#dispatchWMSFeature)
    }

    #initMap(
        maxZoom: number,
        initialCenter: Coordinate,
        target: HTMLElement,
        geojson: string,
        wmsUrl: string,
        fullscreenElement: HTMLElement,
    ) {
        this.#geojsonLayer = new VectorLayer({
            source: new VectorSource({
                features: new GeoJSON().readFeatures(geojson),
            }),
            style: buildStyle({
                strokeColor: this.#initialStrokeColor,
                fillColor: this.#initialFillColor,
                width: this.#initialWidth,
            }),
            renderOrder: (a, b) => {
                return (
                    getArea(b.getGeometry()!.getExtent()) -
                    getArea(a.getGeometry()!.getExtent())
                )
            },
        })

        const view = new View({
            center: initialCenter,
            zoom: maxZoom,
        })

        const layerPerZoom = [
            // We keep RASTER_MARINE_50_WMSR_3857 because RASTER_MARINE_3857_WMSR is missing tiles at high zoom levels
            { layer: "RASTER_MARINE_50_WMSR_3857", minZoom: 13 },
            { layer: "RASTER_MARINE_3857_WMSR" },
        ]
        const rasterMarineLayers = layerPerZoom.map(({ layer, minZoom }) => {
            return new TileLayer({
                source: new TileWMS({
                    url: "https://services.data.shom.fr/u2kejlcaaf2ar8v69kvvqef6/wms/r",
                    params: { LAYERS: layer },
                    serverType: "geoserver",
                }),
                preload: Infinity,
                minZoom,
            })
        })

        const LAYERS = "BALISAGE_BDD_WMSV"
        this.#source = new TileWMS({
            url: wmsUrl,
            params: { TILED: true, LAYERS },
            serverType: "geoserver",
        })
        const WMSLayer = new TileLayer({
            source: this.#source,
            minZoom: 11,
        })

        return new OLMap({
            controls: defaultControls().extend([
                new ScaleLine({ bar: true, units: "nautical", steps: 4, text: true }),
                new FullScreen({ source: fullscreenElement }),
                new MousePosition({
                    coordinateFormat: toStringHDMS,
                    className:
                        "sn-absolute sn-bottom-1w sn-right-1w sn-bg-white sn-bg-opacity-70 sn-tabular-nums",
                }),
            ]),
            keyboardEventTarget: document,
            target,
            view,
            layers: [...rasterMarineLayers, this.#geojsonLayer, WMSLayer],
        })
    }

    #initSelectInteraction() {
        const selectInteraction = new Select({
            condition: (mapBrowserEvent) =>
                click(mapBrowserEvent) && noModifierKeys(mapBrowserEvent),
            style: buildStyle({
                strokeColor: this.#selectedStrokeColor,
                fillColor: this.#selectedFillColor,
                width: this.#selectedWidth,
            }),
        })
        selectInteraction.on("select", this.#dispatchBpnID)
        this.#map.addInteraction(selectInteraction)

        return selectInteraction
    }

    #initHoverMapInteraction() {
        const hoverInteraction = new Select({
            condition: (mapBrowserEvent) =>
                pointerMove(mapBrowserEvent) && noModifierKeys(mapBrowserEvent),
            style: buildStyle({
                strokeColor: this.#hoveredStrokeColor,
                fillColor: this.#hoveredFillColor,
                width: this.#hoveredWidth,
            }),
        })

        this.#map.addInteraction(hoverInteraction)
    }

    #initHoverSectionInteraction() {
        const hoverSectionInteraction = new Select({
            condition: (mapBrowserEvent) =>
                pointerMove(mapBrowserEvent) && noModifierKeys(mapBrowserEvent),
            style: buildStyle({
                strokeColor: this.#selectedStrokeColor,
                fillColor: this.#selectedFillColor,
                width: this.#selectedWidth,
            }),
        })

        this.#map.addInteraction(hoverSectionInteraction)
        return hoverSectionInteraction
    }

    selectSection(bpnID) {
        const feature = this.#selectFeature(bpnID, { in: this.#selectInteraction })
        if (feature) {
            this.#fitMapToExtent(feature.getGeometry()!.getExtent())
        }
    }

    highlightSection(bpnID) {
        this.#selectFeature(bpnID, { in: this.#hoverSectionInteraction })
    }

    unhighlightSection() {
        this.#hoverSectionInteraction.getFeatures().clear()
    }

    #selectFeature(bpnID, { in: selectInteraction }: { in: Select }) {
        const sectionFeature = this.#geojsonLayer.getSource()!.getFeatureById(bpnID)
        if (!sectionFeature) {
            console.debug(`No geometry associated to hash: "${bpnID}"`)
            return
        }
        const selectedFeatures = selectInteraction.getFeatures()
        selectedFeatures.clear()
        selectedFeatures.push(sectionFeature)
        return sectionFeature
    }

    fitViewToAllSections() {
        this.#fitMapToExtent(this.#geojsonLayer.getSource()!.getExtent())
    }

    #fitMapToExtent(extent) {
        if (isEmpty(extent)) {
            console.debug("Cannot fit empty extent provided as 'geometry'")
            return
        }
        const view = this.#map.getView()
        view.cancelAnimations()
        view.fit(extent, {
            maxZoom: this.#maxZoom,
            padding: this.#padding,
            duration: this.#duration,
        })
    }

    #dispatch(type, details) {
        this.#map.getTargetElement().dispatchEvent(
            new CustomEvent(type, {
                detail: details,
                bubbles: true,
            }),
        )
    }

    #dispatchBpnID = (olEvent) => {
        const selectedFeature = olEvent.target.getFeatures().item(0)
        let bpnID = ""
        if (selectedFeature) {
            bpnID = selectedFeature.getId()
        }
        this.#dispatch("ol:select", { bpnID })
    }

    #dispatchWMSFeature = async (mapBrowserEvent) => {
        if (!mapBrowserEvent.originalEvent.shiftKey) {
            console.log("Pas de shift == pas de popin")
            return
        }

        const resolutionIn4326Unit = 0.0002
        const htmlUrl = this.#source.getFeatureInfoUrl(
            mapBrowserEvent.coordinate,
            resolutionIn4326Unit,
            "EPSG:4326",
            {
                INFO_FORMAT: "text/html",
            },
        )!

        const response = await fetch(htmlUrl)
        const html = await response.text()
        const fetchedEmptyFeature = !html.includes("FR00")
        if (fetchedEmptyFeature) {
            return
        }

        this.#dispatch("wms:featureInfoFetched", { html })
    }
}

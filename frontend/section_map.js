import "ol/ol.css"

import { Map as OLMap, View } from "ol"
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
    #map
    #geojsonLayer
    #selectInteraction

    #maxZoom
    #padding = [20, 20, 20, 20]
    #duration = 300

    #initialStrokeColor = "red"
    #initialFillColor = "transparent"
    #initialWidth = 1.5

    #hoveredStrokeColor = "red"
    #hoveredFillColor = "transparent"
    #hoveredWidth = 3

    #selectedStrokeColor = "red"
    #selectedFillColor = "#00009108"
    #selectedWidth = 2

    constructor({ target, initialCenter, maxZoom, geojson }) {
        this.#maxZoom = maxZoom
        this.#map = this.#initMap(maxZoom, initialCenter, target, geojson)
        this.#initHoverInteraction()
        this.#selectInteraction = this.#initSelectInteraction()
    }

    #initMap(maxZoom, initialCenter, target, geojson) {
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
                    getArea(b.getGeometry().getExtent()) -
                    getArea(a.getGeometry().getExtent())
                )
            },
        })

        const view = new View({
            center: initialCenter,
            zoom: maxZoom,
        })

        const layerPerZoom = [
            { layer: "RASTER_MARINE_1M_3857_WMSR", maxZoom: 7 },
            { layer: "RASTER_MARINE_400_WMSR_3857", minZoom: 7, maxZoom: 10 },
            { layer: "RASTER_MARINE_150_WMSR_3857", minZoom: 10, maxZoom: 11 },
            { layer: "RASTER_MARINE_50_WMSR_3857", minZoom: 11 },
            { layer: "RASTER_MARINE_20_WMSR_3857", minZoom: 13 },
        ]
        const rasterMarineLayers = layerPerZoom.map(({ layer, minZoom, maxZoom }) => {
            return new TileLayer({
                source: new TileWMS({
                    // FIXME : ne pas hardcoder cette url dans le JS mais la définir côté router
                    url: "/carting/proxy",
                    params: { LAYERS: layer },
                    serverType: "geoserver",
                }),
                preload: Infinity,
                maxZoom,
                minZoom,
            })
        })

        return new OLMap({
            target,
            view,
            layers: [...rasterMarineLayers, this.#geojsonLayer],
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

    #initHoverInteraction() {
        const hoverInteraction = new Select({
            condition: pointerMove,
            style: buildStyle({
                strokeColor: this.#hoveredStrokeColor,
                fillColor: this.#hoveredFillColor,
                width: this.#hoveredWidth,
            }),
        })

        this.#map.addInteraction(hoverInteraction)
    }

    selectSection(bpnID) {
        const sectionFeature = this.#geojsonLayer.getSource().getFeatureById(bpnID)
        if (!sectionFeature) {
            console.debug(`No geometry associated to window hash: "${bpnID}"`)
            return
        }
        const selectedFeatures = this.#selectInteraction.getFeatures()
        selectedFeatures.clear()
        selectedFeatures.push(sectionFeature)
        this.#fitMapToExtent(sectionFeature.getGeometry().getExtent())
    }

    fitViewToAllSections() {
        this.#fitMapToExtent(this.#geojsonLayer.getSource().getExtent())
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

    #dispatchBpnID = (olEvent) => {
        const selectedFeature = olEvent.target.getFeatures().item(0)
        let bpnID = ""
        if (selectedFeature) {
            bpnID = selectedFeature.getId()
        }
        this.#map.getTargetElement().dispatchEvent(
            new CustomEvent("ol:select", {
                detail: { bpnID },
                bubbles: true,
            }),
        )
    }
}

import "ol/ol.css"

import { Map as OLMap, View } from "ol"
import { click, noModifierKeys, pointerMove } from "ol/events/condition.js"
import * as extent from "ol/extent"
import GeoJSON from "ol/format/GeoJSON.js"
import Select from "ol/interaction/Select.js"
import LayerGroup from "ol/layer/Group"
import TileLayer from "ol/layer/Tile"
import VectorLayer from "ol/layer/Vector"
import { useGeographic } from "ol/proj.js"
import { TileWMS, Vector as VectorSource } from "ol/source.js"
import { Circle, Fill, Stroke, Style } from "ol/style.js"

useGeographic()

export class SectionMap {
    #map
    #sectionsLayerGroup
    #selectInteraction

    #maxZoom
    #padding = [20, 20, 20, 20]
    #duration = 300
    #selectedStrokeColor = "#000091"
    #selectedFillColor = "#00009108"

    constructor({ target, initialCenter, maxZoom }) {
        this.#maxZoom = maxZoom

        this.#sectionsLayerGroup = new LayerGroup()

        const view = new View({
            center: initialCenter,
            zoom: maxZoom,
        })

        const layerPerZoom = [
            { layer: "RASTER_MARINE_1M_3857_WMSR", maxZoom: 7 },
            { layer: "RASTER_MARINE_400_WMSR_3857", minZoom: 7, maxZoom: 10 },
            { layer: "RASTER_MARINE_150_WMSR_3857", minZoom: 10, maxZoom: 11 },
            { layer: "RASTER_MARINE_50_WMSR_3857", minZoom: 11, maxZoom: 13 },
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
                maxZoom,
                minZoom,
            })
        })
        this.#map = new OLMap({
            target,
            view,
            layers: [...rasterMarineLayers, this.#sectionsLayerGroup],
        })

        this.#map.on("moveend", () =>
            // FIXME : enlever
            console.log("Zoom", this.#map.getView().getZoom()),
        )

        this.#selectInteraction = new Select({
            condition: (mapBrowserEvent) =>
                click(mapBrowserEvent) && noModifierKeys(mapBrowserEvent),
            style: this.#style({
                strokeColor: this.#selectedStrokeColor,
                fillColor: this.#selectedFillColor,
                width: 2,
            }),
        })
        this.#selectInteraction.on("select", this.#dispatchBpnID)
        this.#map.addInteraction(this.#selectInteraction)

        const hoverInteraction = new Select({
            condition: pointerMove,
            style: this.#style({
                strokeColor: "#6a6af4",
                fillColor: "transparent",
                width: 2,
            }),
        })
        this.#map.addInteraction(hoverInteraction)
    }

    addSection(bpnID, geojson) {
        const layer = new VectorLayer({
            source: new VectorSource({
                features: new GeoJSON().readFeatures(geojson),
            }),
            style: this.#style({
                strokeColor: "#6a6af4",
                fillColor: "transparent",
            }),
        })
        const layerArea = extent.getArea(layer.getSource().getExtent())

        layer.setZIndex(1 / layerArea)
        layer.set("bpnID", bpnID)
        this.#sectionsLayerGroup.getLayers().push(layer)
    }

    selectSection(bpnID) {
        const layer = this.#sectionsLayerGroup
            .getLayers()
            .getArray()
            .find((layer) => layer.get("bpnID") == bpnID)
        const selectedFeatures = this.#selectInteraction.getFeatures()
        selectedFeatures.clear()
        selectedFeatures.push(layer.getSource().getFeatures()[0])
        this.#fitMapToExtent(layer.getSource().getExtent())
    }

    fitViewToAllSections() {
        const sectionsLayerGroupExtent = extent.createEmpty()
        this.#sectionsLayerGroup.getLayers().forEach((layer) => {
            const layerExtent = layer.getSource().getExtent()
            extent.extend(sectionsLayerGroupExtent, layerExtent)
        })

        this.#fitMapToExtent(sectionsLayerGroupExtent)
    }

    #fitMapToExtent(extent) {
        const view = this.#map.getView()
        view.cancelAnimations()
        view.fit(extent, {
            maxZoom: this.#maxZoom,
            padding: this.#padding,
            duration: this.#duration,
        })
    }

    #dispatchBpnID = (e) => {
        const selectedFeature = e.target.getFeatures().item(0)
        let bpnID = ""
        if (selectedFeature) {
            const layer = e.target.getLayer(selectedFeature)
            bpnID = layer.get("bpnID")
        }
        this.#map.getTargetElement().dispatchEvent(
            new CustomEvent("ol:select", {
                detail: { bpnID },
                bubbles: true,
            }),
        )
    }

    #style({ strokeColor, fillColor, width }) {
        const stroke = new Stroke({ color: strokeColor, width })
        const fill = new Fill({ color: fillColor })
        return new Style({
            fill,
            stroke,
            image: new Circle({ radius: 5, stroke, fill }),
        })
    }
}

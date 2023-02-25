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
import { OSM, Vector as VectorSource } from "ol/source.js"
import { Circle, Fill, Stroke, Style } from "ol/style.js"

useGeographic()

export class SectionMap {
    #map
    #sectionsLayerGroup
    #selectInteraction

    #maxZoom
    #padding
    #duration

    constructor({
        target,
        initialCenter,
        maxZoom,
        padding,
        duration,
        selectedFillColor,
        selectedStrokeColor,
    }) {
        this.#maxZoom = maxZoom
        this.#padding = padding
        this.#duration = duration

        this.#sectionsLayerGroup = new LayerGroup()

        const view = new View({
            center: initialCenter,
            zoom: maxZoom,
        })
        const osmSource = new OSM()
        const tileLayer = new TileLayer({ source: osmSource })
        this.#map = new OLMap({
            target,
            view,
            layers: [tileLayer, this.#sectionsLayerGroup],
        })

        this.#selectInteraction = new Select({
            condition: (mapBrowserEvent) =>
                click(mapBrowserEvent) && noModifierKeys(mapBrowserEvent),
            style: this.#style({
                strokeColor: selectedStrokeColor,
                fillColor: selectedFillColor,
                width: 2,
            }),
        })
        this.#selectInteraction.on("select", this.#dispatchBpnID)
        this.#map.addInteraction(this.#selectInteraction)

        const hoverInteraction = new Select({
            condition: pointerMove,
            style: this.#style({
                strokeColor: "#3399CC",
                fillColor: "rgba(255,255,255,0.25)",
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
                strokeColor: "#3399CC",
                fillColor: "rgba(255,255,255,0.2)",
            }),
        })
        // FIXME: Voir si on peut faire ça plus proprement
        const layerArea = extent.getArea(layer.getSource().getExtent())
        layer.setZIndex(Math.max(10000 - layerArea * 1000, 1))
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

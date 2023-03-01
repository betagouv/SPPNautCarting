import "ol/ol.css"

import { Map as OLMap, View } from "ol"
import { click, noModifierKeys, pointerMove } from "ol/events/condition.js"
import * as extent from "ol/extent"
import GeoJSON from "ol/format/GeoJSON.js"
import Select from "ol/interaction/Select.js"
import { Image as ImageLayer } from "ol/layer.js"
import LayerGroup from "ol/layer/Group"
import TileLayer from "ol/layer/Tile"
import VectorLayer from "ol/layer/Vector"
import { useGeographic } from "ol/proj.js"
import { OSM, TileWMS, Vector as VectorSource } from "ol/source.js"
import ImageWMS from "ol/source/ImageWMS.js"
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
        const osmLayer = new TileLayer({ source: osmSource })
        const epavesLayer = new ImageLayer({
            source: new ImageWMS({
                url: "https://services.data.shom.fr/INSPIRE/wms/r?version=1.3.0",
                params: { LAYERS: "EPAVES_PYR-PNG_WLD_3857_WMSR" },
                ratio: 1,
                serverType: "geoserver",
            }),
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
                    url: "/carting/proxy",
                    params: { LAYERS: layer },
                    serverType: "geoserver",
                }),
                maxZoom: maxZoom,
                minZoom: minZoom,
            })
        })
        this.#map = new OLMap({
            target,
            view,
            layers: [
                //osmLayer,
                // rasterMarineLayer,
                // rasterMarineTileLayer,
                ...rasterMarineLayers,
                // epavesLayer,
                this.#sectionsLayerGroup,
            ],
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

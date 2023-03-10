import "ol/ol.css"

import { Map as OLMap, View } from "ol"
import TileLayer from "ol/layer/Tile"
import { useGeographic } from "ol/proj.js"
import { TileWMS } from "ol/source"

useGeographic()

export class Map {
    map
    #initialCenter
    #source
    #target
    #view
    #selectedInspireId

    constructor() {
        this.#target = "map"
        this.#initialCenter = [-2.0, 48.65]
        this.map = this.#initMap()
        this.#initListeners()
    }

    #initMap() {
        this.#view = new View({
            center: this.#initialCenter,
            zoom: 13,
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
        // const layers = [
        //     new TileLayer({
        //         source: new OSM(),
        //     }),
        // ]
        const LAYERS = "BALISAGE_BDD_WMSV"
        this.#source = new TileWMS({
            url: "/carting/proxy/wms",
            params: { TILED: true, LAYERS },
            serverType: "geoserver",
            // Countries have transparency, so do not fade tiles:
            // transition: 0,
        })
        const WMSLayer = new TileLayer({
            source: this.#source,
        })

        return new OLMap({
            target: this.#target,
            view: this.#view,
            layers: [...rasterMarineLayers, WMSLayer],
        })
    }

    #initListeners() {
        this.map.on("click", (event) => {
            const url = this.#source.getFeatureInfoUrl(
                event.coordinate,
                0.0001,
                "EPSG:4326",
                {
                    INFO_FORMAT: "application/json",
                },
            )

            console.log({ url, coords: event.coordinate })

            fetch(url)
                .then((response) => response.text())
                .then((jsonString) => {
                    console.log(jsonString)
                    const json = JSON.parse(jsonString)
                    this.#setInspireIdOnForm(json.features[0].properties.inspireid)
                })
        })
    }

    #setInspireIdOnForm(inspireId) {
        console.log("set inspire id", inspireId)
        document.getElementById("id_bdgs_object").value = inspireId
    }
}

window.addEventListener("DOMContentLoaded", () => {
    new Map()
})

import "ol/ol.css"

import { Map as OLMap, View } from "ol"
import GeoJSON from "ol/format/GeoJSON.js"
import TileLayer from "ol/layer/Tile"
import VectorLayer from "ol/layer/Vector"
import { useGeographic } from "ol/proj.js"
import { TileWMS } from "ol/source"
import VectorSource from "ol/source/Vector"
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

export class Map {
    map
    #initialCenter
    #geojsonLayer
    #source
    #target
    #view

    #initialStrokeColor = "red"
    #initialFillColor = "transparent"
    #initialWidth = 3

    #layerSelect = document.getElementById("layer-select")

    constructor() {
        this.#target = "map"
        this.#initialCenter = [-2.0, 48.65]
        this.map = this.#initMap()
        this.#initListeners()
        // FIXME : récupérer la géométrie existante sur l'objet bdgs lié et zommer dedans
    }

    #initMap() {
        this.#view = new View({
            center: this.#initialCenter,
            zoom: 13,
        })

        this.#geojsonLayer = new VectorLayer({
            source: new VectorSource({
                features: new GeoJSON().readFeatures(JSON.parse(document.getElementById("bdgs_geometry")!.textContent!)),
            }),
            style: buildStyle({
                strokeColor: this.#initialStrokeColor,
                fillColor: this.#initialFillColor,
                width: this.#initialWidth,
            }),
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

        const LAYERS = this.#layerSelect.value
        this.#source = new TileWMS({
            url: "/carting/proxy/wms",
            params: { TILED: true, LAYERS },
            serverType: "geoserver",
        })
        const WMSLayer = new TileLayer({
            source: this.#source,
        })

        return new OLMap({
            target: this.#target,
            view: this.#view,
            layers: [...rasterMarineLayers, WMSLayer, this.#geojsonLayer],
        })
    }

    #initListeners() {
        this.map.on("click", (event) => {
            const jsonUrl = this.#source.getFeatureInfoUrl(
                event.coordinate,
                0.0001,
                "EPSG:4326",
                {
                    INFO_FORMAT: "application/json",
                },
            )

            const htmlUrl = this.#source.getFeatureInfoUrl(
                event.coordinate,
                0.0001,
                "EPSG:4326",
                {
                    INFO_FORMAT: "text/html",
                },
            )
            fetch(jsonUrl)
                .then((response) => response.text())
                .then((jsonString) => {
                    this.#setInspireId(jsonString)
                })

            fetch(htmlUrl)
                .then((response) => response.text())
                .then((html) => {
                    this.#setWMSFeatureContent(html)
                })
        })

        this.#layerSelect?.addEventListener("change", (event) => {
            console.log(event)
            this.#source.updateParams({ TILED: true, LAYERS: event.target.value })
            this.#setWMSFeatureContent("")
        })
    }

    #setWMSFeatureContent(html) {
        document.getElementById("wms-feature").innerHTML = html
    }

    #setInspireId(jsonString) {
        const inspireId = JSON.parse(jsonString).features[0]?.properties.inspireid
        if (inspireId) {
            document.getElementById("id_bdgs_object").value = inspireId
        } else {
            this.#setWMSFeatureContent(`
            <div>
                <h2>Aucun objet trouvé à cet emplacement</h2>
            </div>
            `)
        }
    }
}

window.addEventListener("DOMContentLoaded", () => {
    new Map()
})

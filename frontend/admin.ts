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

    #initialStrokeColor = "red"
    #initialFillColor = "transparent"
    #initialWidth = 3

    #layerSelect = document.getElementById("layer-select") as HTMLSelectElement

    constructor() {
        this.#target = "map"
        this.#initialCenter = [-2.0, 48.65]
        this.map = this.#initMap()
        this.map.on("click", (event) => this.#readWMSAtCoordinate(event.coordinate))
        this.#layerSelect?.addEventListener("change", (event) => {
            console.log(event)
            this.#source.updateParams({ TILED: true, LAYERS: event.target.value })
            this.#setWMSFeatureContent("")
        })
    }

    #initMap() {
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

        const LAYERS = this.#layerSelect.value
        this.#source = new TileWMS({
            url: "/carting/proxy/wms",
            params: { TILED: true, LAYERS },
            serverType: "geoserver",
        })
        const WMSLayer = new TileLayer({
            source: this.#source,
        })

        const layers = [...rasterMarineLayers, WMSLayer]

        const view = new View({
            center: this.#initialCenter,
            zoom: 13,
        })
        const geojson = JSON.parse(
            document.getElementById("bdgs_geometry")!.textContent!,
        )
        if (geojson) {
            this.#geojsonLayer = new VectorLayer({
                source: new VectorSource({
                    features: new GeoJSON().readFeatures(geojson),
                }),
                style: buildStyle({
                    strokeColor: this.#initialStrokeColor,
                    fillColor: this.#initialFillColor,
                    width: this.#initialWidth,
                }),
            })
            layers.push(this.#geojsonLayer)

            view.fit(this.#geojsonLayer.getSource().getExtent(), {
                maxZoom: 13,
            })
            this.#readWMSAtCoordinate(view.getCenter())
        }

        return new OLMap({
            target: this.#target,
            view,
            layers,
        })
    }

    #readWMSAtCoordinate = (coordinate) => {
        const jsonUrl = this.#source.getFeatureInfoUrl(
            coordinate,
            0.0001,
            "EPSG:4326",
            {
                INFO_FORMAT: "application/json",
            },
        )

        const htmlUrl = this.#source.getFeatureInfoUrl(
            coordinate,
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

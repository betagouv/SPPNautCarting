import "ol/ol.css";

import { getCenter } from "ol/extent.js";
import GeoJSON from "ol/format/GeoJSON.js";
import LayerGroup from "ol/layer/Group";
import TileLayer from "ol/layer/Tile.js";
import Vector from "ol/layer/Vector.js";
import Map from "ol/Map.js";
import { useGeographic } from "ol/proj.js";
import { OSM, Vector as VectorSource } from "ol/source.js";
import View from "ol/View.js";

useGeographic();

const fooLayerGroup = new LayerGroup();
const map = new Map({
    layers: [
        new TileLayer({
            source: new OSM(),
        }),
        fooLayerGroup,
    ],
    target: "map",
    view: new View({
        center: [-2.0, 48.65],
        zoom: 12,
    }),
});
window.map = map;

var sppnaut_maps = document.querySelectorAll(".sppnaut-map");
for (var i = 0; i < sppnaut_maps.length; i++) {
    sppnaut_maps[i].addEventListener("click", (event) => {
        var source = new VectorSource({
            features: new GeoJSON().readFeatures(
                JSON.parse(event.target.dataset.geojson)
            ),
        });

        var layer = new Vector({
            source: source,
        });

        fooLayerGroup.getLayers().clear();
        fooLayerGroup.getLayers().push(layer);
        var layer_extent = layer.getSource().getExtent();
        map.getView().setCenter(getCenter(layer_extent));
        map.getView().fit(layer_extent, {
            maxZoom: 14,
            padding: [20, 20, 20, 20],
        });
    });
}

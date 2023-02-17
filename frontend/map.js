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

const sectionsLayerGroup = new LayerGroup();
const map = new Map({
    layers: [
        new TileLayer({
            source: new OSM(),
        }),
        sectionsLayerGroup,
    ],
    target: "map",
    view: new View({
        center: [-2.0, 48.65],
        zoom: 12,
    }),
});
// Expose map to help debug in the browser
window.map = map;

const geoSections = document.querySelectorAll("span[data-geojson]");
for (const geoSection of geoSections) {
    geoSection.addEventListener("click", showGeometry);
}

function showGeometry(event) {
    const source = new VectorSource({
        features: new GeoJSON().readFeatures(
            JSON.parse(event.target.dataset.geojson)
        ),
    });

    const layer = new Vector({
        source: source,
    });

    sectionsLayerGroup.getLayers().clear();
    sectionsLayerGroup.getLayers().push(layer);
    const layer_extent = layer.getSource().getExtent();
    map.getView().setCenter(getCenter(layer_extent));
    map.getView().fit(layer_extent, {
        maxZoom: 13,
        padding: [100, 100, 100, 100],
    });
}

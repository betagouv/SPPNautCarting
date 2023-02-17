import "ol/ol.css";

import { createEmpty, extend, getArea } from "ol/extent.js";
import GeoJSON from "ol/format/GeoJSON.js";
import LayerGroup from "ol/layer/Group";
import TileLayer from "ol/layer/Tile.js";
import Vector from "ol/layer/Vector.js";
import Map from "ol/Map.js";
import { useGeographic } from "ol/proj.js";
import { OSM, Vector as VectorSource } from "ol/source.js";
import View from "ol/View.js";

useGeographic();

// FIXME : make the functions of this file in object structure

const sectionsLayerGroup = new LayerGroup();
const highlightClass = 'sppnaut-bg-color-yellow';
const mapElement = document.querySelector("#map");
const map = new Map({
    layers: [
        new TileLayer({
            source: new OSM(),
        }),
        sectionsLayerGroup,
    ],
    target: mapElement,
    view: new View({
        center: [-2.0, 48.65],
        zoom: 12,
    }),
});

map.on('singleclick', function (evt) {
    let feature = map.forEachFeatureAtPixel(evt.pixel, function (feature, layer) {
        return feature;
    });
    focusSectionOnText(feature.get('pk'))
});

const geoSections = document.querySelectorAll("[data-geojson]");
for (const geoSection of geoSections) {
    geoSection.addEventListener("click", showGeometry);
}
showAllGeometries(geoSections);

function showGeometry(event) {
    sectionsLayerGroup.getLayers().clear();
    const features = new GeoJSON().readFeatures(
        JSON.parse(event.target.dataset.geojson)
    )
    if (features.length > 0) {
        focusSectionOnText(features[0].get('pk'))
    }
    setSectionsLayerGroup(features);
    fitMap();
}

function showAllGeometries(sections) {
    sectionsLayerGroup.getLayers().clear();
    for (let i = 0; i < sections.length; i++) {
        let features = new GeoJSON().readFeatures(
            JSON.parse(sections[i].dataset.geojson)
        )
        setSectionsLayerGroup(features);
    }
    fitMap();
}

function focusSectionOnText(section_pk) {
    let highlighteds = document.getElementsByClassName(highlightClass)
    for (let i = 0; i < highlighteds.length; i++) {
        highlighteds[i].classList.remove(highlightClass)
    }
    const sectionInText = document.getElementById(section_pk)
    sectionInText.scrollIntoView({ behavior: "smooth" });
    sectionInText.classList.add(highlightClass)
}

function setSectionsLayerGroup(features) {
    const layer = new Vector({
        source: new VectorSource({
            features: features,
        }),
    });
    let layerArea = getArea(layer.getSource().getExtent())
    layer.setZIndex(Math.max(10000 - layerArea * 1000, 1))
    sectionsLayerGroup.getLayers().push(layer);
}

function fitMap() {
    let sectionsLayerGroupExtent = createEmpty();
    sectionsLayerGroup.getLayers().forEach(layer => {
        const layerExtent = layer.getSource().getExtent();
        extend(sectionsLayerGroupExtent, layerExtent);
    })
    if (sectionsLayerGroup.getLayers().getLength() > 0) {
        map.getView().fit(sectionsLayerGroupExtent, {
            maxZoom: 13,
            padding: [100, 100, 100, 100],
            duration: 300,
        });
    }
}

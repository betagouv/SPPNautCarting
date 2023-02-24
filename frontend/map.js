import "ol/ol.css"

import { createEmpty, extend, getArea } from "ol/extent.js"
import GeoJSON from "ol/format/GeoJSON.js"
import LayerGroup from "ol/layer/Group"
import TileLayer from "ol/layer/Tile.js"
import Vector from "ol/layer/Vector.js"
import Map from "ol/Map.js"
import { useGeographic } from "ol/proj.js"
import { OSM, Vector as VectorSource } from "ol/source.js"
import { Circle, Fill, Stroke, Style } from "ol/style.js"
import View from "ol/View.js"

useGeographic()

const defaultCenter = [-2.0, 48.65];
const defaultZoom = 13;
const defaultPadding = [100, 100, 100, 100];
const defaultDuration = 300;
const defaultHighlightColor = "rgb(255,255,0)";
const defaultHighlightColorFill = "rgb(255,255,0,0.3)";

const sectionsLayerGroup = new LayerGroup()
const mapElement = document.querySelector("#map")
const map = new Map({
    layers: [
        new TileLayer({
            source: new OSM(),
        }),
        sectionsLayerGroup,
    ],
    target: mapElement,
    view: new View({
        center: defaultCenter,
        zoom: defaultZoom,
    }),
})
const stroke = new Stroke({
    color: defaultHighlightColor,
    width: 4,
})
const fill = new Fill({
    color: defaultHighlightColorFill,
})
const selectedStyle = new Style({
    fill: fill,
    stroke: stroke,
    image: new Circle({
        radius: 5,
        stroke: stroke,
        fill: fill,
    }),
})
});
map.on('singleclick', olEvent => {
    mapElement.dispatchEvent(new CustomEvent('ol:click', {
        detail: {
            olEvent: olEvent,
        }
    }));
})


export function getHigherLayer(evt) {
    const higherLayer = map.forEachFeatureAtPixel(evt.pixel, function (feature, layer) {
        return layer;
    });
    if (!higherLayer) return;
    return higherLayer;
}

export function highlightMapSection(bpnID) {
    const layer = sectionsLayerGroup.getLayers().getArray().find(layer => layer.get('bpnID') === bpnID)
    if (!layer) return;
    fitMapToExtend(layer.getSource().getExtent())
    highlightSelectedLayer(layer)
}


function highlightSelectedLayer(layer) {
    sectionsLayerGroup.getLayers().forEach((eachLayer) => {
        if (eachLayer.get("selected")) {
            eachLayer.set("selected", false)
            eachLayer.setStyle(undefined)
        }
    })
    layer.set('selected', true)
    layer.setStyle(selectedStyle);
}


export function showGeometry(bpnID, geojson) {
    sectionsLayerGroup.getLayers().clear();
    addGeometryToLayerGroup(bpnID, geojson)
    focusSectionOnText(bpnID)
    fitMapToLayerGroup();
}

export function centerToGeometry(bpnID) {
    const layer = sectionsLayerGroup.getLayers().getArray().find(layer => layer.get('bpnID') === bpnID)
    highlightSelectedLayer(layer)
    fitMapToExtend(layer.getSource().getExtent())
    focusSectionOnText(bpnID)
}

export function addGeometryToLayerGroup(bpnID, geojson) {
    const layer = new Vector({
        source: new VectorSource({
            features: new GeoJSON().readFeatures(geojson),
        }),
    })
    //FIXME: Voir si on peut faire ça plus proprement
    const layerArea = getArea(layer.getSource().getExtent())
    layer.setZIndex(Math.max(10000 - layerArea * 1000, 1))
    sectionsLayerGroup.getLayers().push(layer);

    layer.set('bpnID', bpnID)
}

export function fitMapToLayerGroup() {
    const sectionsLayerGroupExtent = createEmpty()
    sectionsLayerGroup.getLayers().forEach((layer) => {
        const layerExtent = layer.getSource().getExtent()
        extend(sectionsLayerGroupExtent, layerExtent)
    })
    fitMapToExtend(sectionsLayerGroupExtent)
}

function fitMapToExtend(extent) {
    map.getView().fit(extent, {
        maxZoom: defaultZoom,
        padding: defaultPadding,
        duration: defaultDuration,
    })
}

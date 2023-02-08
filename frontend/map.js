import "ol/ol.css";

import TileLayer from 'ol/layer/Tile.js';
import Map from 'ol/Map.js';
import { useGeographic } from 'ol/proj.js';
import OSM from 'ol/source/OSM.js';
import View from 'ol/View.js';
useGeographic();

const map = new Map({
    layers: [
        new TileLayer({
            source: new OSM(),
        }),
    ],
    target: 'map',
    view: new View({
        center: [-2, 48],
        zoom: 12,
    }),
});

import "ol/ol.css";

import Feature from "ol/Feature.js";
import Point from 'ol/geom/Point.js';
import TileLayer from 'ol/layer/Tile.js';
import Vector from 'ol/layer/Vector.js';
import Map from 'ol/Map.js';
import { useGeographic } from 'ol/proj.js';
import { OSM, Vector as VectorSource } from 'ol/source.js';

import { Circle, Fill, Stroke, Style } from "ol/style.js";
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
        center: [-2.017364501953125, 48.65468584817256],
        zoom: 12,
    }),
});

var sppnaut_maps = document.querySelectorAll(".sppnaut-map");
for (var i = 0; i < sppnaut_maps.length; i++) {
    sppnaut_maps[i].addEventListener("click", event => {
        var x = parseFloat(event.target.dataset.x.replace(/,/g, '.'))
        var y = parseFloat(event.target.dataset.y.replace(/,/g, '.'))
        var coordonnee = [x,y];

        var point = new Point(coordonnee, 'XY');
        var point_feature = new Feature ( point );
        var imageStyle = new Style({
            image: new Circle({
                radius: 5,
                snapToPixel: false,
                fill: new Fill({
                color: [255 , 0 , 0 , 0.2]
            }),
            stroke: new Stroke({
                color: [255 , 0 , 0 , 1],
                width: 1
            })
            })
        });
        point_feature.setStyle(imageStyle);

        var layer = new Vector({
            source: new VectorSource({
                features: [
                    point_feature
                ]
            })
        });
        map.addLayer(layer);
    });
}

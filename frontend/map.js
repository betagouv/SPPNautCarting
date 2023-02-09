import "ol/ol.css";

import { getCenter } from 'ol/extent.js';
import Feature from "ol/Feature.js";
import GeoJSON from 'ol/format/GeoJSON.js';
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
        center: [-2.0, 48.65],
        zoom: 12,
    }),
});

var imageStyle = new Style({
    image: new Circle({
        radius: 5,
        snapToPixel: false,
        fill: new Fill({
            color: [255, 0, 0, 0.2]
        }),
        stroke: new Stroke({
            color: [255, 0, 0, 1],
            width: 1
        })
    })
});

var sppnaut_maps = document.querySelectorAll(".sppnaut-map");
for (var i = 0; i < sppnaut_maps.length; i++) {
    sppnaut_maps[i].addEventListener("click", event => {
        var geom_type = event.target.dataset.type
        var geom_coords = event.target.dataset.geom

        if (geom_type == 'Point') {
            // remplacer en utilisant geom_coords
            var x = parseFloat(event.target.dataset.x.replace(/,/g, '.'))
            var y = parseFloat(event.target.dataset.y.replace(/,/g, '.'))
            var coordonnee = [x, y];
            console.log(coordonnee)
            var point = new Point(coordonnee, 'XY');
            var feature = new Feature(point);
            feature.setStyle(imageStyle);

            var source = new VectorSource({
                features: [
                    feature
                ]
            });

        } else if (geom_type == 'Polygon') {
            const geojsonObject = {
                'type': 'FeatureCollection',
                'crs': {
                    'type': 'name',
                    'properties': {
                        'name': 'EPSG:3857',
                    },
                },
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Polygon',
                            'coordinates': [[[-1.770000457763672, 48.60340355404897], [-1.7827033996582033, 48.60419814619142], [-1.7811584472656248, 48.597841059021896], [-1.7708587646484375, 48.595570476850746], [-1.7657089233398438, 48.599203359339896], [-1.770000457763672, 48.60340355404897]]]
                            //'coordinates': geom_coords
                        },
                    }
                ],
            };

            var source = new VectorSource({
                features: new GeoJSON().readFeatures(geojsonObject),
            });
        }

        var layer = new Vector({
            source: source
        });

        map.addLayer(layer);
        var layer_extent = layer.getSource().getExtent();
        var center = getCenter(layer_extent);
        map.setView(new View({
            center: [center[0], center[1]],
            zoom: 12
        }));
    });
}


// var sppnaut_maps = document.querySelectorAll(".sppnaut-map");
// for (var i = 0; i < sppnaut_maps.length; i++) {
//     sppnaut_maps[i].addEventListener("click", event => {
//         var geom_type = event.target.dataset.type

//         var x = parseFloat(event.target.dataset.x.replace(/,/g, '.'))
//         var y = parseFloat(event.target.dataset.y.replace(/,/g, '.'))
//         var coordonnee = [x, y];

//         var point = new Point(coordonnee, 'XY');
//         var point_feature = new Feature(point);
//         point_feature.setStyle(imageStyle);

//         var layer = new Vector({
//             source: new VectorSource({
//                 features: [
//                     point_feature
//                 ]
//             })
//         });
//         map.addLayer(layer);
//         var layer_extent = layer.getSource().getExtent();
//         var center = getCenter(layer_extent);
//         map.setView(new View({
//             center: [center[0], center[1]],
//             zoom: 10
//         }));
//     });
// }

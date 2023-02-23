import { Controller } from "@hotwired/stimulus";
import { debounce } from "lodash";
import { addGeometryToLayerGroup, centerToGeometry, fitMapToLayerGroup } from "./map";

export default class extends Controller {
    static targets = ["section"]

    sectionTargetConnected(sectionTarget) {
        const geojson = JSON.parse(sectionTarget.dataset.mapGeojsonParam)
        addGeometryToLayerGroup(sectionTarget.dataset.mapBpnidParam, geojson)
        this.#showLayerGroupSoon()
    }

    showOnMap(event) {
        const geojson = event.params.geojson
        //showGeometry(event.params.bpnid, geojson)
        centerToGeometry(event.params.bpnid, geojson)
    }

    #showLayerGroupSoon = debounce(fitMapToLayerGroup)

}

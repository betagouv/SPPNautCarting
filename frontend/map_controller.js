import { Controller } from "@hotwired/stimulus"
import { debounce } from "lodash"
import {
    addGeometryToLayerGroup,
    fitMapToLayerGroup,
    getHigherLayer,
    highlightMapSection,
} from "./map"

export default class extends Controller {
    static targets = ["section"]

    connect() {
        this.highlightMapSection()
    }

    #showLayerGroupSoon = debounce(fitMapToLayerGroup)

    sectionTargetConnected(sectionTarget) {
        const geojson = JSON.parse(sectionTarget.dataset.mapGeojsonParam)
        addGeometryToLayerGroup(sectionTarget.dataset.mapBpnidParam, geojson)
        this.#showLayerGroupSoon()
    }

    showOnMap(event) {
        const geojson = event.params.geojson
        location.hash = event.params.bpnid
    }

    focusOnSection(event) {
        const layer = getHigherLayer(event.detail.olEvent)
        location.hash = layer.get("bpnID")
    }
    highlightMapSection() {
        highlightMapSection(location.hash.split("#")[1])
    }
}

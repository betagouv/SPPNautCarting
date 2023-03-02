import { Controller } from "@hotwired/stimulus"
import { SectionMap } from "./section_map"

export default class extends Controller {
    #map

    static targets = ["map", "section"]
    static values = {
        initialCenter: { type: Array, default: [-2.0, 48.65] },
        maxZoom: { type: Number, default: 13 },
    }

    initialize() {
        this.#map = new SectionMap({
            target: this.mapTarget,
            initialCenter: this.initialCenterValue,
            maxZoom: this.maxZoomValue,
        })
    }

    connect() {
        this.#map.fitViewToAllSections()
        this.selectSectionInMapFromHash()
    }

    sectionTargetConnected(sectionTarget) {
        const geojson = JSON.parse(sectionTarget.dataset.geojson)
        this.#map.addSection(sectionTarget.dataset.bpnId, geojson)
    }

    selectSectionInText(event) {
        location.hash = event.detail.bpnID
    }

    selectSectionInMapFromHash() {
        const bpnID = location.hash.split("#")[1]
        if (!bpnID) {
            return
        }
        this.#map.selectSection(bpnID)
    }
}

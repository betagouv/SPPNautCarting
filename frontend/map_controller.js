import { Controller } from "@hotwired/stimulus"
import { SectionMap } from "./section_map"

export default class extends Controller {
    #map

    static targets = ["map", "section"]
    static values = {
        initialCenter: { type: Array, default: [-2.0, 48.65] },
        maxZoom: { type: Number, default: 13 },
        padding: { type: Array, default: [20, 20, 20, 20] },
        duration: { type: Number, default: 300 },
        selectedStrokeColor: { type: String, default: "#000091" },
        selectedFillColor: { type: String, default: "#00009108" },
    }

    initialize() {
        this.#map = new SectionMap({
            target: this.mapTarget,
            initialCenter: this.initialCenterValue,
            maxZoom: this.maxZoomValue,
            padding: this.paddingValue,
            duration: this.durationValue,
            selectedFillColor: this.selectedFillColorValue,
            selectedStrokeColor: this.selectedStrokeColorValue,
        })
    }

    connect() {
        this.#map.fitViewToAllSections()
        this.selectSectionInMap()
    }

    sectionTargetConnected(sectionTarget) {
        const geojson = JSON.parse(sectionTarget.dataset.geojson)
        this.#map.addSection(sectionTarget.dataset.bpnId, geojson)
    }

    selectSectionInText(e) {
        location.hash = e.detail.bpnID
    }

    selectSectionInMap() {
        const bpnID = location.hash.split("#")[1]
        if (!bpnID) {
            return
        }
        this.#map.selectSection(bpnID)
    }
}

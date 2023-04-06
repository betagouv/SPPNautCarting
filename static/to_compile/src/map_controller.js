import { Controller } from "@hotwired/stimulus"
import { SectionMap } from "./section_map"

export default class extends Controller {
    #map

    static targets = ["map", "geojson", "featurePopin"]
    static values = {
        initialCenter: { type: Array, default: [-2.0, 48.65] },
        maxZoom: { type: Number, default: 13 },
        wmsUrl: String,
    }

    connect() {
        this.#map = new SectionMap({
            target: this.mapTarget,
            initialCenter: this.initialCenterValue,
            maxZoom: this.maxZoomValue,
            geojson: this.geojsonTarget.textContent,
            wmsUrl: this.wmsUrlValue,
        })

        this.#map.fitViewToAllSections()
        this.selectSectionInMapFromHash()
    }

    selectSectionInText(event) {
        location.hash = event.detail.bpnID
    }

    selectSectionInMapFromHash() {
        const bpnID = location.hash.replace("#", "")
        if (!bpnID) {
            return
        }
        this.#map.selectSection(bpnID)
    }

    showFeaturePopin(event) {
        this.#popinController.show(event.detail.html)
    }

    closeFeaturePopin() {
        this.#popinController.close()
    }

    get #popinController() {
        return this.application.getControllerForElementAndIdentifier(
            this.featurePopinTarget,
            "popin",
        )
    }
}

import { Controller } from "@hotwired/stimulus"
import type { default as PopinController } from "./popin_controller"

import { Coordinate } from "ol/coordinate"
import { SectionMap } from "./section_map"

export default class extends Controller<HTMLElement> {
    #map

    static targets = ["map", "geojson", "featurePopin"]
    readonly mapTarget: HTMLElement
    readonly geojsonTarget: HTMLScriptElement
    readonly featurePopinTarget: HTMLElement

    static values = {
        initialCenter: { type: Array, default: [-2.0, 48.65] },
        maxZoom: { type: Number, default: 13 },
        wmsUrl: String,
    }
    readonly initialCenterValue: Coordinate
    readonly maxZoomValue: number
    readonly wmsUrlValue: string

    connect() {
        this.#map = new SectionMap({
            target: this.mapTarget,
            initialCenter: this.initialCenterValue,
            maxZoom: this.maxZoomValue,
            geojson: this.geojsonTarget.textContent!,
            wmsUrl: this.wmsUrlValue,
            fullscreenElement: this.element,
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

    highlightSectionInMap(e) {
        this.#map.highlightSection(e.target.getAttribute("href").replace("#", ""))
    }

    unhighlightSectionInMap(e) {
        this.#map.unhighlightSection()
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
        ) as PopinController
    }
}

import { Controller } from "@hotwired/stimulus"
import type { FrameElement } from "@hotwired/turbo"

import type { Coordinate } from "ol/coordinate"
import type { Extent } from "ol/extent"

import type { default as PopinController } from "./popin_controller"
import { SectionMap } from "./section_map"

export default class extends Controller<HTMLElement> {
    #map: SectionMap

    static targets = ["map", "geojson", "featurePopin", "turboframe"]
    readonly mapTarget: HTMLElement
    readonly geojsonTarget: HTMLScriptElement
    readonly featurePopinTarget: HTMLElement
    readonly turboframeTarget: FrameElement

    static values = {
        initialCenter: { type: Array, default: [-2.0, 48.65] },
        maxZoom: { type: Number, default: 13 },
        wmsUrl: String,
        bbox: Array,
    }
    readonly initialCenterValue: Coordinate
    readonly maxZoomValue: number
    readonly wmsUrlValue: string
    readonly hasBboxValue: boolean
    readonly bboxValue: Extent

    initialize() {
        this.#map = new SectionMap({
            target: this.mapTarget,
            initialCenter: this.initialCenterValue,
            maxZoom: this.maxZoomValue,
            geojson: this.geojsonTarget.textContent!,
            wmsUrl: this.wmsUrlValue,
            fullscreenElement: this.element,
        })
        this.#map.fitViewToAllSections()

        if (this.hasBboxValue) {
            this.#map.fitMapToExtent(this.bboxValue, { withAnimation: false })
        }

        this.selectSectionInMapFromHash()
    }

    geojsonTargetConnected() {
        this.#map.updateGeoJson(this.geojsonTarget.textContent)
    }

    updateBboxInUrl(event) {
        const { bbox, zoom } = event.detail

        const url = new URL(location.href)
        url.searchParams.set("bbox", bbox)
        url.searchParams.set("zoom", zoom)
        this.turboframeTarget.src = url.toString()
        // FIXME : turbo does not update the url when the bbox changes
        // It requires one click inside the frame, and after it works properly
        // Similar issue https://github.com/hotwired/turbo/issues/489
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

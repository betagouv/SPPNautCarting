import { Controller } from "@hotwired/stimulus"

export default class extends Controller<HTMLElement> {
    static targets = ["content"]
    readonly contentTarget: HTMLElement

    show(html) {
        this.contentTarget.innerHTML = html
        // Can't use element.ariaHidden until Firefox implements it
        // https://bugzilla.mozilla.org/show_bug.cgi?id=1785412
        this.element.setAttribute("aria-hidden", "false")
    }

    close() {
        this.element.setAttribute("aria-hidden", "true")
    }
}

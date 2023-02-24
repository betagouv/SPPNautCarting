import { Application } from "@hotwired/stimulus"

import MapController from "./map_controller"

window.Stimulus = Application.start()
Stimulus.register("map", MapController)
Stimulus.debug = true

import { Application } from "@hotwired/stimulus"

import MapController from "./map_controller"
import PopinController from "./popin_controller"

window.stimulus = Application.start()
stimulus.register("map", MapController)
stimulus.register("popin", PopinController)

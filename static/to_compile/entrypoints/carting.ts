import { Application } from "@hotwired/stimulus"
import * as Turbo from "@hotwired/turbo"

import MapController from "../src/map_controller"
import PopinController from "../src/popin_controller"

window.stimulus = Application.start()
stimulus.register("map", MapController)
stimulus.register("popin", PopinController)

Turbo.session.drive = false

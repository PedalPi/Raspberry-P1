# -*- coding: utf-8 -*-
from application.architecture.Component import Component
from raspberry_p1.action.actions_facade import ActionsFacade
from raspberry_p1.action.updates_observer_p1 import UpdatesObserverP1
from raspberry_p1.component.components import Components
from raspberry_p1.configurations import Configurations
from raspberry_p1.mvc.patches.patches_controller import PatchesController


class RaspberryP1(Component):
    """
    Manager the current patch (with next and before patch buttons),
    a status effect and effect parameters

    :param Application application: Class application
    :param string configuration_file: Change the number pins. View raspberry_p1/config.ini for example
    """

    def __init__(self, application, configuration_file="raspberry_p1/config.ini"):
        super(RaspberryP1, self).__init__(application)

        self.app = application
        self.config = Configurations(configuration_file)

        self.components = self.init_components(self.config)
        self.observer = UpdatesObserverP1()
        self.register_observer(self.observer)

        self.actions = ActionsFacade(application)

        self.mvc = {
            'controllers': self.init_mvc_controllers(self)
        }

    def init(self):
        controller = self.mvc['controllers'][PatchesController]
        controller.start()
        controller.init(self.actions.current_patch)

    def init_components(self, configurations):
        components = dict()

        components[Components.DISPLAY] = configurations.display
        components[Components.NEXT_PATCH] = configurations.next_patch_button
        components[Components.BEFORE_PATCH] = configurations.before_patch_button
        components[Components.EFFECT] = configurations.effect
        components[Components.ROTARY_ENCODER] = configurations.rotary_encoder

        return components

    def init_mvc_controllers(self, equipment):
        return {
            PatchesController: PatchesController(equipment)
        }

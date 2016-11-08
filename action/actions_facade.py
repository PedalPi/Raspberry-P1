from application.controller.CurrentController import CurrentController
from application.controller.ComponentDataController import ComponentDataController
from application.controller.EffectController import EffectController

from raspberry_p1.action.data import Data


class ActionsFacade(object):
    TOKEN = 'raspberry-p1-token'

    def __init__(self, application):
        self.app = application
        self.data = Data(self.app.controller(ComponentDataController), ActionsFacade.TOKEN)

    @property
    def current_patch(self):
        controller = self.app.controller(CurrentController)
        return controller.currentPatch

    @property
    def current_effect(self):
        return self.current_effect_of_patch(self.current_patch)

    def current_effect_of_patch(self, patch):
        patch_data = self.data.patch(patch)

        try:
            current_effect = patch_data['current']
        except KeyError:
            patch_data['current'] = 0
            current_effect = 0

        self.data.update_patch(patch, patch_data)

        try:
            return patch.effects[current_effect]
        except IndexError:
            del patch_data['current']
            self.data.update_patch(patch, patch_data)
            return None

    @current_effect.setter
    def current_effect(self, effect):
        patch = self.current_patch

        patch_data = self.data.patch(patch)
        patch_data['current'] = effect.index

        self.data.update_patch(patch, patch_data)

    def to_next_patch(self):
        controller = self.app.controller(CurrentController)

        controller.toNextPatch(ActionsFacade.TOKEN)
        return controller.currentPatch

    def to_before_patch(self):
        controller = self.app.controller(CurrentController)

        controller.toBeforePatch(ActionsFacade.TOKEN)
        return controller.currentPatch

    def toggle_status_effect(self, effect):
        controller = self.app.controller(EffectController)
        controller.toggleStatus(effect, ActionsFacade.TOKEN)

    def set_param_value(self, param, new_value):
        effect = param.effect
        controller = self.app.controller(CurrentController)
        controller.setEffectParam(effect.index, param.index, new_value, ActionsFacade.TOKEN)

from application.controller.CurrentController import CurrentController
from application.controller.ComponentDataController import ComponentDataController
from application.controller.EffectController import EffectController


class ActionsFacade(object):
    TOKEN = 'raspberry-p1-token'

    def __init__(self, application):
        self.app = application

    @property
    def current_patch(self):
        controller = self.app.controller(CurrentController)
        return controller.currentPatch

    @property
    def current_effect(self):
        controller = self.app.controller(CurrentController)
        patch = controller.currentPatch

        return self.current_effect_of_patch(patch)

    def current_effect_of_patch(self, patch):
        try:
            banks = self.data['banks']
        except KeyError:
            banks = {}

        try:
            bank = banks[patch.bank.index]
        except KeyError:
            banks[patch.bank.index] = {}
            bank = banks[patch.bank.index]

        try:
            patch_data = bank[patch.index]
        except KeyError:
            bank[patch.index] = {}
            patch_data = bank[patch.index]

        try:
            current_effect = patch_data['current']
        except KeyError:
            patch_data['current'] = 0
            current_effect = 0

        self.data['banks'] = banks

        try:
            return patch.effects[current_effect]
        except IndexError:
            return None

    @property
    def data(self):
        return self.app.controller(ComponentDataController)[ActionsFacade.TOKEN]

    @data.setter
    def data(self, data):
        self.app.controller(ComponentDataController)[ActionsFacade.TOKEN] = data

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

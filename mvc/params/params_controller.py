from raspberry_p1.mvc.controller import Controller
from raspberry_p1.mvc.params.params_view import ParamsView


class ParamsController(Controller):

    def __init__(self, equipment):
        super().__init__(equipment, ParamsView)
        self.current_effect = None
        self.current_param = None

    def init(self, param):
        self.current_effect = param.effect
        self.current_param = param

        self.view.show_param(self.current_param)

    @property
    def params(self):
        return self.current_effect.params

    ##########################
    # Actions - Param
    ##########################
    def to_next_param(self):
        index = self.current_param.index + 1

        if index == len(self.params):
            index = 0

        self.to_param(index)

    def to_param(self, param_index):
        self.init(self.current_effect.params[param_index])

    ##########################
    # Actions - Param value
    ##########################
    def add_value(self):
        maximum = self.current_param['ranges']['maximum']
        new_value = self.current_param.value + 1

        if new_value > maximum:
            new_value = maximum

        self.set_value(new_value)

    def minus_value(self):
        minimum = self.current_param['ranges']['minimum']
        new_value = self.current_param.value - 1

        if new_value < minimum:
            new_value = minimum

        self.set_value(new_value)

    def set_value(self, new_value):
        self.actions.set_param_value(self.current_param, new_value)
        self.init(self.current_param)

    ##########################
    # Set controller
    ##########################
    def to_patches_controller(self, patch):
        from raspberry_p1.mvc.patches.patches_controller import PatchesController
        self.start_controller(PatchesController, patch)

    def to_effects_controller(self):
        from raspberry_p1.mvc.effects.effects_controller import EffectsController
        self.start_controller(EffectsController, self.current_effect)

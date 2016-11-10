from raspberry_p1.mvc.p1_view import P1View


class ParamsView(P1View):

    def init(self, controller):
        self.controller = controller

    def init_components_actions(self):
        self.effect.action = lambda *args: ...#self.controller.return_to_params_controller

        self.next_patch.action = lambda *args: ...#self.controller.return_to_params_controller
        self.before_patch.action = lambda *args: ...#self.controller.return_to_params_controller

        self.rotary_encoder.when_selected = self.controller.to_next_param
        self.rotary_encoder.when_rotated = self.when_rotary_rotated

    def when_rotary_rotated(self, state):
        if state == 1:
            self.controller.add_value()
        else:
            self.controller.minus_value()

    def show_param(self, param):
        self.display.show_param(param)

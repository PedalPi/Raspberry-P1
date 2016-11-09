from raspberry_p1.mvc.p1_view import P1View


class EffectsView(P1View):

    def init_components_actions(self):
        self.effect.action = self.controller.toggle_status_effect

        self.next_patch.action = self.controller.to_next_patch
        self.before_patch.action = self.controller.to_before_patch

        self.rotary_encoder.when_rotated = self.when_rotary_rotated
        self.rotary_encoder.when_selected = lambda *args: ...#self.controller.to_effects_controller

    def when_rotary_rotated(self, state):
        if state == 1:
            self.controller.to_next_effect()
        else:
            self.controller.to_before_effect()

    def show_effect(self, effect):
        self.display.show_effect(effect)
        self.effect.effect = effect

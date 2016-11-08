from raspberry_p1.mvc.p1_view import P1View


class PatchesView(P1View):

    def init_components_actions(self):
        self.effect.action = self.controller.toggle_status_effect

        self.next_patch.action = self.controller.to_next_patch
        self.before_patch.action = self.controller.to_before_patch

        self.rotary_encoder.when_rotated = lambda *args: ...
        self.rotary_encoder.when_pressed = self.controller.to_effects_controller

    def show_patch(self, patch, effect):
        self.display.show_patch(patch)
        self.effect.effect = effect

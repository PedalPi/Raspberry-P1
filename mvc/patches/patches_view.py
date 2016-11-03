from raspberry_p1.mvc.view import View
from raspberry_p1.component.components import Components


class PatchesView(View):
    controller = None

    display = None
    next_patch = None
    before_patch = None
    effect = None
    rotary_encoder = None

    def init(self, controller):
        self.controller = controller

    def init_components(self, components):
        self.display = components[Components.DISPLAY]

        self.next_patch = components[Components.NEXT_PATCH]
        self.before_patch = components[Components.BEFORE_PATCH]

        self.effect = components[Components.EFFECT]

        self.rotary_encoder = components[Components.ROTARY_ENCODER]

    def init_components_actions(self):
        self.effect.action = self.controller.toggle_status_effect

        self.next_patch.action = self.controller.to_next_patch
        self.before_patch.action = self.controller.to_before_patch

        self.rotary_encoder.when_rotated = lambda: ...
        self.rotary_encoder.when_selected = self.controller.to_effects_controller

    def show_patch(self, patch, effect):
        self.display.show_patch(patch)
        self.effect.effect = effect

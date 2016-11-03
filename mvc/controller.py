# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Controller(metaclass=ABCMeta):

    def __init__(self, equipment, view_class):
        self.equipment = equipment
        self.view = view_class()

    @abstractmethod
    def init(self, *args):
        raise NotImplementedError()

    def start(self):
        self.view.init(self)
        self.view.init_components(self.equipment.components)
        self.view.init_components_actions()
        self.register()

    def register(self):
        self.equipment.observer.register(self)

    @property
    def actions(self):
        return self.equipment.actions

    def on_current_patch_change(self, patch, token=None):
        pass

    def on_bank_update(self, bank, update_type, token=None):
        pass

    def on_patch_updated(self, patch, update_type, token=None):
        pass

    def on_effect_updated(self, effect, update_type, token=None):
        pass

    def on_effect_status_toggled(self, effect, token=None):
        pass

    def on_param_value_change(self, param, token=None):
        pass

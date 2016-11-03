from gpiozero.pins.mock import MockPin
from configparser import ConfigParser

from raspberry_p1.component.pcd8544_display import PCD8544Display
from raspberry_p1.component.patch_component import PatchComponent
from raspberry_p1.component.effect_component import EffectComponent

from physical.component.rotary_encoder import RotaryEncoderWithButton


class Configurations(object):
    """
    Configure the pins based in
    https://pinout.xyz/ pinout number
    """
    def __init__(self, configuration_file):
        self.display = None
        self.next_patch_button = None
        self.before_patch_button = None
        self.effect = None
        self.rotary_encoder = None

        config = self._parse_configuration(configuration_file)
        config = self._prepare_pins(config)
        self.configure(config)

    def _parse_configuration(self, configuration_file):
        config_parser = ConfigParser()
        config_parser.read(configuration_file)

        data = config_parser['DEFAULT']

        keys = data.keys()

        config = dict()
        config['test'] = config_parser['test']['test'] == 'True'

        config['display'] = dict()
        pin_keys = filter(lambda key: key.startswith('display_'), keys)
        for key in pin_keys:
            config['display'][key] = int(data[key])

        config['rotary_encoder'] = dict()
        pin_keys = filter(lambda key: key.startswith('rotary_encoder_'), keys)
        for key in pin_keys:
            config['rotary_encoder'][key] = int(data[key])

        config['next_patch'] = int(data['next_patch'])
        config['before_patch'] = int(data['before_patch'])
        config['effect_button'] = int(data['effect_button'])
        config['effect_led'] = int(data['effect_led'])

        return config

    def _prepare_pins(self, config):
        test = config['test']

        if not test:
            return config

        for key, value in config['display'].items():
            config['display'][key] = MockPin(value)
        for key, value in config['rotary_encoder'].items():
            config['rotary_encoder'][key] = MockPin(value)

        config['next_patch'] = MockPin(config['next_patch'])
        config['before_patch'] = MockPin(config['before_patch'])
        config['effect_button'] = MockPin(config['effect_button'])
        config['effect_led'] = MockPin(config['effect_led'])

        return config

    def configure(self, config):
        display_pins = config['display']
        self.display = PCD8544Display(
            dc=display_pins['display_dc'],
            sclk=display_pins['display_sclk'],
            din=display_pins['display_din'],
            cs=display_pins['display_cs'],
            rst=display_pins['display_rst'],
            contrast=60
        )

        self.next_patch_button = PatchComponent(config['next_patch'], pull_up=True)
        self.before_patch_button = PatchComponent(config['before_patch'], pull_up=True)

        self.effect = EffectComponent(
            pin_button=config['effect_button'],
            pin_led=config['effect_led'],
            pull_up=True
        )

        rotary_encoder = config['rotary_encoder']
        self.rotary_encoder = RotaryEncoderWithButton(
            pin_a=rotary_encoder['rotary_encoder_a'],
            pin_b=rotary_encoder['rotary_encoder_b'],
            button_pin=rotary_encoder['rotary_encoder_button'],
            pull_up=True
        )

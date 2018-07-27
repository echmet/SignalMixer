import json


class Configuration:
    def __init__(self):
        try:
            cfg_file = open('smconfig.json')
            self._cfg = json.load(cfg_file)
        except IOError:
            self._cfg = dict()

    def get_value(self, key):
        if key not in self._cfg:
            return None
        return self._cfg[key]

    def save(self):
        with open('smconfig.json', 'w') as cfg_file:
            json.dump(self._cfg, cfg_file)

    def set_value(self, key, value):
        self._cfg[key] = value

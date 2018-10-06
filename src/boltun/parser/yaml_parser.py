import io

import yaml
from path import Path
from yaml_tags import tag_registry

class YamlParser(object):

    def __init__(self):
        super(YamlParser, self).__init__()
        tag_registry.require()

    def parse(self, input_path):
        input_path = Path(input_path)

        if not input_path.isabs():
            input_path = input_path.abspath()

        with io.open(input_path, mode='r', encoding='utf-8') as fh:
            yaml_data = yaml.load(fh)
            print(yaml.dump(yaml_data, indent=2))

        return input_path

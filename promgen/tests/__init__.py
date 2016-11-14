import json
import os
import yaml

with open(os.path.join(os.path.dirname(__file__), 'examples', 'alertmanager.json')) as fp:
    TEST_ALERT = json.load(fp)

with open(os.path.join(os.path.dirname(__file__), 'examples', 'import.json')) as fp:
    TEST_IMPORT = json.load(fp)

with open(os.path.join(os.path.dirname(__file__), 'examples', 'settings.yaml')) as fp:
    TEST_SETTINGS = yaml.load(fp)

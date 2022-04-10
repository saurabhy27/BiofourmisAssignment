import yaml
import os


def fetch_constant(constant_name, file_name="constants.yaml"):
    file_path = os.path.abspath(os.path.join(__file__, '../../resources/' + str(file_name)))
    with open(file_path, 'r') as f:
        doc = yaml.safe_load(f)
    return doc[constant_name]

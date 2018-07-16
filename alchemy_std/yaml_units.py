
def load_yaml_file(filepath):
    import yaml
    with open(filepath) as f:
        data = yaml.load(f)

    return {'yaml_data': data}

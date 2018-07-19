
def load_yaml_file(filepath, dryrun=False):
    import yaml

    if dryrun:
        return {'yaml_data': None}

    with open(filepath) as f:
        data = yaml.load(f)

    return {'yaml_data': data}


# Both JSON and YAML aim to be human readable data interchange formats.

# JSON’s foremost design goal is simplicity and universality.
# Thus, JSON is trivial to generate and parse, at the cost of reduced human readability.

# In contrast, YAML’s foremost design goals are human readability,
# but is more complex to generate and parse.

# https://en.wikipedia.org/wiki/YAML
# https://yaml.org/spec/1.2/spec.html

# PyYaml package
# https://pyyaml.org/wiki/PyYAMLDocumentation


import yaml

with open('./config.yaml') as config_file:
    config = yaml.load(config_file)
    print(config)

new_config = {
    'tree_root':
        {'branch1':
             {'branch1-1':
                  {'name': 'Node 1-1'},
              'name': 'Node 1'},
         'branch2':
            {'branch2-1':
                 {'name': 'Node 2-1'},
              'name': 'Node 2'}
         }
}

with open('./new_config.yaml', 'w') as new_config_file:
    yaml.dump(new_config, new_config_file)

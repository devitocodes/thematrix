import json

with open('../thematrix/thematrix.json', 'r') as f:
    data = json.load(f)

runners = data['runners'].keys()

output = {"include": [{"runner": i} for i in runners]}

with open('runners.json', 'w') as f:
    json.dump(output, f, indent=4)

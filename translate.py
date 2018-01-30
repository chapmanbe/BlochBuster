import os
import json
import yaml
import glob

for f in glob.glob(os.path.join("config","*.json")):
    name, suffix = os.path.splitext(f)
    print(name)
    with open(f) as f0:
        data = json.load(f0)
    with open(name+".yaml", "w") as f0:
        yaml.dump(data,f0)


import json
from pprint import pprint

with open('dataset/Demographic_Statistics_By_Zip_Code.json') as f:
    data = json.load(f)

"pprint(data)"
for key in data:
    value = data[key]
    print(value)

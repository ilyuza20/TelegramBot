import json

from deeppavlov import build_model, train_model, configs
from deeppavlov.core.common.file import read_json

#config = json.load(open(configs['intent_catcher']['intent_catcher']))
#print(f"Intents: {list(train_data.keys())}")
# print(train_data['about'])

model_config = read_json("intent_catcher.json")

model = train_model(model_config)

print(model(["phone number"]))


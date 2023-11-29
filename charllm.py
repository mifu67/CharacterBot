import torch
import torch.nn as nn
import torch.nn.functional as F
import json
import together
from apikey import TOG_KEY

EXPERIENCE_PATH = 'trainingdata/hansolo/young-han.json'
PROTECTED_PATH = 'trainingdata/hansolo/young-han-protective.json'

together.api_key = TOG_KEY

model_list = together.Models.list()

print(f"{len(model_list)} models available")

# print the first 10 models on the menu
model_names = [model_dict['name'] for model_dict in model_list]
print(model_names[:10])
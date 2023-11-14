import together
from apikey import KEY

together.api_key = KEY

resp = together.Finetune.create(
  training_file = 'file-bb280f38-2b64-42a9-9349-6e7eb2ad2d05',
  model = 'togethercomputer/llama-2-70b-chat',
  n_epochs = 3,
  n_checkpoints = 1,
  batch_size = 4,
  learning_rate = 1e-5,
  suffix = 'my-demo-finetune',
  wandb_api_key = KEY,
)

fine_tune_id = resp['id']
print(resp)
# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests

model_inputs = {'prompt': 'Hello I am a [MASK] model.'}

res = requests.post('http://127.0. 0.1:8000/', json = model_inputs)

print(res.json())

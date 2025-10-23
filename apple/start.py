import json
from edutap.wallet_apple import api

from dotenv import load_dotenv

load_dotenv()

with open("apple/test.json", 'r') as file:
  jsonData = json.load(file)

  jsonStr = json.dumps(jsonData)

  # print(json.dumps(jsonStr))


pkPassModel = api.new(
  data = jsonData
)

print(pkPassModel)



# api.sign(
#   pkPassModel
# )


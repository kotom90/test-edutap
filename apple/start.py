import json
from pathlib import Path
from edutap.wallet_apple import api, settings

with open("apple/test.json", 'r') as file:
  jsonData = json.load(file)

  jsonStr = json.dumps(jsonData)
  # print(json.dumps(jsonStr))


pkPassModel = api.new(
  data = jsonData
)

# print(pkPassModel)

root_path = Path("apple").resolve()

""" certificates must be provided on the "certs" folder
https://developer.apple.com/documentation/walletpasses/building-a-pass
key pswd = trinitySystems3
...
"""

settings = settings.Settings(
  root_dir = root_path,
  fernet_key="WV1aSC2TgErgOeoMG6rup3jqWy2kLTGIbjC87VLl-MM="
)

api.sign(
  pkPassModel,
  settings
)

print(pkPassModel.is_signed)

link = api.save_link(
  pass_type_id="com.example.mypass",
  serial_number="pass01",
  settings = settings
)

print(link)

from edutap.wallet_google import api
from edutap.wallet_google.models.passes.generic import GenericObject
from edutap.wallet_google.models.datatypes.message import Message, MessageType
from dotenv import load_dotenv
import os

load_dotenv()

# Suppose obj is your previously created GenericObject
# or just use the object ID

object_id = f"{os.environ.get('EDUTAP_WALLET_GOOGLE_ISSUER_ID')}.example_object06.edutap_example"

# You can get the object model from the API if needed
obj = api.read("GenericObject", object_id)

obj.subheader.defaultValue.value = "change5"
obj.header.defaultValue.value = "change6"

#api.update(obj, partial=True)

#msg = Message(body="well done 2", messageType=MessageType.TEXT_AND_NOTIFY)
#api.message("GenericObject", object_id, msg)

# Generate the save link
save_url = api.save_link([obj], origins=["https://example.com"])
save_url_api = f"https://pay.google.com/gp/v/save/{object_id}"

print("Save to Google Wallet link JWT:", save_url)
print("Save to Google Wallet link API:", save_url_api)

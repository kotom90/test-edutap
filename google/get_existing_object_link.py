from edutap.wallet_google import api
from edutap.wallet_google.models.passes.generic import GenericObject
from edutap.wallet_google.models.datatypes.message import Message, MessageType
from edutap.wallet_google.models.datatypes.enums import State
from dotenv import load_dotenv
import os

load_dotenv()

# Suppose obj is your previously created GenericObject
# or just use the object ID

object_id = f"{os.environ.get('EDUTAP_WALLET_GOOGLE_ISSUER_ID')}.example_object08.edutap_example"

# You can get the object model from the API if needed
obj = api.read("GenericObject", object_id)


# Update pass example
obj.subheader.defaultValue.value = "Your pass is expired!"
obj.state = State.EXPIRED

api.update(obj, partial=True)

#msg = Message(body="well done 2", messageType=MessageType.TEXT_AND_NOTIFY)
#api.message("GenericObject", object_id, msg)

# Generate the save link
save_url = api.save_link([obj], origins=["https://example.com"])

print("Save to Google Wallet link JWT:", save_url)

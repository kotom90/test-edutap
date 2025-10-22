from edutap.wallet_google import api
from dotenv import load_dotenv

import os

load_dotenv()
# if you run the code more than once, you need to change the ID of the class,
# like by incrementing the number part.
class_id = f"{os.environ.get('EDUTAP_WALLET_GOOGLE_ISSUER_ID')}.example_class01.edutap_example"

class_model = api.new("GenericClass",{
        "id": class_id,
    },
)

new_class = api.create(class_model)
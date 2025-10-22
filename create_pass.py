from edutap.wallet_google import api
from dotenv import load_dotenv
from datetime import datetime, timezone

import os

load_dotenv()
# if you run the code more than once, you need to change the ID of the class,
# like by incrementing the number part.
class_id = f"{os.environ.get('EDUTAP_WALLET_GOOGLE_ISSUER_ID')}.example_class01.edutap_example"
object_id = f"{os.environ.get('EDUTAP_WALLET_GOOGLE_ISSUER_ID')}.example_object06.edutap_example"

obj = api.new("GenericObject",
    {
        'id': object_id,
        'classId': class_id,
        "logo": {
            "sourceUri": {
            "uri": "https://storage.googleapis.com/wallet-lab-tools-codelab-artifacts-public/pass_google_logo.jpg"
            },
            "contentDescription": {
            "defaultValue": {
                "language": "en-US",
                "value": "LOGO_IMAGE_DESCRIPTION"
                }
            }
        },
        "cardTitle": {
            "defaultValue": {
            "language": "el-GR",
            "value": "ΕΚΠΑΙΔΕΥΤΗΡΙΑ ΜΑΝΤΟΥΛΙΔΗ"
            }
        },
        "subheader": {
            "defaultValue": {
            "language": "en-US",
            "value": "Subheader text"
            }
        },
        "header": {
            "defaultValue": {
            "language": "el-GR",
            "value": "ΣΙΔΗΡΟΠΟΥΛΟΣ Κωνσταντίνος"
            }
        },
        "textModulesData": [
            {
            "id": "test",
            "header": "test",
            "body": "9999"
            },
            {
            "id": "test1",
            "header": "test1",
            "body": "8888"
            }
        ],
        "barcode": {
            "type": "QR_CODE",
            "value": "3c617fac-58b5-4703-b2e1-429d61e08974",
            "alternateText": ""
        },
        "validTimeInterval": {
            "end": {
                "date": datetime(2024, 10, 15, 13, 15).isoformat()
            }
            
        },
        "hexBackgroundColor": "#4285f4",
        "heroImage": {
            "sourceUri": {
            "uri": "https://storage.googleapis.com/wallet-lab-tools-codelab-artifacts-public/google-io-hero-demo-only.png"
            },
            "contentDescription": {
            "defaultValue": {
                "language": "en-US",
                "value": "HERO_IMAGE_DESCRIPTION"
                }
            }
        }
    },
)


#api.create(obj)

print(
    api.save_link(
        [obj],
        origins=["www.example.com"],
    )
)
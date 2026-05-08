#!/usr/bin/env python3
"""
ANKR Business Yard – WhatsApp Carousel Template (8 cards)
May 2026 Newsletter Edition

STEP 1: Run img_upload_ankr.py  → get 8 'h' handles
STEP 2: Paste handles into MEDIA_HANDLES below
STEP 3: Run this script
"""
import requests
import json

# ─────────────────────────────────────────────
#  CREDENTIALS
# ─────────────────────────────────────────────
ACCESS_TOKEN = "EAAUZCFPxpY38BP7aBXFvlYvmZBaZAdIsvwehDOZCG2ZBEZAsW1ui4AIP34VL6S3D9zCIgoMXnSemzZA6KZArgZBhFOQ9NXhfRBdoYMIpoVLgz8GvePJuSv6Ecoag1YPCmQM2o8vstqsZB0vFNeUaWQrS9fnRtgLPMDHZBTJx7gPxuZARsgmqeR0v7zNd8zAZCqtFn7gZDZD"
WABA_ID      = "1967270603816020"
APP_ID       = "1476734250214271"

# ─────────────────────────────────────────────
#  BUTTON URLS
# ─────────────────────────────────────────────
LEARN_MORE_URL = "https://ankrdevelopment.com/page/properties/28"
BROCHURE_URL   = "https://drive.google.com/uc?export=download&id=1mCoDzk1xGr7u4nh-TYKTEnAqQGgaeQ2h"

# ─────────────────────────────────────────────
#  MEDIA HANDLES  ← paste 'h' values from img_upload_ankr.py here
#  These are long strings starting with "4:" produced by the
#  Resumable Upload API — NOT the numeric media IDs
# ─────────────────────────────────────────────
MEDIA_HANDLES = [
    "4::aW1hZ2UvcG5n:ARbLxSjBoFjlw-y9nYWrRUKD_vwq-bwOJe7euz4Tqzk2LKj3fdTlBueiy_bMy4xAg9r3W--E3HceQ0oP93XttCLrE20sw9xrqREawiDWk1NO5w:e:1777705055:1476734250214271:61578366272363:ARaJFMLuvxoLdv-3qcM",   # Card 1 – ANKR.png
    "4::aW1hZ2UvanBlZw==:ARbEhc2XAn4PQ7cAiscs3Rz-NfVzouZcQoTUFSoGXzxQeX3iV-xwzwvbtZ5MzY_hEvs3WCDS4zSuccnFB338fM97DIrcBjOxxfNsFM0MAGHYYA:e:1777705056:1476734250214271:61578366272363:ARY0OeU5-fZtBXlMdGU",   # Card 2 – ANKR9900.jpg
    "4::aW1hZ2UvanBlZw==:ARZQOBDKyjbz5468kUPTOw213zldLkbaABVg16mwtc1cdxCtZ102U_fPLmRywGX1eaPujN7I9K4W5yppyiOeaIQfi21RubIPKa2cpTycvNmsYQ:e:1777705057:1476734250214271:61578366272363:ARag3WzRfZPWTEeh538",   # Card 3 – ANKR9901.jpg
    "4::aW1hZ2UvanBlZw==:ARYnWehZr8LwVuVet0N0TZR_zvT8fTn-_hRo3voPcQ58DREqcEu6VzVaLe8DGnibTj55sAmJKmiAnAgblWecF08CIlgFtF3Nvpzb2jbi2k0llw:e:1777705057:1476734250214271:61578366272363:ARYNoVFdHb5s5Rf2GlU",   # Card 4 – ANKRBusinessYard1.jpg
    "4::aW1hZ2UvanBlZw==:ARa4eFtUFcws4F485RG91Lf8BCQP38x3oi-WZqRH36DaIaxNOcKOct5pnMnw_xzZD9jR4xGFX8WcPn61-AjHdy8jUUA3wDAivKrYeheFwYPxzw:e:1777705058:1476734250214271:61578366272363:ARZ0IJc9GOHDEvC1sTs",   # Card 5 – ANKRBusinessYard2.jpg
    "4::aW1hZ2UvcG5n:ARaPWj3k6M2pDynPXFrgOeFqkOVcQ40oV53fDYwjFsMQAY4U5LRXopKWsMjLU7WphmjBXUy1ZRs48V585KiytHOOZ_90L3qZMDxkON08iUpPwQ:e:1777705059:1476734250214271:61578366272363:ARYr_r4CpXt5wR9XIxA",   # Card 6 – UnderConstruction1.png
    "4::aW1hZ2UvcG5n:ARaXTLuZy6ICuLlxlHfG9p4KUemT7KULZAB9_4_xbiFRD5fHbF7rTxHUudaY4plqcs9jdIJaJMYW4Zl8YBG9p60TfaXkwhIVKUpxex3EyalKnA:e:1777705060:1476734250214271:61578366272363:ARZ9aZnZkXAJiG5AkZE",   # Card 7 – UnderConstruction2.png
    "4::aW1hZ2UvcG5n:ARYsPV85e0lC2wpOvVorXK_86Tal4xMekh0a0tdgqxMuZd2Gv4vEQDnuPDXhT0F2fiIlvSO-z_HI9-We5mWboTzY9xNIETkpWZHxHW650dEeow:e:1777705060:1476734250214271:61578366272363:ARZXNMXxWCHg-sFesyU",   # Card 8 – UnderConstruction3.png
]

# ─────────────────────────────────────────────
#  CARD BODY TEXTS  (max 160 chars, no line breaks)
# ─────────────────────────────────────────────
card_bodies = [
    "Welcome to ANKR Business Yard — a landmark commercial address in the heart of Hazmieh. Delivery: December 2026.",
    "Strategically located in Hazmieh, ANKR Business Yard is designed to set your business up for success from day one.",
    "Premium offices with flexible layouts — occupy a full floor or combine units to create a custom headquarters.",
    "Spacious showrooms with high ceilings and wide frontages. The perfect stage to showcase your brand.",
    "More than a building — ANKR Business Yard is a thriving business community. Set your ANKR where it matters.",
    "Construction update May 2026: structural work progressing on schedule. On track for December 2026 delivery.",
    "Phase 2 underway at ANKR Business Yard. Facades and interior fit-out beginning soon. Your office is taking shape.",
    "Only select units remain at ANKR Business Yard. Don't miss your chance — contact us today.",
]

# ─────────────────────────────────────────────
#  VALIDATION
# ─────────────────────────────────────────────
if any("PASTE_HANDLE" in h for h in MEDIA_HANDLES):
    print("❌  Please paste the 'h' handles from img_upload_ankr.py into MEDIA_HANDLES first.")
    raise SystemExit(1)

assert len(MEDIA_HANDLES) == len(card_bodies) == 8

for i, body in enumerate(card_bodies, 1):
    if len(body) > 160:
        raise ValueError(f"Card {i} body is {len(body)} chars — max is 160.")

# ─────────────────────────────────────────────
#  BUILD CAROUSEL CARDS
# ─────────────────────────────────────────────
def make_card(handle, body_text):
    return {
        "components": [
            {
                "type":   "header",
                "format": "image",
                "example": {"header_handle": [handle]},
            },
            {
                "type": "body",
                "text": body_text,
            },
            {
                "type": "buttons",
                "buttons": [
                    {
                        "type": "url",
                        "text": "See Available Units",
                        "url":  LEARN_MORE_URL,
                    },
                    {
                        "type": "url",
                        "text": "Download Brochure",
                        "url":  BROCHURE_URL,
                    },
                ],
            },
        ]
    }

carousel_cards = [make_card(h, body) for h, body in zip(MEDIA_HANDLES, card_bodies)]

# ─────────────────────────────────────────────
#  FULL TEMPLATE PAYLOAD
# ─────────────────────────────────────────────
template_data = {
    "name":     "ankr_business_yard_may2026",
    "language": "en_US",
    "category": "marketing",
    "components": [
        {
            "type": "body",
            "text": (
                "ANKR Business Yard \U0001f3e2 \u2014 May 2026 Newsletter\n\n"
                "We\u2019re proud to feature our only commercial center currently under construction in Hazmieh, "
                "on track for delivery in December 2026.\n\n"
                "Explore available units and set your ANKR where it matters."
            ),
        },
        {
            "type":  "carousel",
            "cards": carousel_cards,
        },
    ],
}

# ─────────────────────────────────────────────
#  SUBMIT
# ─────────────────────────────────────────────
print("=" * 65)
print("   ANKR Business Yard \u2013 Carousel Template Submission")
print("=" * 65)
print(f"\n  Template : {template_data['name']}")
print(f"  WABA ID  : {WABA_ID}")
print(f"  Cards    : {len(carousel_cards)}")
print(f"  Buttons  : [1] See Available Units \u2192 {LEARN_MORE_URL}")
print(f"             [2] Download Brochure \u2192 {BROCHURE_URL}")
print("\nSubmitting...\n")

response = requests.post(
    f"https://graph.facebook.com/v21.0/{WABA_ID}/message_templates",
    headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type":  "application/json",
    },
    json=template_data,
)

print("=" * 65)
if response.status_code == 200:
    result = response.json()
    print("\U0001f389  SUCCESS \u2014 Carousel template created!")
    print("=" * 65)
    print(f"  Template ID : {result.get('id')}")
    print(f"  Name        : {template_data['name']}")
    print(f"  Status      : {result.get('status', 'PENDING')}")
    print(f"  Language    : en_US  |  Category: MARKETING")
    print("=" * 65)

    print("\n\U0001f4cb Cards submitted:")
    labels = [
        "Card 1 \u2013 Brand Hero          (ANKR.png)",
        "Card 2 \u2013 Exterior / Location  (ANKR9900.jpg)",
        "Card 3 \u2013 Premium Offices      (ANKR9901.jpg)",
        "Card 4 \u2013 Showrooms            (ANKRBusinessYard1.jpg)",
        "Card 5 \u2013 Business Community   (ANKRBusinessYard2.jpg)",
        "Card 6 \u2013 Construction Prog. 1 (UnderConstruction1.png)",
        "Card 7 \u2013 Construction Prog. 2 (UnderConstruction2.png)",
        "Card 8 \u2013 Call to Action       (UnderConstruction3.png)",
    ]
    for label in labels:
        print(f"  \u2022 {label}")

    print(f"\n\u23f3 Pending WhatsApp approval (usually 5 min \u2013 24 hours).")
    print(f"\n\U0001f517 Check status:")
    print(f"   https://business.facebook.com/wa/manage/message-templates/?waba_id={WABA_ID}")

else:
    print("\u274c  ERROR")
    print(f"\n  HTTP Status : {response.status_code}")
    error_data = response.json()

    if "error" in error_data:
        err = error_data["error"]
        print(f"  Message     : {err.get('message')}")
        print(f"  Type        : {err.get('type')}")
        print(f"  Code        : {err.get('code')}")
        print(f"  Subcode     : {err.get('error_subcode')}")
        if "error_user_msg" in err:
            print(f"  Details     : {err['error_user_msg']}")

    print("\n[DEBUG] Full response:")
    print(json.dumps(error_data, indent=2))

print("=" * 65)

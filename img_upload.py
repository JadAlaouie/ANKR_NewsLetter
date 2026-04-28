#!/usr/bin/env python3
"""
ANKR Business Yard – Image Upload via Resumable Upload API
This produces 'h' handles required by the carousel template API.
Run this first, then paste the handles into carousel_creation_ankr.py
"""
import requests
import os
import json
import time

# ─────────────────────────────────────────────
#  CREDENTIALS
# ─────────────────────────────────────────────
ACCESS_TOKEN = "EAAUZCFPxpY38BP7aBXFvlYvmZBaZAdIsvwehDOZCG2ZBEZAsW1ui4AIP34VL6S3D9zCIgoMXnSemzZA6KZArgZBhFOQ9NXhfRBdoYMIpoVLgz8GvePJuSv6Ecoag1YPCmQM2o8vstqsZB0vFNeUaWQrS9fnRtgLPMDHZBTJx7gPxuZARsgmqeR0v7zNd8zAZCqtFn7gZDZD"
APP_ID       = "1476734250214271"

# ─────────────────────────────────────────────
#  IMAGE PATHS  (8 cards, in order)
# ─────────────────────────────────────────────
BASE_DIR = r"C:\Users\Jad Alaouie\Desktop\Carousel ANKR"

image_paths = [
    os.path.join(BASE_DIR, "ANKR.png"),
    os.path.join(BASE_DIR, "ANKR9900.jpg"),
    os.path.join(BASE_DIR, "ANKR9901.jpg"),
    os.path.join(BASE_DIR, "ANKRBusinessYard1.jpg"),
    os.path.join(BASE_DIR, "ANKRBusinessYard2.jpg"),
    os.path.join(BASE_DIR, "UnderConstruction1.png"),
    os.path.join(BASE_DIR, "UnderConstruction2.png"),
    os.path.join(BASE_DIR, "UnderConstruction3.png"),
]

card_labels = [
    "ANKR.png           → Card 1",
    "ANKR9900.jpg       → Card 2",
    "ANKR9901.jpg       → Card 3",
    "ANKRBusinessYard1  → Card 4",
    "ANKRBusinessYard2  → Card 5",
    "UnderConstruction1 → Card 6",
    "UnderConstruction2 → Card 7",
    "UnderConstruction3 → Card 8",
]

# ─────────────────────────────────────────────
#  UPLOAD  (Resumable Upload API → returns 'h' handles)
# ─────────────────────────────────────────────
print("=" * 65)
print("   ANKR Business Yard – Resumable Image Upload (8 cards)")
print("=" * 65)

handles = []

for idx, image_path in enumerate(image_paths, 1):
    filename = os.path.basename(image_path)
    ext      = os.path.splitext(filename)[1].lower()
    mime     = "image/png" if ext == ".png" else "image/jpeg"
    size     = os.path.getsize(image_path)

    print(f"\n[{idx}/8]  {filename}  ({size:,} bytes)")

    if not os.path.exists(image_path):
        print(f"  ✗  File not found: {image_path}")
        raise SystemExit(1)

    # Step 1 – Create upload session
    print("  [1/2] Creating upload session...")
    session_resp = requests.post(
        f"https://graph.facebook.com/v21.0/{APP_ID}/uploads",
        params={
            "file_length": size,
            "file_type":   mime,
            "access_token": ACCESS_TOKEN,
        },
    )
    session_data = session_resp.json()

    if session_resp.status_code != 200 or "id" not in session_data:
        print(f"  ✗  Session error: {json.dumps(session_data, indent=2)}")
        raise SystemExit(1)

    upload_session_id = session_data["id"]
    print(f"  ✓  Session: {upload_session_id}")

    # Step 2 – Upload file bytes
    print("  [2/2] Uploading file...")
    with open(image_path, "rb") as f:
        file_data = f.read()

    upload_resp = requests.post(
        f"https://graph.facebook.com/v21.0/{upload_session_id}",
        headers={
            "Authorization": f"OAuth {ACCESS_TOKEN}",
            "file_offset":   "0",
        },
        data=file_data,
    )
    upload_data = upload_resp.json()

    if upload_resp.status_code != 200 or "h" not in upload_data:
        print(f"  ✗  Upload error: {json.dumps(upload_data, indent=2)}")
        raise SystemExit(1)

    handle = upload_data["h"]
    handles.append(handle)
    print(f"  ✓  Handle: {handle[:60]}{'...' if len(handle) > 60 else ''}")

print("\nWaiting 3 seconds for processing...")
time.sleep(3)

# ─────────────────────────────────────────────
#  SUMMARY – paste these into carousel_creation_ankr.py
# ─────────────────────────────────────────────
print("\n" + "=" * 65)
print("  ✓  All 8 images uploaded!")
print("  Copy the handles below into carousel_creation_ankr.py")
print("  → replace the MEDIA_HANDLES list")
print("=" * 65)
for label, handle in zip(card_labels, handles):
    print(f"  {label}:")
    print(f"    \"{handle}\",")
print("=" * 65)
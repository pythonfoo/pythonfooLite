from hashlib import md5
from base64 import b64encode
from pathlib import Path
import requests

def get(email):
    try:
        return {"status": "ok", "url": get_image(email)}
    except Exception as exc:
        return {"status": "error", "error": str(exc)}

def get_image(email):
    print(f"get_image({email})")
    if "@" not in email:
        raise ValueError("E-Mail-Adresse ist ungültig.")
    mail_hash = md5(email.strip().encode()).hexdigest()
    url = "https://www.gravatar.com/avatar/" + mail_hash
    # return url
    try:
        image = requests.get(url).content
    except requests.exceptions.ConnectionError as exc:
        image = Path("fallback.jpg").read_bytes()
        # raise
    # QML erwartet eine URL - wir haben aber das Bild als Bytes.
    # data-URIs lösen das Problem.
    return "data:image/jpeg;base64," + b64encode(image).decode()

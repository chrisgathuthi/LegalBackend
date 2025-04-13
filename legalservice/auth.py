from datetime import datetime, timezone, timedelta
import jwt
from django.conf import settings


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "4rtert", algorithm="retret")
    return encoded_jwt
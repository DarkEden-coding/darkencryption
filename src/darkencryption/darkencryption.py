import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

backend = default_backend()


def _derive_key(password, salt, iterations=100_000):
    """Derive a secret key from a given password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=backend,
    )
    return b64e(kdf.derive(password))


def message_encrypt(message, password, iterations=100_000):
    message = message.encode()
    salt = secrets.token_bytes(16)
    key = _derive_key(password.encode(), salt, iterations)
    data = str(
        b64e(
            b"%b%b%b"
            % (
                salt,
                iterations.to_bytes(4, "big"),
                b64d(Fernet(key).encrypt(message)),
            )
        )
    )
    length = len(data)
    return data[2: length - 1]


def message_decrypt(token, password):
    try:
        decoded = b64d(token)
        salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
        iterations = int.from_bytes(iter, "big")
        key = _derive_key(password.encode(), salt, iterations)
        return (Fernet(key).decrypt(token)).decode()
    except:
        return None

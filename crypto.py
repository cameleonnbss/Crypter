import base64
import hashlib
import secrets


def build_stream(key, salt, length):
    stream = b""

    seed = hashlib.sha256(
        key.encode() + salt
    ).digest()

    while len(stream) < length:
        seed = hashlib.sha256(seed).digest()
        stream += seed

    return stream[:length]


def xor_encrypt(data, key):
    raw = data.encode()
    key_bytes = key.encode()

    out = bytearray()

    for i in range(len(raw)):
        out.append(
            raw[i] ^ key_bytes[i % len(key_bytes)]
        )

    return base64.b64encode(out).decode()


def xor_decrypt(data, key):
    raw = base64.b64decode(data)
    key_bytes = key.encode()

    out = bytearray()

    for i in range(len(raw)):
        out.append(
            raw[i] ^ key_bytes[i % len(key_bytes)]
        )

    return out.decode()


def stream_encrypt(data, key):
    raw = data.encode()

    salt = secrets.token_bytes(16)

    stream = build_stream(
        key,
        salt,
        len(raw)
    )

    out = bytearray()

    for i in range(len(raw)):
        out.append(
            raw[i] ^ stream[i]
        )

    final = salt + out

    return base64.b64encode(final).decode()


def stream_decrypt(data, key):
    raw = base64.b64decode(data)

    salt = raw[:16]
    encrypted = raw[16:]

    stream = build_stream(
        key,
        salt,
        len(encrypted)
    )

    out = bytearray()

    for i in range(len(encrypted)):
        out.append(
            encrypted[i] ^ stream[i]
        )

    return out.decode()


def double_encrypt(data, key):
    first = xor_encrypt(data, key)
    return stream_encrypt(first, key)


def double_decrypt(data, key):
    first = stream_decrypt(data, key)
    return xor_decrypt(first, key)

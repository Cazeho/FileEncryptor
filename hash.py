import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def hsh(s):
    h = 7
    letters = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN/+1234567890"
    for i, val in enumerate(s):
        h = (h * random.randint(1, 39) + letters.index(s[i]))
    return h

a='MIIBCgKCAQEAxnRNYA0jYgUluPv5OImzqnW0Ni2kEInHXb7j5lkZbK9gK9svuah9WRi8fVjQTnJ+62xplrdzCex1J+y/K2YtxDPRmrst7s7l0q/FEKwswEYofOiKW4hAn4GIAHEghYa3gOzIJuwpWkop8Ke75RVrc2pSuHHDV1XrHBDFYCbK7N4LBBQv+js9aMgd4B8AR2l0rMobvPPkRLAZx4yBxyBHyZG+heCCmXEOJuh+tsoD4x2l9PlM5Lt9E4BajNlJQhUqO+dSyapnmcCp90RIMPBb6OS87mTAJoBumGvRT0q1dsxPhR3/D5AD7oRs9sIgnO2N8usOT1eH9mHcBmoNiXn99wIDAQAB'
print(hsh(a))
print(len(str(hsh(a))))
print(len(a))

password_provided = str(hsh(a))
password = password_provided.encode()
salt=b'{OA\x1f\xc8\xc0\xdc\x9a\x012\x99c\xb7?Rn'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)



key = base64.urlsafe_b64encode(kdf.derive(password))
print(str(key))

from ecdsa import SigningKey,NIST192p,NIST224p,NIST256p,NIST384p,NIST521p,SECP256k1,VerifyingKey
import base64
import hashlib, secrets
import sys

msg=""
type = 1
cur=SECP256k1


sk = SigningKey.generate(curve=cur) 

vk = sk.get_verifying_key()

signature = (sk.sign(msg.encode()))

print("Message:\t",msg)
print("Type:\t\t",cur.name)
print("=========================")

print("Signature:\t",hashlib.md5(base64.b64encode(signature)).hexdigest())

a=hashlib.md5(base64.b64encode(signature)).hexdigest()
print("=========================")
print(a.encode('utf-8'))
print("Signatures match:\t",vk.verify(a.encode('utf-8'), msg.encode()))
print("pubnat",vk.to_string().hex())
print("pub:",vk.to_string("compressed").hex())
key=vk.to_string("compressed").hex()
k = VerifyingKey.from_string(bytes.fromhex(key), curve=SECP256k1)
pub_key = k.to_string('uncompressed').hex()
print("uncompressd",pub_key)
print("priv:",sk.to_string().hex())

from cryptography.fernet import Fernet
from basehash import *
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives.asymmetric import rsa  
from cryptography.hazmat.primitives import serialization 
from Crypto.PublicKey import RSA
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding







  

# Generate an RSA Keys  
private_key = rsa.generate_private_key(  
        public_exponent=65537,  
        key_size=2048,  
        backend=default_backend()  
    )  
  
public_key = private_key.public_key()
print('------------------------')
#print(public_key)
print(private_key)



encryptedpass = "myverystrongpassword"  
key = RSA.generate(2048)  
privKey = key.exportKey(passphrase=encryptedpass)#.decode("utf-8") 
pubKey = key.publickey().exportKey()#.decode("utf-8").replace('-----BEGIN PUBLIC KEY-----', '').replace('-----END PUBLIC KEY-----','')
#print(str(privKey))
print('------------')
#print(str(pubKey))
#print(len(pubKey))



password_provided = input('enter password')
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
print(len(key))


message= key
##################### encrypt RSA
encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
)

print((encrypted))



#################decypt RSA





###############################






#message="aaaaaaaaaaaa"
#encoded=message.encode()
#print(encoded)

f= Fernet(key)

#encrypted=f.encrypt(encoded)
#with open('text.e.txt', 'wb') as f:
#    f.write(encrypted)
#    f.close()


#file= open('text.e.txt','rb')
#me=file.read()
#file.close()




#decrypted=f.decrypt(me)

#print(decrypted)

######################

file= open('4G.e.pdf','rb')
me=file.read()
file.close()

decrypted=f.decrypt(me)


with open('4G.d.pdf', 'wb') as f:
    f.write(decrypted)
    f.close()


######################"
def save_key_pub(pk, filename):
    pem = pk.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
    )
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)


pk= public_key
filename="pubkey.pem"
save_key_pub(pk, filename)



def save_key_priv(pk, filename):
    pem = pk.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)
        
pk= private_key
filename="privkey.pem"
save_key_priv(pk, filename)



def load_key_priv(filename):
    with open(filename, 'rb') as pem_in:
        pemlines = pem_in.read()
    private_key = load_pem_private_key(pemlines, None, default_backend())
    print(private_key)
    g=private_key
    #######
    return g


filename="privkey.pem"
a=load_key_priv(filename)
print(a)


###############""test

original_message = a.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
)



print(original_message)

from config.config import Config
from config.config import Config
from util.cipher import Cipher

config = Config()

cipher = Cipher(config.get_generator())
# 'hello' ecrypted with Solitaire
hello = cipher.encrypt(b'hello')
print(hello)
print(cipher.decrypt(hello, 0))

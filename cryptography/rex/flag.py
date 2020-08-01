import base64
import binascii

c = "37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067"

L = list(bytearray(binascii.unhexlify(c)))

b64 = "Z"

for i in L:
	b64+=(chr(i^ord(b64[-1])))

print(base64.b64decode(b64[:-1]))
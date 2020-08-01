from pwn import *
import hashlib
import re
p = remote("jh2i.com", 50005)
type = 0
while True :
	que = p.recvline().decode()
	print(que)
	hash = re.findall(r"[0-9a-f]{3,}",que)[0]
	print("hash is ",hash)
	l = len(hash)
	if "md5sum" in que:
		val = -1
		ans = -1
		while ans != hash:
			val += 1
			ans = hashlib.md5(str(val).encode()).hexdigest()[:l]
			#print("\r{}".format(ans))
		p.sendline(str(val))
		res = p.recvline()
		print(res)
	else:
		ans = -1
		val = -1
		while  ans != hash:
			val += 1
			ans = hashlib.sha1(str(val).encode()).hexdigest()[:l]
			#print("\r{}".format(ans))
		p.sendline(str(val))
		res = p.recvline()
		print(res)
p.interactive()
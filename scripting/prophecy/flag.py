from pwn import *
import time

timer = 2
futurenos = ['99126', '76106', '32378', '49560', '87935', '17366', '36639', '33561']

while(True):
	conn = remote("jh2i.com", 50012)
	time.sleep(timer)

	print(conn.recvS())

	for nos in futurenos:
		conn.send(nos)
		time.sleep(timer)
		print(nos)

	conn.send("0")
	time.sleep(timer)
	rcd = conn.recvS()
	if("F A I L U R E" in rcd):
		futurenos.append(rcd.split()[-1])
	else:
		print(rcd)
		break
	print(futurenos)

print(futurenos)
print(len(futurenos))
conn.interactive()


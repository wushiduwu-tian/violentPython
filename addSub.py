#! /bin/python3 

import socket 
s = socket.socket()
s.connect(("ad.samsclass.info", 10204))
  
for i in range(5):
	response = s.recv(1024).decode()
	print(response)
	colon = response.find(":")
	numbers = response[colon + 2:]
	if numbers[1].isnumeric(): 
		num1 = numbers[0:2]
		if numbers[4].isnumeric():
			num2 = numbers[3:5]
		else: 
			num2 = numbers[3]
	else: 
		num1 = numbers[0]
		if numbers[3].isnumeric():
			num2 = numbers[2:4]
		else: 
			num2 = numbers[2]

	print("Num 1: {}".format(num1))
	print("Num 2: {}".format(num2))
	if response[0:3] == "Add":
		answer = int(num1) + int(num2)
	else: 
		answer = int(num1) - int(num2)
	print("Answer: {}".format(answer))
	answerStr = str(answer) 
	answerStr = answerStr.zfill(3) 
	s.send(answerStr.encode())
	print(s.recv(1024).decode())
	
s.close()

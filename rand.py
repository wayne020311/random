import random
r = random.randint(1,30)

while True :
	x = input("請輸入數字")
	x = int(x)
	if x == r :
		print('恭喜答對')
		break
	if x > r :
		print('比答案大')
	if x < r :
		print('比答案小')
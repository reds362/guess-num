import random
r =random.randint(1,100)

while True:
	num = input('請輸入一個數字來猜猜看')
	num = int(num)
	if num == r :
		print("bingo")
		break
	elif num > r :
		print('比答案大')
	else:
		print('比答案小')
	
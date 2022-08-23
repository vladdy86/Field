import time
seconds = time.time()

count = 1

flag = input('Press number to draw flag:\n1 - USA\n2 - Romania\n\n')

if flag == '1':
	print()
	while count < 5:
		time.sleep(0.5)
		print('************-------------')
		count += 1
		
	while count < 9:
		time.sleep(0.5)
		print('-------------------------')
		count += 1
		
if flag == '2':
	print()
	while count < 11:
		time.sleep(0.5)
		print('***********+++++++++++~~~~~~~~~~~')
		count += 1

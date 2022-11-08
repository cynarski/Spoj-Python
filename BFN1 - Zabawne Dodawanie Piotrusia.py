testy = int(input())
for i in range(testy):
	ilosc = 0
	number = str(input())
	if number == number[::-1]:
		print(number + ' ' + str(ilosc))
	else:
		while number != number[::-1]:
			ilosc += 1
			x = int(number)
			y = int(number[::-1])
			x += y
			number = str(x)
		print(number + ' ' + str(ilosc))
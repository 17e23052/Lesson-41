numbers = [0,1,1,2,3,5,8,13,21,34,55,89,134,223,357,580,937,1517,2454,3971]
str_numbers = []
for number in numbers:
  str_numbers.append(str(number))

data = ",".join(str_numbers)

file = open("numbers.csv", "w")
file.write(data)
file.close()
numbers = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181]
str_numbers = []
for number in numbers:
  str_numbers.append(str(number))

data = ",".join(str_numbers)

file = open("numbers.csv", "w")
file.write(data)
file.close()
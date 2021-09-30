print("What times table do you want to see?")
timestable = int(input())
numbers = [str(1*timestable),str(2*timestable),str(3*timestable),str(4*timestable),str(5*timestable),str(6*timestable),str(7*timestable),str(8*timestable),str(9*timestable),str(10*timestable),str(11*timestable),str(12*timestable)]
str_numbers = []
for number in numbers:
  str_numbers.append(str(number))

data = ",".join(numbers)

file = open("timestables.csv", "w")
file.write(data)
file.close()
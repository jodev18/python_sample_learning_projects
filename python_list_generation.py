
inval = input("Enter 2 digits separated by comma: ")

inputs = inval.split(",")

big_list = []

for x in range(int(inputs[0])):
    another_list = []
    for y in range(int(inputs[1])):
        another_list.append(x*y)

    big_list.append(another_list)

print(big_list)
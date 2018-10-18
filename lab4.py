#converting comma-separated values into a list

comma_input = input("Enter comma-separated values: ")
values = comma_input.split(",")
values.sort()
print(values)
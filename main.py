import pandas

list = [1, 2, 3]
new_list = [list[item - 1] + 1 for item in list]

print(new_list)
doubled = [item * 2 for item in range(1, 5)]
print(doubled)


names = ['alex', 'beth', 'caroline', 'dave', 'elanor', 'freddie']

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string) for string in list_of_strings]
result = [number for number in numbers if number % 2 == 0]
print(result)



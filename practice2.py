list2 = ['a', 'b', 'c']
zipped = zip(list2)

for i in zipped:
    print(i)

nested_list = [[1, 2, 3], [4, 5, 6]]

# flat_list = [item for sublist in nested_list for item in sublist]

flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(flat_list)

print(flat_list)


nested_list = [[1, 2, 3], [4, 5, 6]]

flat_list = []
for sublist in nested_list:
    flat_list.extend(sublist)

print(flat_list)

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

top_keys = [item[0] for item in sorted_dict[:3]]

print(top_keys)
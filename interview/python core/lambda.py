data = {
    "apple": 5,
    "banana": 2,
    "orange": 8,
    "grape": 4,
}

filtered_data = dict(filter(lambda item: item[1] > 3, data.items()))
print(filtered_data)
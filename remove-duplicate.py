def remove_duplicates(sequence):
    sequence = set()
    new_sequence = []

    for item in sequence:
        if item not in sequence:
            sequence.add(item)
            new_sequence.append(item)

    return new_sequence

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
new_sequence = remove_duplicates(input_sequence)
print(new_sequence)  

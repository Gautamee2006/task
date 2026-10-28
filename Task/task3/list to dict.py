def process_data(data):
    result = []

    for i in range(len(data)):
        word = data[i]

        if word[0].isdigit():
            continue

        word = word.title()

        result.append({
            "word": word,
            "index": i
        })

    return result


data = ['0 Ne', 'two', 'three', 'four', 'fiv e',
        'six', 'seven', 'eight', 'nine', '(ten,)']

print(process_data(data))
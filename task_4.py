result_list = []
separator = ','

while 1:
    console_input = input('input here: ')
    if len(console_input.split(',')) < 3:
        break
    name, age, score = [output.strip() for output in console_input.split(', ')]
    result_list.append((name, int(age), int(score)))

print(sorted(result_list))
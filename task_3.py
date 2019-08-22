result = 0
while 1:
    console_input = input('input here: ')
    if len(console_input) >= 3 and console_input[0] in ['D', 'W']:
        money = int(console_input.split(' ')[-1])
        result = result + money if console_input[0] == 'D' else result - money
    else:
        break

print(result)
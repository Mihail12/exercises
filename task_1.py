def find_numbers(a, b):
    return ', '.join([str(i) for i in range(a, b + 1) if i % 11 == 0 and i % 7 != 0])


if __name__ == '__main__':
    print(find_numbers(1000, 2500))

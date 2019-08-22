from collections import Counter

console_input = input('input here: ')

cnt = Counter()
for word in console_input.split(' '):
    cnt[word] += 1

for output in sorted(cnt):
    print('{}:{}'.format(output, cnt[output]))

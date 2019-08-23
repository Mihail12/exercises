hint = [
    ['t', 'c', 'k', 's', 'x', 'f', 'b', 'r', 'a', 'v', 'h', 'i', 'g', 'p', 'o'],
    ['t', 'c', 'l', 'u', 's', 'z', 'f', 'r', 'a', 'h', 'e', 'i', 'j', 'q', 'g'],
    ['w', 't', 'l', 'u', 'k', 's', 'n', 'f', 'm', 'a', 'v', 'h', 'i', 'g', 'p'],
    ['t', 'c', 'u', 's', 'z', 'm', 'r', 'a', 'y', 'v', 'h', 'e', 'q', 'g', 'p'],
    ['w', 'c', 'l', 'u', 's', 'f', 'b', 'm', 'y', 'v', 'h', 'i', 'q', 'g', 'o'],
    ['w', 't', 'c', 'k', 'f', 'b', 'm', 'r', 'h', 'e', 'i', 'j', 'q', 'g', 'o'],
    ['w', 't', 'c', 'u', 'k', 's', 'z', 'x', 'b', 'm', 'h', 'e', 'i', 'g', 'p'],
    ['w', 't', 'c', 'k', 's', 'n', 'b', 'm', 'r', 'v', 'h', 'j', 'q', 'p', 'o'],
    ['w', 't', 'c', 'u', 's', 'z', 'f', 'b', 'm', 'a', 'y', 'e', 'q', 'g', 'o'],
    ['c', 'l', 'u', 'k', 's', 'z', 'n', 'f', 'b', 'r', 'a', 'y', 'v', 'e', 'i'],
    ['t', 'c', 'l', 'k', 's', 'z', 'f', 'b', 'm', 'r', 'a', 'e', 'i', 'g', 'p'],
    ['w', 'c', 'l', 'u', 'k', 's', 'x', 'n', 'f', 'b', 'a', 'y', 'i', 'j', 'q'],
    ['w', 't', 'u', 'z', 'x', 'n', 'f', 'a', 'y', 'e', 'i', 'q', 'g', 'p', 'o'],
    ['w', 't', 'u', 'k', 'z', 'x', 'n', 'b', 'r', 'y', 'h', 'j', 'q', 'g', 'o'],
    ['w', 't', 'c', 'l', 'u', 'k', 'n', 'a', 'y', 'h', 'e', 'j', 'q', 'p', 'o'],
]

skeleton = hint[0]
for arr in hint[1:]:
    last_index = 0
    for letter in arr:
        if letter in skeleton:
            last_index = skeleton.index(letter) + 1
            continue
        first, last = letter, skeleton[last_index]
        existing_letter_rows = [ar for ar in hint if first in ar and last in ar]
        letters_in_order = [{l: count} for count, l in enumerate(existing_letter_rows[0]) if first == l or last == l]

        if first == list(letters_in_order[0].keys())[0]:
            skeleton = skeleton[:last_index] + [letter] + skeleton[last_index:]
            last_index += 1


print(skeleton)
def letter_pattern_groups(pattern):
    if '(' not in pattern:
        return list(pattern)

    patterns = []
    qtd = 0
    while qtd <= len(pattern)-1:
        letter = pattern[qtd]
        if letter != '(':
            patterns.append(letter)
            qtd += 1
        else:
            p = ''
            qtd += 1
            letter = pattern[qtd]
            while letter != ')':
                p += letter
                qtd += 1
                letter = pattern[qtd]
            qtd += 1
            patterns.append(p)

    return patterns

def is_alien_word(word, pattern, length):
    groups = letter_pattern_groups(pattern)

    for index, letter in enumerate(word):
        if letter not in groups[index]:
            return False

    return True

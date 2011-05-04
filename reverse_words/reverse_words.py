def reverse_words(line):
    return ' '.join(reversed(line.split(' ')))

if __name__ == '__main__':
    lines = []
    cases = input()

    for case in range(cases):
        lines.append(reverse_words(raw_input()))

    for index, line in enumerate(lines):
        print 'Case #%d: %s' % (index + 1, line)


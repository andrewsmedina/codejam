def reverse_words(line):
    return ' '.join(reversed(line.split(' ')))

if __name__ == '__main__':
    lines = []

    input_file_name = 'large.in'
    output_file_name = 'large.out'

    input_file = open(input_file_name)
    cases = int(input_file.readline().replace('\n', ''))

    for case in range(cases):
        lines.append(reverse_words(input_file.readline().replace('\n', '')))

    input_file.close()

    output_file = open(output_file_name, 'w')

    for index, line in enumerate(lines):
        output_file.write('Case #%d: %s\n' % (index + 1, line))

    output_file.close()


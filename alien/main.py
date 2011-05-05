from alien import is_alien_word

if __name__ == '__main__':
    input_file_name = 'large.in'
    output_file_name = 'large.out'

    input_file = open(input_file_name)

    word_lenght, words_length, cases = [int(number) for number in input_file.readline().replace('\n', '').split(' ')]

    words = []

    for i in range(words_length):
        words.append(input_file.readline().replace('\n', ''))

    output_file = open(output_file_name, 'w')

    for i in range(cases):
        matches = 0
        pattern = input_file.readline().replace('\n', '')
        for word in words:
            if is_alien_word(word=word, pattern=pattern, length=word_lenght):
                matches += 1

        output_file.write('Case #%d: %d\n' % (i+1, matches))

    input_file.close()
    output_file.close()

def add_new_word():
    in_file = 'in.txt'
    out_file = 'collection.txt'
    word_file = 'words.txt'

    list_of_words = []
    list_n_word = []
    list_3_word = []
    list_4_word = []
    list_5_word = []

    # read from file and parse into List
    with open(out_file) as file_word:
        for line in file_word:
            for w in line.split():
                if w in list_of_words:
                    print("已存在: \t", w)
                else:
                    list_of_words.append(w)
            for w in line.split():
                if len(w) == 3:
                    list_3_word.append(w)
                if len(w) == 4:
                    list_4_word.append(w)
                if len(w) == 5:
                    list_5_word.append(w)

    with open(in_file) as file_word:
        for line in file_word:
            for w in line.split():
                if w in list_of_words:
                    print("已存在: \t", w)
                else:
                    print("新单词: \t", w)
                    list_of_words.append(w)

    # ask for new word
    while True:
        new_word = input("请输入新单词【Q-退出】：")
        if new_word == 'Q':
            break
        if new_word in list_of_words:
            print("已存在: \t", new_word)
        else:
            print("新单词: \t", new_word)
            list_of_words.append(new_word)

    list_of_words.sort()
    list_n_word.sort()

    for n, i in enumerate(list_of_words):
        if i in ['a-b-c-d', 'e-f-g', 'h-i-j-k', 'l-m-n', 'o-p-q', 'r-s-t', 'u-v-w-x-y-z']:
            list_of_words[n] = '\r\n### ' + i + '\r\n'

    list_of_words.remove('###')
    # print(list_of_words)

    # write to file
    with open(out_file, 'w') as file_word:
        file_word.write(' '.join(list_of_words))

    with open(word_file, 'w') as file_word:
        file_word.write(','.join(list_n_word))
        file_word.write('\r\n')
        file_word.write(','.join(list_3_word))
        file_word.write('\r\n')
        file_word.write(','.join(list_4_word))
        file_word.write('\r\n')
        file_word.write(','.join(list_5_word))


if __name__ == '__main__':
    add_new_word()

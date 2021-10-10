def add_new_word():

    in_file = 'in.txt'
    out_file = 'collection.txt'

    list_of_words = []

    # read from file and parse into List
    with open(out_file) as file_word:
        for line in file_word:
            for w in line.split():
                if w in list_of_words:
                    print("已存在: \t", w)
                else:
                    list_of_words.append(w)
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
        new_word = input("请输入新单词【N-退出】：")
        if new_word == 'N':
            break
        if new_word in list_of_words:
            print("已存在: \t", new_word)
        else:
            print("新单词: \t", new_word)
            list_of_words.append(new_word)

    list_of_words.sort()

    for n, i in enumerate(list_of_words):
        if i in ['a-b-c-d', 'e-f-g', 'h-i-j-k', 'l-m-n', 'o-p-q', 'r-s-t', 'u-v-w-x-y-z']:
            list_of_words[n] = '\r\n### ' + i + '\r\n'

    list_of_words.remove('###')

    print(list_of_words)

    # write to file
    with open(out_file, 'w') as file_word:
        file_word.write(' '.join(list_of_words))


if __name__ == '__main__':
    add_new_word()

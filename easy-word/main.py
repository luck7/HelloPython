def add_new_word():

    list_of_words = []

    # read from file and parse into List
    in_file = 'in.txt'
    with open(in_file) as file_word:
        for line in file_word:
            for w in line.split():
                list_of_words.append(w)

    list_of_words.sort()
    print(list_of_words)

    # ask for new word
    while True:
        new_word = input("请输入新单词【N-退出】：")
        if new_word == 'N':
            break
        if new_word in list_of_words:
            print(new_word + " 已存在。")
        else:
            print("新单词: ", new_word)
            list_of_words.append(new_word)

    # write to file
    out_file = 'out.txt'
    with open(out_file, 'w') as file_word:
        file_word.write(' '.join(list_of_words))


if __name__ == '__main__':
    add_new_word()


def main():
    count_words =0

    with open('referat.txt', 'r', encoding='utf-8') as f:
        for line in f:
            w_l = line.split(' ')
            for word in w_l:
                if word != '':
                    count_words += 1
        print('количество слов в тексте = ',count_words)

            


main()
import string
import random


def clean_phrase(phrase):
    # get str punctuations
    punct = string.punctuation

    # replace any characters
    for i in punct:
        phrase = phrase.replace(i, '')

    phrase = phrase.replace('N', '')

    # replace spaces
    phrase = phrase.replace(' ', '')
    phrase = phrase.lower()

    return phrase


def get_list_indexes(int_begin, int_end, len_input):
    n_list = []
    dl = len_input
    while dl > 0:
        n_random = random.randint(int_begin, int_end)
        num = min(n_random, dl)

        n_list.append(num)
        dl = dl - num

    if 1 in n_list:
        print('+++++++++++++recursion+++++++++++')
        print(n_list)
        print('+++++++++++++++++++++++++++++++++++')
        n_list = get_list_indexes(int_begin,int_end,len_input)
    return n_list


def get_list_words(phrase, l_ind):
    list_words = []
    n = 0
    for s in l_ind:
        last_ind = n + s
        list_words.append(phrase[n:last_ind])
        n = last_ind

    return list_words


def get_list_setns(list_words, list_ind_words, numbs_sents):
    list_sents = []

    f_ind = 0
    while numbs_sents > 0:
        for inw in list_ind_words:
            last_ind = f_ind + inw
            words = list_words[f_ind:last_ind]
            sentn = ' '.join(words)
            list_sents.append(sentn)
            print(sentn)
            f_ind = last_ind
            numbs_sents -= 1

    return list_sents


phrase = str("" "Beautiful is better than ugly. \ NExplicit is better than implicit. \ N" "")

phrase = clean_phrase(phrase)
print(phrase)

len_phrase = len(phrase)

list_len_words = get_list_indexes(2, 8, len_phrase)
list_words = get_list_words(phrase, list_len_words)
print(list_words)

numbs_words = len(list_words)
print(numbs_words)

list_len_sent = get_list_indexes(2, 6, numbs_words)
print(list_len_sent)

numbs_sents = len(list_len_sent)
print(numbs_sents)

list_sents = get_list_setns(list_words, list_len_sent, numbs_sents)
print(list_sents)

list_sents = [s.capitalize() for s in list_sents]
print(list_sents)

text_s = '.\n'.join(list_sents)
print(text_s)

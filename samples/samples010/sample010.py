import numpy as np
import random
import string
import datetime
import time


def poisson(lam):
    return np.random.poisson(lam=lam)

def create_time():
    return str(datetime.datetime.now())

def create_word(char_size):
    char_size = poisson(char_size)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=char_size))

def create_sentence(word_size, char_size):
    word_size = poisson(word_size)
    word_list = []
    for ii in range(word_size):
        word_list.append(create_word(char_size))
    return ' '.join(word_list)

def create_log(word_size, char_size):
    time_str = create_time()
    sentence_str = create_sentence(word_size, char_size)
    return time_str + ' ' + sentence_str

def sleep_log(log_size_per_sec):
    msec = int(1000 / log_size_per_sec)
    msec = poisson(msec)
    return msec / 1000
#    usec = int(1000000 / log_size_per_sec)
#    usec = poisson(usec)
#    return usec / 1000000

def main(log_size_per_sec, word_size_per_sentence, char_size_per_word):
    while(1):
        log = create_log(word_size_per_sentence, char_size_per_word)
        print(log)
        # sleep
#        time.sleep(sleep_log(log_size_per_sec))

LOG_SIZE_PER_SEC = 100
WORD_SIZE_PER_SENTENCE = 100
CHAR_SIZE_PER_WORD = 10

main(LOG_SIZE_PER_SEC, WORD_SIZE_PER_SENTENCE, CHAR_SIZE_PER_WORD)
import random
import codecs
import file_operation
import error_log

kusa_dict = []

#read_file
def reload_file(name) -> str:
    if name == 'kusa_dict' or name == 'all':
        #「草」への返信コメ
        try:
            with codecs.open('kusa_dict.txt','r','utf-8') as f:
                kusa_dict.clear
                for txt in f:
                    kusa_dict.append(txt.strip())
            return 0
        except Exception as Err:
            print(str(Err))
            return -1

#random_reply
class rand_rep:
    def __init__(self,txt):
        pass

    def kusa():
        try:
            return random.choice(kusa_dict)
        except IndexError as IdxErr:
            return

class dict_add:
    def __init__(self,txt):
        pass

    def kusa(txt) -> str:
        reload_file('kusa_dict')
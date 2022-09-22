f = open('./text/tokenization-input-part-A.txt','r')

def handle_abbreviation(word): 
    word_list = []
    split_words = word.split('.')
    is_single_word = True
    for w in split_words:
        if len(w) > 1:
            word_list.append(w)
            is_single_word = False
        elif len(w) == 1:
            if len(word_list) == 0:
                word_list.append(w)
            elif is_single_word:
                word_list[len(word_list)-1] += w
            else:
                word_list.append(w)
            is_single_word = True
    return word_list

def handle_punctuation_start_end(word):
    punctuations = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
    for c in punctuations:
        if len(word)>0 and word[0] == c:
            word = word.replace(c,'')
        if len(word)>0 and word[-1] == c:
            word = word.replace(c,'')
    return word

def handle_punctuation(word):
    punctuations = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
    word_list = []
    for c in punctuations:
        if c in word:
            word_list = word.split(c)
            return word_list
    return [word]

def tokenization(word):
    word = handle_punctuation_start_end(word)
    word_list = handle_abbreviation(word)
    for w in word_list:
        for new_w in handle_punctuation(w):
            if len(new_w) > 0:
                token_result.append(new_w)

def contractions(word):
    if "'" in word:
        word_arr = word.split("'")
        for w in word_arr:
            w = w.strip()
            word = ''.join(word_arr)
    return word

def handle_txt_array():
    i = 0
    while i < len(txt_array):
        word = txt_array[i].lower().strip()
        word = contractions(word)
        if word == 'mr.' or word == 'mrs.':
            token_result.append(word+txt_array[i+1].strip())
            i += 1
        else:
            tokenization(word)
        i += 1

def handle_stop_word():
    stop_word_file = open('./text/stopwords.txt','r')
    StopLines = stop_word_file.readlines()
    for stop_word in StopLines:
        while stop_word.strip() in token_result:
            token_result.remove(stop_word.strip())

txt_array = []
token_result = []
Lines = f.readlines()
for line in Lines:
    line_array = line.split(' ')
    txt_array = txt_array + line_array
print(txt_array)
print('')

handle_txt_array()
handle_stop_word()
print(token_result)

f.close()
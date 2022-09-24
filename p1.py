# PART A
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

def handle_punctuation(word):
    punctuations = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
    word_list = [word]
    for c in punctuations:
        for word in word_list:
            if c in word:
                word_list = word.split(c)
    if len(word_list) == 0:
        return [word]
    return word_list

def tokenization(word, token_result):
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

def handle_txt_array(txt_array, token_result):
    i = 0
    while i < len(txt_array):
        word = txt_array[i].lower().strip()
        word = contractions(word)
        if word == 'mr.' or word == 'mrs.':
            token_result.append(word+txt_array[i+1].strip())
            i += 1
        else:
            tokenization(word, token_result)
        i += 1
    return token_result

def handle_stop_word(token_result):
    stop_word_file = open('./stopwords.txt','r')
    StopLines = stop_word_file.readlines()
    for stop_word in StopLines:
        while stop_word.strip() in token_result:
            token_result.remove(stop_word.strip())
    return token_result

def is_vowel(char):
    vowels = ['a','e','o','u','y','i']
    if char in vowels:
        return True
    return False

def step_1a(word):
    if 'sses' in word and word[-1] == 's' and word[-2] == 'e' and word[-3] == 's' and word[-4] == 's' :
        return word[:-2]
    if len(word)>2 and word[-1] == 's':
        if word[-2] == 's':
            return word
        if word[-2] == 'u':
            return word
        if not is_vowel(word[-2]):
            word = word[:-1]
            return word
    if 'ied' in word or 'ies' in word:
        if len(word) > 4:
            word = word[:-2]
            return word
        return word[:-1]
    if len(word)>3 and word[-1] == 's' and is_vowel(word[-2]):
        return word[:-1]
    return word

def contains_vowel(word):
    for c in word:
        if is_vowel(c):
            return True
    return False

def end_with_at_bl_iz(word):
    return word[-1] == 't' and word[-2] == 'a' or word[-1] == 'l' and word[-2] == 'b' or word[-1] == 'z' and word[-2] == 'i'

def end_with_double_letter(word):
    return len(word) > 2 and word[-1] == word[-2]

def is_short_word(word):
    change_count = 0
    if is_vowel(word[0]):
        for i in range(0, len(word)-1):
            if is_vowel(word[i]) != is_vowel(word[i+1]):
                change_count += 1
        if change_count == 1 or change_count == 2:
            return True
    elif not is_vowel(word[0]):
        for i in range(0, len(word)-1):
            if is_vowel(word[i]) != is_vowel(word[i+1]):
                change_count += 1
        if change_count == 2 or change_count == 3:
            return True
    return False

def add_e(word):
    if end_with_at_bl_iz(word):
        return word+'e'
    elif end_with_double_letter(word):
        if len(word)>2 and word[-1] == 'l' and word[-2] == 'l' or word[-1] == 's' and word[-2] == 's' or word[-1] == 'z' and word[-2] == 'z':
            return word
        return word[:-1]
    elif is_short_word(word):
        return word+'e'
    return word

def delete_ed_edly_ing_ingly(word):
    if 'edly' in word and contains_vowel(word[:-4]):
        word = word.replace('edly','')
        return add_e(word)
    elif 'ed' in word and contains_vowel(word[:-2]) and word[-1] == 'd' and word[-2] == 'e':
        word = word.replace('ed','')
        return add_e(word)
    elif 'ingly' in word and contains_vowel(word[:-5]):
        word = word.replace('ingly','')
        return add_e(word)
    elif 'ing' in word and contains_vowel(word[:-3]):
        word = word.replace('ing','')
        return add_e(word)
    return word

def handle_eed_eedly(word):
    def replace_eed_eedly(i,word_to_replace,word):
        cons_preceed = False
        while i >= -len(word):
            if is_vowel(word[i]):
                if cons_preceed:
                    word = word.replace(word_to_replace,'ee')
                    return word
                return word
            else:
                cons_preceed = True
            i -= 1
        return word
    if 'eedly' in word:
        return replace_eed_eedly(-6,'eedly',word)
    if 'eed' in word:
        return replace_eed_eedly(-6,'eed',word)
    return word

def step_1b(word): 
    word = handle_eed_eedly(word)
    word = delete_ed_edly_ing_ingly(word)
    return word

def handle_stemming(token_result):
    step_1a_result = []
    step_1b_result = []
    for word in token_result:
        step_1a_result.append(step_1a(word))
    for word in step_1a_result:
        step_1b_result.append(step_1b(word))
    return step_1b_result

def handle_part_a(txt_array):
    token_result = []
    token_result = handle_txt_array(txt_array,token_result)
    token_result = handle_stop_word(token_result)
    return handle_stemming(token_result)

f = open('./tokenization-input-part-A.txt','r')
part_a_txt_array = []
Lines = f.readlines()
for line in Lines:
    line_array = line.split(' ')
    part_a_txt_array = part_a_txt_array + line_array
# print(part_a_txt_array)
# print('')
result = handle_part_a(part_a_txt_array)
print(result)
f.close()

write_f = open("./tokenized-A.txt", "w")
for word in result:
    write_f.write(str(word)+'\n')       
write_f.close()

#############################################################################################################################
#PART B

# f_b = open('./tokenization-input-part-B.txt','r')
# part_b_txt_array = []
# Lines_B = f_b.readlines()
# for line in Lines_B:
#     line_array = line.split(' ')
#     part_b_txt_array = part_b_txt_array + line_array

# result_b = handle_part_a(part_b_txt_array)

# f_b.close()

# def handle_most_freq(term_dict):
#     return

# def count_term(token_array):
#     term_count = {}
#     for token in token_array:
#         if token not in term_count:
#             term_count[token] = 1
#         else:
#             term_count[token] += 1
#     return term_count

# def handle_part_b(token_array):
#     most_freq_term = {}
#     count_dict = count_term(token_array)
#     sorted_count_dict = sorted(count_dict.items(), key=lambda x : x[1], reverse=True)
#     return sorted_count_dict

# print(handle_part_b(result_b))

# write_f_b = open("./tokenized-B.txt", "w")
# for word in result_b:
#     write_f_b.write(str(word)+'\n')       
# write_f.close()


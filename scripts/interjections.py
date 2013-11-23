import os
import string
input_dir = '../200WordBlocks'
#these are always interjections in the Book of Mormon
interjections = ['yea', 'o', 'oh', 'wo', 'woe', 'ah', 'nay', 'hallelujah',
                 'alleluia' , 'alas', 'amen', 'lo', 'indeed', 'well']
#these vary, depending on the context
context_interjections = ['behold', 'no']
pronouns = ['i', 'we', 'mine', 'there']

def check_context(word, word_no_punc, next_word):
    punctuation = set(string.punctuation)
    end_char = word[-1:]
    if end_char in punctuation or next_word in pronouns:
        return 1
    return 0

def map_interjections(block, block_no_punc):
    words_found = {}
    for i in range(len(block)-1):
        word = block_no_punc[i].lower()
        can_add_word = 0
        if word in interjections:
            can_add_word = 1
        elif word in context_interjections:
            if i < len(block)-1:
                can_add_word = check_context(block[i].lower(), word, block[i+1].lower())
            else:
                can_add_word = check_context(block[i].lower(), word, block[i].lower())

        if can_add_word == 1:
            if word in words_found:
                words_found[word] += 1
            else:
                words_found[word] = 1
    
    return words_found

def get_block(file, writefile):
    file = open(file, 'r')
    block_200 = str(file.read())
    block_200 = block_200.split()
    
    punctuation = set(string.punctuation)
    #this kills any hyphenated compound words, but there aren't any that
    #are interjections, so we go ahead with it
    block_200_no_punc = []
    for word in block_200:
        no_punc = ''.join(ch for ch in word if ch not in punctuation)
        block_200_no_punc.append(no_punc)
    writefile = open(writefile, 'w')
    writefile.write(repr(map_interjections(block_200, block_200_no_punc)))
    writefile.close()
    file.close()
    
def main():
    for folder in os.listdir(input_dir):
        path = [input_dir, '/', folder]
        for file in os.listdir(''.join(path)):
            filepath = path
            if file.endswith('.txt'):
                writefile = file[:-3]+'inter'
                get_block(''.join(filepath)+'/'+file,
                          ''.join(filepath)+'/'+writefile)
    print('All done!')

if __name__ == '__main__':
    main()

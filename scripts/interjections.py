import os
import string
input_dir = '../200WordBlocks'
output_dir = '../TestDirectory'

#FEEL FREE TO ADD TO THESE INTERJECTION LISTS IF YOU CAN FIND OTHER EXAMPLES

#these are always interjections in the Book of Mormon
interjections = ['yea', 'o', 'oh', 'wo', 'woe', 'ah', 'nay', 'hallelujah',
                 'alleluia' , 'alas', 'amen', 'lo', 'indeed', 'verily', 'adieu']

#these next two vary, depending on the context

#these need to check whether they are immediately followed by punctuation
punc_interjections = ['behold', 'no', 'farewell']
#this dict checks whether the key word is followed by a value word (ignore punc)
next_word_interjections = {
    'behold':['i', 'we', 'mine', 'there', 'how'],
    'farewell':['until']}

def check_context(word, word_no_punc, next_word):
    if word_no_punc in punc_interjections:
        punctuation = set(string.punctuation)
        end_char = word[-1:]
        if end_char in punctuation:
            return 1
    if word_no_punc in next_word_interjections:
        if next_word in next_word_interjections[word_no_punc]:
            return 1
    return 0

def map_interjections(block, block_no_punc):
    words_found = {}
    for i in range(len(block)-1):
        word = block_no_punc[i].lower()
        can_add_word = 0
        if word in interjections:
            can_add_word = 1
        elif word in punc_interjections or word in next_word_interjections:
            if i < len(block)-1:
                can_add_word = check_context(block[i].lower(), word, block_no_punc[i+1].lower())
            else:
                can_add_word = check_context(block[i].lower(), word, block_no_punc[i].lower())

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
    for file in os.listdir(input_dir):
        if file.endswith('.txt'):
            author, block, good = file.split('_')
            block_num, extension = good.split('.')
            writefile = author + "-" + block_num + "-interjections.inter"
            get_block(input_dir+'/'+file,
                      output_dir+'/'+writefile)
    print("All Done!")

if __name__ == '__main__':
    main()

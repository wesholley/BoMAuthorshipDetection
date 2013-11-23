import os
import string
input_dir = '../200WordBlocks'
interjections = ['yea', 'o', 'oh', 'wo', 'woe', 'no', 'ah', 'nay', 'how great',
                 'hallelujah', 'alleluia', 'behold', 'moreover', 'alas', 'amen',
                 'lo', 'indeed', 'well']

def map_interjections(block):
    words_found = {}
    for word in block:
        word = word.lower()
        if word in interjections:
            if word in words_found:
                words_found[word] += 1
            else:
                words_found[word] = 1
    return words_found

def get_block(file, writefile):
    file = open(file, 'r')
    block_200 = str(file.read())
    exclude = set(string.punctuation)
    block_200 = ''.join(ch for ch in block_200 if ch not in exclude)
    block_200 = block_200.split()
    writefile = open(writefile, 'w')
    writefile.write(repr(map_interjections(block_200)))
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

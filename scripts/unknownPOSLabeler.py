############################################################
# Tags all the parts of speech which were tagged as "unknown"
# by the part of speech tagger
############################################################

import os

proper_nouns = {}     # A list of proper nouns in the Book of Mormon 

############################################################
# Fills the list with proper nouns in the Book of Mormon
############################################################
def load_proper_nouns(directory, filename):
    noun_list = open(directory + filename, 'r')
    
    print "start"
    for line in noun_list:
        word, classification = line.strip('\n').split('\t')
        if not word in proper_nouns.keys():
            proper_nouns[word.lower()] = classification.upper()

    return

############################################################
# Processes the fileName at directory, opening the file and 
# giving replacing all words tagged as UNKNOWN as either
# proper nouns or transitive verbs, based on whether or not
# they are in the list of proper nouns found in the Book of Mormon
############################################################
def process_author_file(directory, fileName):
    print "directory", directory, "fileName", fileName
    author = fileName.split('.')
    print author
    unknown_words = {}
    
    # Open the file and find unknown tags
    f_read = open(directory + fileName)
    output = ""
    
    for line in f_read:
        word, classification = line.strip('\n').split('/')
        if (classification == 'UNKNOWN') and (not word.lower() in unknown_words.keys()):
            if word.lower() in proper_nouns.keys():
                line = line.replace(classification, 'NP')
            else:
                line = line.replace(classification, 'VBN')  #TODO - check this tag--should be transitive verb
        output = output + line
    f_read.close()

    f_write = open(directory + fileName, 'w')
    f_write.write(output)
            
    return


############################################################
# Main
############################################################
if __name__ == '__main__':
    proper_noun_directory = "../"
    test_directory = "../ParseReadyAuthors/"
    
    # load the dictionary
    load_proper_nouns(proper_noun_directory, 'BoMProperNouns.txt')
    
    # update the part of speech tagging
    print os.listdir(test_directory)
    for fileName in os.listdir(test_directory):
        if fileName.endswith(".txt"):
            process_author_file(test_directory, fileName)
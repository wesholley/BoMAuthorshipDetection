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
# giving the unknown parts of speech a tag, then appending
# that word with the newly taggd part of speech at the end 
# of the file, leaving the "unknown" word up above
############################################################
def process_author_file(directory, fileName):
    print "directory", directory, "fileName", fileName
    author, block, junk = fileName.split('-')
    unknown_words = {}
    line_count = 0
    
    # Open the file and find unknown tags
    f = open(directory + fileName, 'w')
    for line in f:
        line_count = line_count + 1
        word, classification = line.strip('\n').split('/')
        if (classification == 'UNKNOWN') and (not word in unknown_words.keys()):
            print "unknown:", word, classification 
            if word in proper_nouns:
                
                unknown_words[word] = 'NP'  #proper noun
            else:
                #TODO - check this tag--should be transitive verb
                unknown_words[word] = 'VBN' #transitive verb
        
    # Appends all of the now-tagged "unknown" words
    # to the end of the file with their new tags
    with open(directory+fileName, "a") as myfile:
        for word in unknown_words.keys():
            print word, unknown_words[word]
            myfile.write(word + '/' + unknown_words[word] + '\n')
            
    return


############################################################
# Main
############################################################
if __name__ == '__main__':
    proper_noun_directory = "../"
    test_directory = "../TestDirectory/"
    
    # load the dictionary
    load_proper_nouns(proper_noun_directory, 'BoMProperNouns.txt')
    
    # update the part of speech tagging
    for fileName in os.listdir(test_directory):
        if fileName.endswith(".txt"):
            process_author_file(test_directory, fileName)
import os
import re

# Returns an array with all the words from the file in it
#    file - handle to the open file to be read
#    blocks_directory - author-specific directory to write the blocks of text
#    filename - the name of the file (when written, the block number is appended)
def getBlocks(file, blocks_directory, filename):
    # create ouput directory for the blocks for each author
    print "==========\n BLOCKS FOR:", filename, "\n=========="
    if not os.path.exists(blocks_directory):
        os.makedirs(blocks_directory)
     
    # remove newlines and hyphens, put in array
    text = file.read()
    text = text.strip('\n').replace('--', ' ').replace('\n', ' ')
    text = re.sub(' +', ' ', text)
    text_array = text.split(' ')
     
    # count words 
    length =  len(text_array)
    numBlocks = length/200
    print "Numblocks", numBlocks
 
    # create blocks of 200 words and write to file       
    curblock = ""
    offset = 0;
    for block in range(0, numBlocks):
        print "----\nBlock:", block, "\n----"
        # get 200 words for the block
        for word in range((0+offset), (200+offset)):
            curblock = curblock + " " + text_array[word]
        
        # write block to a file in author-specific folder (blocks_directory)
        file_directory = blocks_directory + "/" + filename + "_block_" + str(block) + ".txt"
        block_file = open(file_directory, 'w+')
        block_file.write(curblock)
        block_file.close()
        
        # update offset and curblock 
        offset = offset + 200
        print "\t Written to:", file_directory
        curblock = ""

############################################################
# Builds blocks based upon files of tagged output.  One line
# represents one word
############################################################    
def getBlocksByLines(file_path, blocks_directory, filename):
    # create ouput directory for the blocks for each author
    print "==========\n BLOCKS FOR:", filename, "\n=========="
        
    # get line count
    wordCount = 0
    with open(file_path, 'r') as file:
        for line in file:
            wordCount = wordCount + 1
    
    # get number of blocks needed
    numBlocks = wordCount/200
    print "wordcount: ", wordCount, "Numblocks", numBlocks
    
    # create blocks of 200 words and write to file
    blocksMade = 0
    blockLineCount = 0
    curBlock = ""
    
    with open(file_path, 'r') as file:
        for line in file:
#             print "Line:", line, "BlockLineCount:", blockLineCount, "blocksMade:", blocksMade 
#             print "Curblock:", len(curBlock.split('\n'))
            if (blocksMade == numBlocks):   # already made as many blocks as we need
                break
            if (blockLineCount == 199):     # end of the current block (200 words)
                blockLineCount = 0
                blocksMade = blocksMade + 1
                saveBlockToFile(blocks_directory, filename, blocksMade, curBlock)
                curBlock = ""
            else:                           # keep building curBlock
                curBlock = curBlock + line
                blockLineCount = blockLineCount + 1
        print "\n"

            
############################################################
# Saves a block to file
############################################################
def saveBlockToFile(blocks_directory, filename, blockNumber, curBlock):
    # write block to a file in author-specific folder (blocks_directory)
#     if not os.path.exists(blocks_directory):
#         os.makedirs(blocks_directory)
    block_destination = blocks_directory + "/" + filename + "_block_" + str(blockNumber) + ".txt" 
    block_file = open(block_destination, 'w+')
    block_file.write(curBlock)
    block_file.close()
        
 
    
############################################################
# Main
############################################################
if __name__ == '__main__':
    """ load the files """
    INPUT_PATH = "../ParseReadyAuthors/"
    OUTPUT_PATH = "../TestDirectory/"
    dir_contents = os.listdir(INPUT_PATH)   # this folder CANNOT HAVE SUB-FOLDERS or .read() will break
     
    # Break each author's text into blocks of 200 words
    for x in range(0, len(dir_contents)):
        #open the file
        file = dir_contents[x] 
        print "file:" + file
        file_path = INPUT_PATH + file
        output_file = OUTPUT_PATH + file

        temp = getBlocksByLines(file_path, OUTPUT_PATH, dir_contents[x].strip('.txt'))
    
    print "\n\nDone!"     
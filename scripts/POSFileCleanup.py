

#====================================
#
# Main clean up method. This is where each line is written to the file.
#
#====================================
def cleanUp(lines, out, fileName):
    count = 1 # Keeping track of tag count per block for testing purposes.
    for line in lines:
        if line.strip():
            tokens = removeBrackets(line).split(' ')
            for tag in tokens:
                if validTag(tag):
                    if '/' in tag:
                        out.write(tag.strip() + '\n') # Writes tag to it's own line
                        count += 1
#     print count
#     if count != 200:
#         if count < 195:
#             print fileName
#             print count
#         elif count > 205:
#             print fileName
#             print count

#====================================
#
# Checks to see if the line is enclosed in brackets and removes them.
#
#====================================
def removeBrackets(string):
    if '[' in string:
        if ']' in string:
            return string[2:-2]
        else:
            return string
    else:
        return string

#====================================
#
# Removes any tags or lines that contain invalid information.
# Example: punctuation, random brackets, parenthesis.
#
#====================================
def validTag(string):
    if '!' in string:
        return False
    elif '-' in string:
        return False
    elif ':' in string:
        return False
    elif '?' in string:
        return False
    elif '.' in string:
        return False
    elif ',' in string:
        return False
    elif ';' in string:
        return False
    elif '(' in string:
        return False
    elif ')' in string:
        return False
    elif '[' in string:
        return False
    elif ']' in string:
        return False
    elif '=' in string:
        return False
    else:
        return True

#====================================
#
# Finds the files to be parsed.
#
#====================================
def getFiles(folderPath, outputPath):
    import os
    #May hard code the paths if desired.
#     outputPath = 'C:\\Users\\okiobe\\Documents\\ParseReadyBlocks\\'
#     folderPath = 'C:\\Users\\okiobe\\Documents\\200WordBlocksTagged\\'
    author = ''
    for (path, dirs, files) in os.walk(folderPath):
        if os.path.exists(os.path.join(path, 'tags.txt')): # Performs operation on only the tags.txt files
            iFile = os.path.join(path, 'tags.txt')
            number = path.split('.')[0].split('_')[2] # Extracts the block number from the folder name
            folder = path.split('\\')
            if author == folder[5]: # Changes the name of the author when the author folder changes
                inputFile = open(iFile).readlines()
                oFile = "%s%s-%s.txt" % (outputPath, author, number) 
                outputFile = open(oFile, 'w')
                cleanUp(inputFile, outputFile, oFile) # oFile only passed for testing purposes
                outputFile.close()
#                 print "%s%s-%d.txt" % (outputPath, author, count)
            else:
                author =  folder[5]
                inputFile = open(iFile).readlines()
                oFile = "%s%s-%s.txt" % (outputPath, author, number)
                outputFile = open(oFile, 'w')
                cleanUp(inputFile, outputFile, oFile)
                outputFile.close()
#                 print "%s%s-%d.txt" % (outputPath, author, count)

#====================================
#
# Does the same thing as getFiles except it only checks one folder
# Meant for parsing the entire authors text
#
#====================================
def getEntireFiles(folderPath, outputPath):
    import os
    # May hard code the paths if desired.
#     outputPath = 'C:\\Users\\okiobe\\Documents\\ParseReadyBlocks\\'
#     folderPath = 'C:\\Users\\okiobe\\Documents\\200WordBlocksTagged\\'
    author = ''
    for (path, dirs, files) in os.walk(folderPath):
        if os.path.exists(os.path.join(path, 'tags.txt')): # Performs operation on only the tags.txt files
            iFile = os.path.join(path, 'tags.txt')
            folder = path.split('\\')[5].split('.')
#             print folder[0]
            if author == folder[0]: # Changes the name of the author when the author folder changes
                inputFile = open(iFile).readlines()
                oFile = "%s%s.txt" % (outputPath, author)
                outputFile = open(oFile, 'w')
                cleanUp(inputFile, outputFile, oFile) # oFile only passed for testing purposes
                outputFile.close()
            else:
                author =  folder[0]
                inputFile = open(iFile).readlines()
                oFile = "%s%s.txt" % (outputPath, author)
                outputFile = open(oFile, 'w')
                cleanUp(inputFile, outputFile, oFile)
                outputFile.close()

#====================================
#
# Start of main program
#
# First argument: Source Folder (VisualText structure inside)
# Second Argument: Destination Folder
# Third Argument: Type - b blocks, w whole author
#
#====================================
def main():
    import sys
    if sys.argv[3] == 'b':
        getFiles(sys.argv[1], sys.argv[2])
    elif sys.argv[3] == 'w':
        getEntireFiles(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
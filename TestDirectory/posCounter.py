
import os

############################################################
# Example:
# { 'Nephi': 
#			[
#				#block 0
#				{'NN': [10, ['nephi', 'bob', 'noun'...]],
#				 'AJ': [20, ['quikly', 'sharply', 'adjictive'...]],
#				 ...,
#				"Interjections":{'yea': 3, 'behold': 1, 'wo': 1} 
#				},
#				 #block 1 
#				 {'NN': [1,['obo']], ...,"Interjections":{'yea': 3, 'behold': 1, 'wo': 1}},
#				 #block n
#				 ...
#			]
#	'Alma': [...],
#	...
# }
############################################################
data = {}


############################################################
# This function will process a file that represents the number
# of interjection that a author used in a given block and adds
# it to 'data'
############################################################
def process_author_interjection_file(fileName):
	return


############################################################
# This function will open a file(An author's n^th block of text)
# and add it to the authors current list of blocks.
# It will also add all of the parts of speach(pos) the author used
# in that block and count them as well. 
############################################################
def process_author_file(fileName):
	author, block, junk = fileName.split('-')
	
	#TODO::: Call process_author_interjection_file(author+'-'+block+'-interjection.inter')

	if not author in data.keys():
		data[author] = []

	#Generate Block from File
	block_file = open(fileName, 'r')
	block = {}
	for word_and_pos in block_file:
		word, pos = word_and_pos.strip().split('/')

		#Add the Part of Speech if not already seen
		if not pos in block.keys():
			block[pos] = []
			block[pos].append(0)
			block[pos].append([])

		block[pos][0] = block[pos][0] + 1 	#Count the number of Parts of Speach
		block[pos][1].append(word)			#Keep track of each Part of Speach

	#Add Block to Author
	data[author].append(block)

	return

############################################################
# Goal: Nice Data structure to query any pos statistic 
#		required.
############################################################
if __name__ == '__main__':
	for fileName in os.listdir("."):
	    if fileName.endswith(".txt"):
	        process_author_file(fileName)

	print data
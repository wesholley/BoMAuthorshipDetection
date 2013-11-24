import os

for fileName in os.listdir("."):
    if fileName.endswith(".inter"):
    	author, block, good = fileName.split('_')
    	block_num, extension = good.split('.')
    	rename = author + "-" + block_num + "-interjections." + extension 
    	# print rename
        os.rename(fileName,rename)

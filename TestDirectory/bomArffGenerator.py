########################Create Attributes###################################
# All of our jobs


## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Make sure when you are building your attribute arrays you always
## run through the data (data structure/dictionary) by iterating
## through data.keys().  This will ensure our ordering is always
## the same.  See get_attribute_class_value_array for example of
## how i build the class attribute array...

############################################################
# This function will return an array that represents the
# attribute value of %ProperNouns versus Pronouns.
# the i'th value represents the i'th instance in our database.
#
# Criteria: Proper Nouns == (NP -- ProperN Singular, NPS -- plural),
#			ProNouns == (PP -- Personal,   PP$ -- Posesive, 
#						 WP -- wh-pronoun, WP$ -- wh-Possesive pronoun)
#
############################################################
def generate_array_of_Percent_ProperNouns_Vs_Pronouns(data):
	attribute_array = []

	for author in data.keys():
		for block_number in range(0, len(data[author])):
			np  = data[author][block_number]['NP'][0] #[0] Get me the count
			nps = data[author][block_number]['NPS'][0]
			pp  = data[author][block_number]['PP'][0]
			pps = data[author][block_number]['PPS$'][0]
			wp  = data[author][block_number]['WP'][0]
			wps = data[author][block_number]['WP$'][0]

			attribute_array.append(np + nps / float(pp+pps+wp+wps))

	print "Remove When validated:"
	print "Atrribute PPN/ProN:", attribute_array

	return attribute_array

############################################################
# This array will be used to build the final weka.arff file.
# The way it works is this:
#
# I was given responsibility for the %properNounsVsPronouns,
# so i created a function what will take our entire data structure
# (the same 'data' dictionary found in posCounter.py) and will
# simply create an array that represents this attribute value
# for each instance in our data structure.

# This array will simply link in all of our work.

# So i will call each function in this array to build get back
# all of the values for each individual attribute and then
# append them all together to build our new data base weka file.
# So we'll end up with something like:
# [%ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Nephi,
# %ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Nephi,
# %ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Nephi,
# %ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Nephi,
# ...
# %ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Alma,
# ...]
#
# This array just tells our driver how to get each of these
# data values...for example mine return all of the %ProperNounsVsPronouns.
# ... Call me if this is not clear.
#
# In other words...we will have an attribute for each function in this
# array... and the values for that respective attrubute will be returned
# by calling the function in the array with the 'data' object/dictionary
# found in posCounter.py
#
# Format: [(function, 'nameOfAtribute'),...]
############################################################
attribute_builder_functions_array = [ (generate_array_of_Percent_ProperNouns_Vs_Pronouns, 'properNounsVsPronouns')]




########################Create the General Structure of the ARFF File###################################
# Chris's Job
############################################################
############################################################
def get_attirbute_class_value_array(data):
	class_array = []

	for key in data.keys():
		for i in range(0, len(data[key])):
			class_array.append(key)

	print "Remove when validated:"
	print "Class Array:", class_array

	return class_array


############################################################
# Writes the bom_data to a file_name.arff Weka file
############################################################
def write_data_to_weka_data_file(data, file_name):
	write_header_to_file(data, file_name)
	write_data_to_file(data, file_name)
	return


############################################################
# Example:
# @relation 'BOM_By_Author'
# @attribute A0 {0,1}
# @attribute A1 {0,1}
# @attribute A2 {0,1}
# @attribute DIST real
# @attribute LNG numeric
# @attribute class {0,1} or {Nephi, Alma, JesusChris, ...}
############################################################
def write_header_to_file(data, file_name):
	arff_file = open(file_name, 'w')

	#Print Name of Database
	arff_file.write('@relation \'BOM_By_Author\'')

	#Print Atributes
	for att in attribute_builder_functions_array:
		arff_file.write('@attribute ' + att[1] + 'numeric')

	#Get Classes
	string_of_authors_with_commas = ""
	for author in data.keys():
		string_of_authors_with_commas = string_of_authors_with_commas + (',' if len(string_of_authors_with_commas) > 0 else "") + author

	#Print Classes
	arff_file.write('@attribute class {' + string_of_authors_with_commas + '}')

	arff_file.close()

	return

############################################################
# This function use attribute_builder_functions_array to 
# generate attribute values and then write those to the file.
# This function assumes that the data file has already
# had its header info writen.
# Example:
# @DATA
# 5.1,3.5,1.4,0.2,Iris-setosa
# ...
############################################################
def write_data_to_file(data, file_name):
	arff_file = open(file_name, 'a')

	arff_file.write('@data')

	#Build Attribute arrays
	att_arrays = []
	for att in attribute_builder_functions_array:
		att_arrays.append(att[0](data))

	#Add Class assignments
	att_arrays.append(get_attirbute_class_value_array(data))

	#Check: 
	#To check that each array has the same number of items
	curr_length = len(att_arrays[0]) 
	for array in att_arrays:
		if not len(array) == curr_length:
			print "\n\n\tHOLLY COW!!!!"
			print "We have an error in our attribute array generation!"
			print "I just discovered that the lengths of our attribute arrays don't match!"
			print "I'm going to blow chunks and die!!"
			return

	#Write attribute and class values to file_name
	for i in range(0, curr_length):
		str_instance = ""
		for array in att_arrays:
			str_instance = str_instance + (',' if len(str_instance) > 0 else '') + array[i]
		arff_file.write(str_instance)

	arff_file.close()

	print "Arff Generation:: Wrote:", len(att_arrays), "attributes, for", curr_length, 'instances.'

	return
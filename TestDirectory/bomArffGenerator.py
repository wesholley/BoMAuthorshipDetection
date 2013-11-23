########################Create Attributes###################################
# All of our jobs

############################################################
# This function will return an array that represents the
# attribute value of %ProperNouns verus Prounouns.
# the ith value represents the ith instance in our database.
############################################################
def generate_array_of_Percent_ProperNouns_Vs_Pronouns(data):
	attribute_array = []
	return attribute_array

############################################################
# This array will be used to build the final weka.arff file.
# The way it works is this:
# I was given responcibility for the %properNounsVsPronouns,
# so i created a function what will take our entire data structure(
# the same 'data' dictionary found in posCounter.py) and will
# simply create and array that represents this attribute value
# for each instance in our data structure.
# This array will simple link in all of our work...
# So i will call each function in this array to build get back
# all of the values for each indivdual attribute and then
# append them all together to build our new data base weka file.
# So we'll end up with somthing like:
# [%ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Nephi,
# %ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Nephi,
# %ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Nephi,
# %ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Nephi,
# ...
# %ProperNounsVsPronouns, InterjectionCnt, #Adjectives,..., Alma,
# ...]
#
# This array just tells our drive how to get each of these
# data values...for example mine return all of the %ProperNounsVsPronouns.
# ... Call me if this is no clear.

# In other words...we will have an attribute for each functio in this
# array... and the values for that respective attrubute will be returned
# by calling the function in the array with the 'data' object/dictionary
# found in posCounter.py
#
# Format: (function, 'nameOfAtribute')
############################################################
attribute_builder_functions_array = [ (generate_array_of_Percent_ProperNouns_Vs_Pronouns, 'properNounsVsPronouns')]







########################Create the General Structure of the ARFF File###################################
# Chris's Job


############################################################
# This function will write the bom_data to a weka file_name.arff
# file.
############################################################
def write_data_to_weka_data_file(data, file_name):

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
def write_header_to_file(file_name, data):
	arff_file = open(file_name, 'w')

	arff_file.write('@relation \'BOM_By_Author\'')

	for att in attribute_builder_functions_array:
		arff_file.write('@attribute ' + att[1] + 'numeric')

	string_of_authors_with_commas = ""
	for author in data.keys():
		string_of_authors_with_commas = string_of_authors_with_commas + "," if len(string_of_authors_with_commas > 0 else "" + author

	arff_file.write('@attribute class {' + string_of_authors_with_commas + '}')

	return

############################################################
#
############################################################
def write_data_to_file(data, file_name):
	
	return


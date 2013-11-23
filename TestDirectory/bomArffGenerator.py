

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
############################################################
attribute_builder_functions_array = [generate_array_of_Percent_ProperNouns_Vs_Pronouns]








############################################################
# This function will write the bom_data to a weka file_name.arff
# file.
############################################################
def write_data_to_weka_data_file(data, file_name):

	return


############################################################
############################################################
def write_header_to_file(file_name):
	return

############################################################
############################################################
def write_data_to_file(data, file_name):
	return


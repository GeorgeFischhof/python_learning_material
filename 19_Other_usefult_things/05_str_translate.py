
# Translate
# =========

# Replace and remove several characters from a string


# https://docs.python.org/3/library/stdtypes.html#str.translate
# https://docs.python.org/3/library/stdtypes.html#str.maketrans


# Example convert filename to ascii
# ---------------------------------

input_characters  = "öüóőúéáűíÖÜÓŐÚÉÁŰÍ "
output_characters = "ouooueauiouooueaui_"
remove_characters = ',?;:.-§¬~+^!˘%°/˛=`(˙)´˝¨¸÷×$ß¤'
table = str.maketrans(input_characters, output_characters, remove_characters)

print('Árvíztűrő tükörfúrógép'.translate(table))
#  ==> 'arvizturo_tukorfurogep'

#To run this, install module via: pip install langdetect
#To run the functions, it is best to run inside a terminal, rather than making a script and executing. For example, in linux, use command "Python" in terminal, then begin using the langdetect module.

#This example uses the keyword "detect" Note that the "detect" function works better on longer sentences instead of one word inputs.
from langdetect import detect
detect("Hello! How are you today? I'm doing well.")

#This example shows the probability of a phrase being of a certain language
from langdetect import detect_langs
detect_langs("Buenos Noches")

#Lastly, you can change the algorithm to get more consistent results with short phrases. If a single word, like "Hello", is appearing as German, rather than English, use: *Note this can mess up longer phrases*
from langdetect import DetectorFactory
DectorFactory.seed = 0


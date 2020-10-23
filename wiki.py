#This is an amazing program
#importing modules

import wikipedia
#first you have to install wikipedia module as it is not in-built
import warnings
#warning is in-built module
#this module in not important for this program
#this module hide warning from module, if occurs

# initializing a function
def mywiki(a):
    
    #try and except hideing errors, if occurs
    try:
        warnings.filterwarnings("ignore")
        result = wikipedia.summary(a, sentences = 3)
        return(result)
    
    except Exception as e:
        print(a,"is unable to find easily.There are many ",a,"which one do you want to find...")
        return(e)

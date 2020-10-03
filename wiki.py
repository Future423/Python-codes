import wikipedia
import warnings

def mywiki(a):
    import wikipedia
    import warnings

    try:
        warnings.filterwarnings("ignore")
        result = wikipedia.summary(a, sentences = 3)
        return(result)
    except Exception as e:
        print(a,"is unable to find easily.There are many ",a,"which one do you want to find...")
        return(e)

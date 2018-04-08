import re
def getnumber(tokens):
    number=""
    fout = open("results.tex", "a",encoding="utf-8")
    numregex=re.compile("(?:\+?(\d{1})?-?\(?(\d{3})\)?[\s\-\.]?)?(\d{3})[\s\-\.]?(\d{4})[\s\-\.]?")
    for i in range(len(tokens)):
        match=numregex.search(tokens[i])
        if(match):
            if(len(tokens[i])>=10):
                return(tokens[i])
    return number

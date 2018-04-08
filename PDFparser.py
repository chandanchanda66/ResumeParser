
import pdftotext
import getCategory
import tokenizer
import gender_guesser
import getphonenumber

def init():

    # input the file name
    filename = input("Enter Resume Name to Parse")
    text=pdftotext.convert("./SampleResume/"+filename)
    out = open("resumeoutput.txt", "w",encoding="utf-8")
    out.write(text)
    out.close()
    fout = open("results.tex", "w")
    fout.write("\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\
    \\title{Results}\n\\begin{document}\n\n")
    text=str(text).replace("\u200b","")
    return text.replace("\xa0","")

resume = init()
def main(resume):
    # initialize variables
    # have the words as tokens in a list
    tokens = tokenizer.input_file_lines(resume, [])
    word_tokens = tokenizer.input_file_words(resume, [])
    out = open("resulttoken.txt", "w",encoding="utf-8")
    out.write(str(tokens))
    out.close()
    out = open("resultwordtoken.txt", "w",encoding="utf-8")
    out.write(str(word_tokens))
    out.close()
    while '' in tokens:
        tokens.remove('')
    while ' ' in tokens:
        tokens.remove(' ')
    # get email

    email = ""
    print(tokens)

    for token in word_tokens:
        if "@" in token:
            email = token
            break
    fout = open("results.tex", "a")
    fout.write("\\section{" + email + "}\n")
    programming = getCategory.programming(resume)
    for i in range(tokens.__len__()):
        if(tokens[i]!=' '):
            print(tokens[i])
            fout.write("\\name{" + tokens[i] + "}\n")
            sex=gender_guesser.genderguesser(tokens[i])
            fout.write("\\sex{" + sex+ "}\n")
            break


    print(programming)
    recentcompany=getCategory.recentcompany(tokens)
    numbers = getphonenumber.extract_phone_numbers(resume)
    emails = getphonenumber.extract_email_addresses(resume)
    names = getphonenumber.extract_names(resume)
    print(str(numbers[i])+"\n"+str(emails[i])+"\n"+str(names[i]))
    fout.write("\\getnumber{" + str(numbers[i]) + "}\n")
    fout.write("\\recentcompany{" + recentcompany + "}\n")
    fout.close()
    return (email)

if type(resume) == list:
    for i in range(len(resume)):
        print( main(resume[i]))
    fout = open("results.tex", "a")
    fout.write("\\end{document}")
    fout.close()
elif resume != "":
    print (main(resume))
    fout = open("results.tex", "a")
    fout.write("\\end{document}")
    fout.close()


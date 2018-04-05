import re
import tokenizer
import datetime

def programming(resume):
    #print(resume)
    fout = open("results.tex", "a")
    fout.write("\\textbf{Programming Languages:} \\\\\n")
    programming = ["assembly", "bash", " c " "c++", "c#", "coffeescript", "emacs lisp",
         "go!", "groovy", "haskell", "java", "javascript", "matlab", "max MSP", "objective c", 
         "perl", "php","html", "xml", "css", "processing", "python", "ruby", "sml", "swift", 
         "latex" "unity", "unix" "visual basic" "wolfram language", "xquery", "sql", "node.js", 
         "scala", "kdb", "jquery", "mongodb"]

    pro=[]
    for i in range(len(programming)):
        if programming[i].lower() in resume.lower() != -1:
            if not("#" in programming[i]):
                pro.append(programming[i])
                fout.write(programming[i]+", ")


    fout.close()


    return pro


def recentcompany(tokens):
    #print(resume)
    fout = open("results.tex", "a",encoding="utf-8")
    experiences=["EXPERIENCE","Experience","experience"]
    yrregx = re.compile("(.*)\d{4}(.*)")
    tokenyrregex = re.compile("\d{4}")
    for k in range(len(experiences)):
        regex = re.compile("(.*)"+experiences[k]+ "(.*)")


        yrs=[]
        company=""
        for i in range(len(tokens)):
            m = regex.search(tokens[i])
            if m:
                company=tokens[i+1]
                print(tokens[i+1])
                for j in range(i+1,len(tokens)):
                    searchyr=yrregx.search(tokens[j])
                    if searchyr:
                        print(tokens[j])
                        yrtoken=tokenizer.input_file_words(str(tokens[j]).lower(), [])
                        print(yrtoken)
                        break

                break
        if(company!=""):
            break


    if(company==""):
        print("no experience")
        return "no experience"
    fout.write("\\recentcompany{" + tokens[i + 1] + ":} \\\\\n")
    for i in range(len(yrtoken)):
        yrsearchtoken=tokenyrregex.search(yrtoken[i])
        if yrsearchtoken:
            yrs.append(yrtoken[i])
        elif(yrtoken[i]=="present"):
            yrs.append(str(datetime.datetime.now().year))
        elif (yrtoken[i] == "now"):
            yrs.append(str(datetime.datetime.now().year))
    fout.write("\\experience duration{" + str(yrs) + " }\n")
    for i in range(len(yrs)):
        matchObj = re.match(r'(.*)(\d{4}).*', yrs[i], re.M | re.I)
        yrs[i]=matchObj.group(2)
    if(len(yrs)==2):
        experience=int(yrs[1])-int(yrs[0])

        fout.write("\\experience{" + str(experience) + " yrs}\n")

        print(experience)

    else:
        print(yrs)
        print("0")
        fout.write("\\experience{0 yrs}\n")


    fout.close()
    return (company)








import string
# import json

#list of key terms
terms = ["data", "camera", "microphone", "audio", "billing", "tracking", "location", "organisation", "organisation's"]

#open text file
doc = open("fp.txt", "r")
docData = doc.read()
docData = list(docData.split(" "))
doc.close()

#function to remove punctuation
def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result

#goes throgh each word in list
for x in range(len(docData)):

#makes it lower and removes punctuation
    word = docData[x].lower()
    waye = remove_punctuation(word)

#compare word to each key term
    for i in range(len(terms)):
#TODO: fix semicolon bug
        if word.strip() == terms[i]:
            docData[x] = word.upper()
        if waye.strip() == terms[i]:
            docData[x] = word.upper()

#joins list into string
print(" ".join(docData))

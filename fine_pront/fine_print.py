import string
# import json

terms = ["data", "camera", "microphone", "audio", "billing", "tracking", "location", "organisation", "organisation's"]

doc = open("fp.txt", "r")
docData = doc.read()
docData = list(docData.split(" "))
doc.close()

def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result
print(docData)
for x in range(len(docData)):
    word = docData[x].lower()
    waye = remove_punctuation(word)
    for i in range(len(terms)):
        if word.strip() == terms[i]:
            docData[x] = word.upper()
        if waye.strip() == terms[i]:
            docData[x] = word.upper()

print(" ".join(docData))

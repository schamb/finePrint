import string



#function to remove punctuation
def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result

#funcion for DATA
def find_DATA(document):
    #open keyTerms file

    termsDoc = open("txtFiles/DATA.txt", "r")

    keyTerms = termsDoc.readlines()
    termsDoc.close()
    for x in range(len(document)):
        word = document[x].lower()
        waye = remove_punctuation(word)

        for i in range(len(keyTerms)):
            keyTerm = keyTerms[i]
            keyTerm = keyTerm.strip()

            if word.strip() == keyTerm:
                document[x] = word.upper()
            if waye.strip() == keyTerm:
                document[x] = word.upper()

    return document
def find_ALL(document):
    #open keyTerms file

    termsDoc = open("txtFiles/ALL.txt", "r")

    keyTerms = termsDoc.readlines()
    termsDoc.close()
    for x in range(len(document)):
        word = document[x].lower()
        waye = remove_punctuation(word)

        for i in range(len(keyTerms)):
            keyTerm = keyTerms[i]
            keyTerm = keyTerm.strip()

            if word.strip() == keyTerm:
                document[x] = word.upper()
            if waye.strip() == keyTerm:
                document[x] = word.upper()

    return document
def find_LOCATION(document):
    #open keyTerms file

    termsDoc = open("txtFiles/LOCATION.txt", "r")

    keyTerms = termsDoc.readlines()
    termsDoc.close()
    for x in range(len(document)):
        word = document[x].lower()
        waye = remove_punctuation(word)

        for i in range(len(keyTerms)):
            keyTerm = keyTerms[i]
            keyTerm = keyTerm.strip()

            if word.strip() == keyTerm:
                document[x] = word.upper()
            if waye.strip() == keyTerm:
                document[x] = word.upper()

    return document
def find_BILLING(document):
    #open keyTerms file

    termsDoc = open("txtFiles/BILLING.txt", "r")

    keyTerms = termsDoc.readlines()
    termsDoc.close()
    for x in range(len(document)):
        word = document[x].lower()
        waye = remove_punctuation(word)

        for i in range(len(keyTerms)):
            keyTerm = keyTerms[i]
            keyTerm = keyTerm.strip()

            if word.strip() == keyTerm:
                document[x] = word.upper()
            if waye.strip() == keyTerm:
                document[x] = word.upper()

    return document
def find_CAMERA(document):
    #open keyTerms file

    termsDoc = open("txtFiles/CAMERA.txt", "r")

    keyTerms = termsDoc.readlines()
    termsDoc.close()
    for x in range(len(document)):
        word = document[x].lower()
        waye = remove_punctuation(word)

        for i in range(len(keyTerms)):
            keyTerm = keyTerms[i]
            keyTerm = keyTerm.strip()

            if word.strip() == keyTerm:
                document[x] = word.upper()
            if waye.strip() == keyTerm:
                document[x] = word.upper()

    return document
def find_USER(document):
    #open keyTerms file

    termsDoc = open("txtFiles/USER.txt", "r")

    keyTerms = termsDoc.readlines()
    termsDoc.close()
    for x in range(len(document)):
        word = document[x].lower()
        waye = remove_punctuation(word)

        for i in range(len(keyTerms)):
            keyTerm = keyTerms[i]
            keyTerm = keyTerm.strip()

            if word.strip() == keyTerm:
                document[x] = word.upper()
            if waye.strip() == keyTerm:
                document[x] = word.upper()

    return document
def find_MICROPHONE(document):
    #open keyTerms file

    termsDoc = open("txtFiles/MICROPHONE.txt", "r")

    keyTerms = termsDoc.readlines()
    termsDoc.close()
    for x in range(len(document)):
        word = document[x].lower()
        waye = remove_punctuation(word)

        for i in range(len(keyTerms)):
            keyTerm = keyTerms[i]
            keyTerm = keyTerm.strip()

            if word.strip() == keyTerm:
                document[x] = word.upper()
            if waye.strip() == keyTerm:
                document[x] = word.upper()

    return document

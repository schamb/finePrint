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
<<<<<<< HEAD
    termsDoc = open("DATA.txt", "r")
=======
    termsDoc = open("txtFiles/DATA.txt", "r")
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
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
<<<<<<< HEAD
    termsDoc = open("ALL.txt", "r")
=======
    termsDoc = open("txtFiles/ALL.txt", "r")
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
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
<<<<<<< HEAD
    termsDoc = open("LOCATION.txt", "r")
=======
    termsDoc = open("txtFiles/LOCATION.txt", "r")
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
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
<<<<<<< HEAD
    termsDoc = open("BILLING.txt", "r")
=======
    termsDoc = open("txtFiles/BILLING.txt", "r")
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
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
<<<<<<< HEAD
    termsDoc = open("CAMERA.txt", "r")
=======
    termsDoc = open("txtFiles/CAMERA.txt", "r")
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
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
<<<<<<< HEAD
    termsDoc = open("USER.txt", "r")
=======
    termsDoc = open("txtFiles/USER.txt", "r")
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
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
<<<<<<< HEAD
    termsDoc = open("MICROPHONE.txt", "r")
=======
    termsDoc = open("txtFiles/MICROPHONE.txt", "r")
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
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

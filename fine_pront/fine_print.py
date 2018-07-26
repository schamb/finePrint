import string
import finePrintFunctions as fpFxs

def main():
    #open text file
<<<<<<< HEAD
    doc = open("fp.txt", "r")
=======
    doc = open("txtFiles/fp.txt", "r")
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
    docData = doc.read()
    docData = list(docData.split(" "))
    doc.close()

<<<<<<< HEAD
    termsDoc = open("DATA.txt", "r")
    keyTerms = termsDoc.readlines()
    termsDoc.close()
=======
    # termsDoc = open("DATA.txt", "r")
    # keyTerms = termsDoc.readlines()
    # termsDoc.close()
>>>>>>> f7bd6d07a81338e251f1d2262f6325d23877013b
    while True:
        print("DATA\nUSER\nCAMERA\nMICROPHONE\nBILLING\nLOCATION\nALL\nSTOP\n")
        specTerm = input("What would you like to look for? ")
        if specTerm == "DATA":
            poop = fpFxs.find_DATA(docData)
        elif specTerm == "ALL":
            poop = fpFxs.find_ALL(docData)
        elif specTerm == "LOCATION":
            poop = fpFxs.find_LOCATION(docData)
        elif specTerm == "BILLING":
            poop = fpFxs.find_BILLING(docData)
        elif specTerm == "CAMERA":
            poop = fpFxs.find_CAMERA(docData)
        elif specTerm == "USER":
            poop = fpFxs.find_USER(docData)
        elif specTerm == "MICROPHONE":
            poop = fpFxs.find_MICROPHONE(docData)
        elif specTerm == "STOP":
            break

        print(" ".join(poop))
if __name__ == '__main__':
    main()

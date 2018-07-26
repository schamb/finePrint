import string
import finePrintFunctions as fpFxs

def main():
    #open text file
    doc = open("fp.txt", "r")
    docData = doc.read()
    docData = list(docData.split(" "))
    doc.close()

    termsDoc = open("DATA.txt", "r")
    keyTerms = termsDoc.readlines()
    termsDoc.close()
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

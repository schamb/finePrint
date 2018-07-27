#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, jinja2, os, string
from google.appengine.ext import ndb

template_directory = os.path.join(os.path.dirname(__file__),'templates')
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory))

class MainHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

class UserInput(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('addcompany.html')
        self.response.out.write(template.render())

class OutputHandler(webapp2.RequestHandler):
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

        termsDoc = open("cssFiles/txtFiles/DATA.txt", "r")

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

        termsDoc = open("cssFiles/txtFiles/ALL.txt", "r")

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

        termsDoc = open("cssFiles/txtFiles/LOCATION.txt", "r")

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

        termsDoc = open("cssFiles/txtFiles/BILLING.txt", "r")

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

        termsDoc = open("cssFiles/txtFiles/CAMERA.txt", "r")

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

        termsDoc = open("cssFiles/txtFiles/USER.txt", "r")

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

        termsDoc = open("cssFiles/txtFiles/MICROPHONE.txt", "r")

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
    def runPython(data):
        specTerm = data#checkbox data??
        if specTerm == "DATA":
            poop = fpFxs.find_DATA(docData)
        elif specTerm == "allCheck":
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
        print(" ".join(poop))
    def post(self):
        template = jinja_environment.get_template('companyname.html')
        data = self.request.get('userInput')
        name1 = self.request.get('allCheck')
        if name1:
            runPython(name1)
        self.response.out.write(template.render(data = data))

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aboutus.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/addcompany', UserInput),
    ('/companyname', OutputHandler),
    ('/aboutus', AboutUsHandler)
], debug=True)

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
    # user input company Name
    # def UIcompanyName():
    #     if addButton clicked:
    #         companyname.html
    #

    #function to remove punctuation
    def remove_punctuation(self, value):
        result = ""
        for c in value:
            # If char is not punctuation, add it to the result.
            if c not in string.punctuation:
                result += c
        return result

    #funcion for DATA
    def find_DATA(self, document):
        #open keyTerms file

        keyTerms = ["data","metadata","storage","tracking","cookies","share"]
        newDocument = document.split(" ")
        for x in range(len(newDocument)):
            word = newDocument[x].lower()
            waye = self.remove_punctuation(word)

            for i in range(len(keyTerms)):
                keyTerm = keyTerms[i]
                keyTerm = keyTerm.strip()

                if word.strip() == keyTerm:
                    newDocument[x] = word.upper()
                if waye.strip() == keyTerm:
                    newDocument[x] = word.upper()

        return " ".join(newDocument)
    def find_ALL(self, document):
        #open keyTerms file

        keyTerms = ["tracking","location","demographic","billing","sell","selling","data","metadata","storage","tracking","cookies","camera","video","photo","user","contact","information","microphone","audio","share","email","phone","address","collect",
        "gather","how we use", "conditions of use", "opt-out", "delete", "deactivate"]
        newDocument = document.split(" ")
        for x in range(len(newDocument)):
            word = newDocument[x].lower()
            waye = self.remove_punctuation(word)

            for i in range(len(keyTerms)):
                keyTerm = keyTerms[i]
                keyTerm = keyTerm.strip()

                if word.strip() == keyTerm:
                    newDocument[x] = word.upper()
                if waye.strip() == keyTerm:
                    newDocument[x] = word.upper()

        return " ".join(newDocument)
    def find_LOCATION(self, document):
        #open keyTerms file
        keyTerms = ["tracking", "location", "demographic"]
        newDocument = document.split(" ")
        for x in range(len(document)):
            word = document[x].lower()
            waye = self.remove_punctuation(word)

            for i in range(len(keyTerms)):
                keyTerm = keyTerms[i]
                keyTerm = keyTerm.strip()

                if word.strip() == keyTerm:
                    newDocument[x] = word.upper()
                if waye.strip() == keyTerm:
                    newDocument[x] = word.upper()

        return " ".join(newDocument)
    def find_BILLING(self, document):
        #open keyTerms file
        keyTerms = ["billing", "sell", "selling"]
        newDocument = document.split(" ")
        for x in range(len(newDocument)):
            word = newDocument[x].lower()
            waye = self.remove_punctuation(word)

            for i in range(len(keyTerms)):
                keyTerm = keyTerms[i]
                keyTerm = keyTerm.strip()

                if word.strip() == keyTerm:
                    newDocument[x] = word.upper()
                if waye.strip() == keyTerm:
                    newDocument[x] = word.upper()

        return " ".join(newDocument)
    def find_CAMERA(self, document):
        #open keyTerms file
        keyTerms = ["camera", "video", "photo"]
        newDocument = document.split(" ")
        for x in range(len(newDocument)):
            word = newDocument[x].lower()
            waye = self.remove_punctuation(word)

            for i in range(len(keyTerms)):
                keyTerm = keyTerms[i]
                keyTerm = keyTerm.strip()

                if word.strip() == keyTerm:
                    newDocument[x] = word.upper()
                if waye.strip() == keyTerm:
                    newDocument[x] = word.upper()

        return " ".join(newDocument)
    def find_USER(self, document):
        #open keyTerms file

        keyTerms = ["user", "contact", "information", "email", "phone", "address"]
        newDocument = document.split(" ")
        for x in range(len(newDocument)):
            word = newDocument[x].lower()
            waye = self.remove_punctuation(word)

            for i in range(len(keyTerms)):
                keyTerm = keyTerms[i]
                keyTerm = keyTerm.strip()

                if word.strip() == keyTerm:
                    newDocument[x] = word.upper()
                if waye.strip() == keyTerm:
                    newDocument[x] = word.upper()


        return " ".join(newDocument)
    def find_MICROPHONE(self, document):
        #open keyTerms file

        keyTerms = ["microphone", "audio"]
        newDocument = document.split(" ")
        for x in range(len(newDocument)):
            word = newDocument[x].lower()
            waye = self.remove_punctuation(word)

            for i in range(len(keyTerms)):
                keyTerm = keyTerms[i]
                keyTerm = keyTerm.strip()

                if word.strip() == keyTerm:
                    newDocument[x] = word.upper()
                if waye.strip() == keyTerm:
                    newDocument[x] = word.upper()

        return " ".join(newDocument)
    def post(self):
        companyTerms = self.request.get('terms')
        companyName = self.request.get('name')

        #Microphone Check box
        audioCheckBox = self.request.get('audio')
        if audioCheckBox == 'audioCheck':
            new_audio = self.find_MICROPHONE(companyTerms)
        else:
            new_audio = "audio not checked"

<<<<<<< HEAD
        #data check box
        dataCheckbox = self.request.get("dataBox")
        if dataCheckbox == 'dataCheck':
            new_data = self.find_DATA(companyTerms)
        else:
            new_data = "Data not checked"
=======
        # #data check box
        # dataCheckBox = self.request.get('otherstuff')
        # if dataCheckBox == 'otherstuffCheck':
        #     new_stuff = self.find_DATA(data)
        # else:
        #     new_stuff = "Data not checked"
>>>>>>> 4d5d3c0af110dddaef5aa8ed76f9a2e768f3ec46

        #user check box
        userCheckBox = self.request.get("user")
        if userCheckBox == 'userCheck':
            new_all = self.find_USER(companyTerms)
        else:
            new_all = "User not Checked"

        #user check box
        billingCheckBox = self.request.get("billing")
        if billingCheckBox == 'billingCheck':
            new_billing = self.find_BILLING(data)
        else:
            new_billing = "billing not Checked"





        template = jinja_environment.get_template('companyname.html')

<<<<<<< HEAD
        self.response.out.write(template.render(name = companyName, terms = companyTerms, audioWords = new_audio, dataWords = new_data, userWords = new_all))
=======
        self.response.out.write(template.render(data = data, audioWords = new_audio, billingWords = new_billing, userWords = new_user))
>>>>>>> 4d5d3c0af110dddaef5aa8ed76f9a2e768f3ec46

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

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
import webapp2, jinja2, os, string, re
from google.appengine.ext import ndb

template_directory = os.path.join(os.path.dirname(__file__),'templates')
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory))

# home page
class MainHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

# add company page
class UserInput(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('addcompany.html')
        self.response.out.write(template.render())

# company name page whth highlighted words
class OutputHandler(webapp2.RequestHandler):
    # user input company Name
    # def UIcompanyName():
    #     if addButton clicked:
    #         companyname.html

    #function to remove punctuation
    def remove_punctuation(self, value):
        result = ""
        for c in value:
            # If char is not punctuation, add it to the result.
            #check if charecters are not in the alphebet
            if c not in string.punctuation:
                result += c
        return result

    #funcion for finding DATA words
    def find_DATAINFO(self, document):
        #open keyTerms file

        keyTerms = ["metadata","data","storage","tracking","cookies","share"]
        document = document.lower()

        #find if the terms in list match a term in the document and change it to uppercase
        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    # function for finding ALL keywords
    def find_ALL(self, document):
        #open keyTerms file
        #keyterms for DATA
        keyTerms = ["tracking","location","demographic","billing","selling","sell","metadata","data","storage","cookies","camera","video","photo","users","user","contact information","microphone","audio","share","email address","phone number","collected", "collects","collect",
        "gather","how we use", "conditions of use", "opt-out", "delete", "deactivates","deactivate", "third-party"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    # function for finding LOCATION key words
    def find_LOCATION(self, document):
        #open keyTerms file
        keyTerms = ["tracking", "location", "demographic"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    # function for finding BILLING key words
    def find_BILLING(self, document):
        #open keyTerms file
        keyTerms = ["billing", "selling", "sell"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    # function for finding CAMERA key words
    def find_CAMERA(self, document):
        #open keyTerms file
        keyTerms = ["camera", "video", "photo"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_USER(self, document):
        #open keyTerms file

        keyTerms = ["users", "user","user information", "contact information", "email address", "email", "phone number", "address"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]


        return document
    def find_MICROPHONE(self, document):
        #open keyTerms file

        keyTerms = ["microphone", "audio"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def post(self):
        #getting results from the user input (checkbox)
        companyTerms = self.request.get('terms')
        companyName = self.request.get('name')
        audioCheckBox = self.request.get('audio')
        dataCheckbox = self.request.get('dataInfo')
        userCheckBox = self.request.get('user')
        billingCheckBox = self.request.get('billing')
        allCheckBox = self.request.get('all')
        cameraCheckBox = self.request.get('camera')
        locationCheckBox = self.request.get('location')
        color = self.request.get('color')
        # self.request.get_all('allCheckboxes')

        #Microphone Check box
        if audioCheckBox:
            new_audio = self.find_MICROPHONE(companyTerms)
            new_audio = new_audio.replace('"', '')
            new_audio = new_audio.replace('"', '')
            new_audio = new_audio.replace('\r\n', '')
        else:
            new_audio = ""
        #data check box
        if dataCheckbox:
            new_dataInfo = self.find_DATAINFO(companyTerms)
            new_dataInfo = new_dataInfo.replace('"', '')
            new_dataInfo = new_dataInfo.replace('"', '')
            new_dataInfo = new_dataInfo.replace('\r\n', '')
        else:
            new_dataInfo = ""
        #user check box
        if userCheckBox:
            new_user = self.find_USER(companyTerms)
            new_user = new_user.replace('"', '')
            new_user = new_user.replace('"', '')
            new_user = new_user.replace('\r\n', '')
        else:
            new_user = ""

        #billing check box
        if billingCheckBox:
            new_billing = self.find_BILLING(companyTerms)
            new_billing = new_billing.replace('"', '')
            new_billing = new_billing.replace('"', '')
            new_billing = new_billing.replace('\r\n', '')
        else:
            new_billing = ""
        #all check box
        if allCheckBox:
            new_all = self.find_ALL(companyTerms)
            new_all = new_all.replace('"', '')
            new_all = new_all.replace('"', '')
            new_all = new_all.replace('\r\n', ' ')
        else:
            new_all = ""
        #location check box
        if locationCheckBox:
            new_location = self.find_LOCATION(companyTerms)
            new_location = new_location.replace('"', '')
            new_location = new_location.replace('"', '')
            new_location = new_location.replace('\r\n', '')
        else:
            new_location = ""
        #camera check box
        if cameraCheckBox:
            new_camera = self.find_CAMERA(companyTerms)
            new_camera = new_camera.replace('"', '')
            new_camera = new_camera.replace('"', '')
            new_camera = new_camera.replace('\r\n', '')
        else:
            new_camera = ""





        template = jinja_environment.get_template('companyname.html')
        self.response.out.write(template.render(name = companyName, terms = companyTerms, cameraWords = new_camera, allWords = new_all, locationWords = new_location, audioWords = new_audio, dataWords = new_dataInfo, userWords = new_user, billingWords = new_billing, highlightColor = color))


class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aboutus.html')
        self.response.out.write(template.render())

class TwitterHandler(webapp2.RequestHandler):
    def remove_punctuation(self, value):
        result = ""
        for c in value:
            # If char is not punctuation, add it to the result.
            if c not in string.punctuation:
                result += c
        return result

    #funcion for DATA
    def find_DATAINFO(self, document):
        #open keyTerms file

        keyTerms = ["metadata","data","storage","tracking","cookies","share"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

            return document

    def find_ALL(self, document):
        #open keyTerms file

        keyTerms = ["tracking","location","demographic","billing","selling","sell","metadata","data","storage","cookies","camera","video","photo","user","contact information","microphone","audio","share","email address","phone number","collect",
        "gather","how we use", "conditions of use", "opt-out", "delete", "deactivate"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_LOCATION(self, document):
        #open keyTerms file
        keyTerms = ["tracking", "location", "demographic"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_BILLING(self, document):
        #open keyTerms file
        keyTerms = ["billing", "selling", "sell"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_CAMERA(self, document):
        #open keyTerms file
        keyTerms = ["camera", "video", "photo"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_USER(self, document):
        #open keyTerms file

        keyTerms = ["user","user information", "contact information", "email address", "phone number", "address", "email"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_MICROPHONE(self, document):
        #open keyTerms file

        keyTerms = ["microphone", "audio"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def post(self):
        companyTerms = self.request.get('terms')
        companyName = self.request.get('name')


        audioCheckBox = self.request.get('audio')
        dataCheckbox = self.request.get('dataInfo')
        userCheckBox = self.request.get('user')
        billingCheckBox = self.request.get('billing')
        allCheckBox = self.request.get('all')
        cameraCheckBox = self.request.get('camera')
        locationCheckBox = self.request.get('location')
        # self.request.get_all('allCheckboxes')

        #Microphone Check box
        if audioCheckBox:
            new_audio = self.find_MICROPHONE(companyTerms)
        else:
            new_audio = ""
        #data check box
        if dataCheckbox:
            new_dataInfo = self.find_DATAINFO(companyTerms)
        else:
            new_dataInfo = ""
        #user check box
        if userCheckBox:
            new_user = self.find_USER(companyTerms)
        else:
            new_user = ""

        #billing check box
        if billingCheckBox:
            new_billing = self.find_BILLING(companyTerms)
        else:
            new_billing = ""
        #all check box
        if allCheckBox:
            new_all = self.find_ALL(companyTerms)
        else:
            new_all = ""
        #location check box
        if locationCheckBox:
            new_location = self.find_LOCATION(companyTerms)
        else:
            new_location = ""
        #camera check box
        if cameraCheckBox:
            new_camera = self.find_CAMERA(companyTerms)
        else:
            new_camera = ""





        template = jinja_environment.get_template('twitter.html')
        self.response.out.write(template.render(name = companyName, terms = companyTerms, cameraWords = new_camera, allWords = new_all, locationWords = new_location, audioWords = new_audio, dataWords = new_dataInfo, userWords = new_user, billingWords = new_billing))

class FacebookHandler(webapp2.RequestHandler):
    def remove_punctuation(self, value):
        result = ""
        for c in value:
            # If char is not punctuation, add it to the result.
            if c not in string.punctuation:
                result += c
        return result

    #funcion for DATA
    def find_DATAINFO(self, document):
        #open keyTerms file

        keyTerms = ["metadata","data","storage","tracking","cookies","share"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

            return document

    def find_ALL(self, document):
        #open keyTerms file

        keyTerms = ["tracking","location","demographic","billing","selling","sell","metadata","data","storage","cookies","camera","video","photo","user","contact information","microphone","audio","share","email address","phone number","collect",
        "gather","how we use", "conditions of use", "opt-out", "delete", "deactivate"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_LOCATION(self, document):
        #open keyTerms file
        keyTerms = ["tracking", "location", "demographic"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_BILLING(self, document):
        #open keyTerms file
        keyTerms = ["billing", "selling", "sell"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_CAMERA(self, document):
        #open keyTerms file
        keyTerms = ["camera", "video", "photo"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_USER(self, document):
        #open keyTerms file

        keyTerms = ["user","user information", "contact information", "email address", "phone number", "address", "email"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def find_MICROPHONE(self, document):
        #open keyTerms file

        keyTerms = ["microphone", "audio"]
        document = document.lower()

        for keyTerm in keyTerms:
            for match in re.finditer(keyTerm, document):
                start = match.start()
                end = start + len(keyTerm)
                document = document[:start] + document[start:end].upper() + document[end:]

        return document
    def post(self):
        companyTerms = self.request.get('terms')
        companyName = self.request.get('name')


        audioCheckBox = self.request.get('audio')
        dataCheckbox = self.request.get('dataInfo')
        userCheckBox = self.request.get('user')
        billingCheckBox = self.request.get('billing')
        allCheckBox = self.request.get('all')
        cameraCheckBox = self.request.get('camera')
        locationCheckBox = self.request.get('location')
        # self.request.get_all('allCheckboxes')

        #Microphone Check box
        if audioCheckBox:
            new_audio = self.find_MICROPHONE(companyTerms)
        else:
            new_audio = ""
        #data check box
        if dataCheckbox:
            new_dataInfo = self.find_DATAINFO(companyTerms)
        else:
            new_dataInfo = ""
        #user check box
        if userCheckBox:
            new_user = self.find_USER(companyTerms)
        else:
            new_user = ""

        #billing check box
        if billingCheckBox:
            new_billing = self.find_BILLING(companyTerms)
        else:
            new_billing = ""
        #all check box
        if allCheckBox:
            new_all = self.find_ALL(companyTerms)
        else:
            new_all = ""
        #location check box
        if locationCheckBox:
            new_location = self.find_LOCATION(companyTerms)
        else:
            new_location = ""
        #camera check box
        if cameraCheckBox:
            new_camera = self.find_CAMERA(companyTerms)
        else:
            new_camera = ""





        template = jinja_environment.get_template('facebook.html')
        self.response.out.write(template.render(name = companyName, terms = companyTerms, cameraWords = new_camera, allWords = new_all, locationWords = new_location, audioWords = new_audio, dataWords = new_dataInfo, userWords = new_user, billingWords = new_billing))

class InstagramHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('instagram.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/addcompany', UserInput),
    ('/companyname', OutputHandler),
    ('/aboutus', AboutUsHandler),
    ('/twitter', TwitterHandler),
    ('/facebook', FacebookHandler),
    ('/instagram', InstagramHandler)



], debug=True)

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
import webapp2, jinja2, os
from google.appengine.ext import ndb

template_directory = os.path.join(os.path.dirname(__file__),'templates')
jinja_environment = jinja2.Enviornment(loader = jinja2.FilsSystemLoader(template_directory))

class User(ndb.Model):
    privacy_policy = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class UserInput(webapp.RequestHandler):
    def post(self):
        template = jinja_environment.get_template('addcompany.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

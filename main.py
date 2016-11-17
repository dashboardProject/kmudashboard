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
import webapp2

from configs import JINJA_ENV
from controller.sign import Sign_In, Sign_Up
from utils.decorators import userCheck

@userCheck
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')

        temp = self.request.get('contents1')
        if temp == 'qwer':
            self.redirect('/test')

        self.response.write(JINJA_ENV.get_template('main.html').render())

    def post(self):
        temp = self.request.get('contents1')
        if temp == 'qwer':
            self.redirect('/test')

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/signin', Sign_In),
                               ('/signup', Sign_Up)],
                              debug=True)

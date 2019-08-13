import webapp2
import jinja2
import os


jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/main.html")
        self.response.write(start_template.render())

class Dog_Shelter(webapp2.RequestHandler):
    def get(self):
        shelter_template = jinja_current_dir.get_template("templates/shelter.html")
        self.response.write(shelter_template.render())

class About_page(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_current_dir.get_template("templates/about.html")
        self.response.write(about_template.render())

class Breed_tab(webapp2.RequestHandler):
    def get(self):
        breed_template = jinja_current_dir.get_template("templates/breed.html")
        self.response.write(breed_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/shelter', Dog_Shelter),
    ('/about', About_page),
    ('/breed',Breed_tab)
], debug=True)

from auth import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        self.template_name = 'home.html'
        self.render_template()

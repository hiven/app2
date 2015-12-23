import webapp2
from config import config

routes = []

home_routes = [
    webapp2.Route('/', 'home.MainHandler', name='home'),
]

auth_routes = [
    webapp2.Route('/auth/signup', 'auth.SignupHandler', name='signup'),
    webapp2.Route('/auth/<type:v|p>/<user_id:\d+>-<signup_token:.+>', handler='auth.VerificationHandler', name='verification'),
    webapp2.Route('/auth/password', 'auth.SetPasswordHandler', name='set_password'),
    webapp2.Route('/auth/login', 'auth.LoginHandler', name='login'),
    webapp2.Route('/auth/logout', 'auth.LogoutHandler', name='logout'),
    webapp2.Route('/auth/forgot', 'auth.ForgotPasswordHandler', name='forgot'),
    webapp2.Route('/auth/authenticated', 'auth.AuthenticatedHandler', name='authenticated')
]

routes += home_routes
routes += auth_routes

app = webapp2.WSGIApplication(routes, debug=config.get('debug'), config=config)

from flask import redirect, request, session
from flask.ext.classy import FlaskView, route

from machete.templating import render
from machete.users.models import User

@route('/login')
class LoginView(FlaskView):

    def get(self):
        return render('login.mako')

    def post(self):
        """
        login route

        POST params:
            email: the email to login with
            password: the password to login with
        :return:
        """
        if 'email' in request.form and 'password' in request.form:
            user = User.get_by_email(request.form.get('email'))
            if user.authenticate(request.form.get('password')):
                session.save()
                session.user = user
                return redirect('/')
        return render('login.mako')

@route('/logout')
class LogoutView(FlaskView):

    def get(self):
        session.user = None
        return redirect('/')

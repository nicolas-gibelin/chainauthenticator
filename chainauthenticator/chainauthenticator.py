import re
import sys

from jupyterhub.auth import Authenticator, LocalAuthenticator
from tornado import gen
from traitlets import List, Instance, Type, Any
from importlib import import_module

class ChainAuthenticator(LocalAuthenticator):

    # Grab this from constructor args in case some Authenticator ever wants it
    config = Any()

    authenticators = List(
        trait=Type(Authenticator),
        config=True,
        help="""
        A list of authenticators

        """
    )

    def _import(self, name):
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        password = data['password']

        print("Chain Auth")

        # No empty passwords!
        if password is None or password.strip() == '':
            self.log.warn('username:%s Login denied for blank password', username)
            return None

        for auth_class in self.authenticators:
            auth = auth_class()
            print(auth)
            # Needed to pass config to authenticator
            auth.config = self.config
            res = yield auth.authenticate(handler, data)
            if res is not None:
                print("Result", res)
                return res

        return None

    @gen.coroutine
    def add_user(self, user):
        """Hook called whenever a new user is added

        """
        yield gen.maybe_future(super().add_user(user))

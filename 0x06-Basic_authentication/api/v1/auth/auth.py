#!/usr/bin/env python3
""" Module of auth
"""
import re
from flask import request
from typing import List, TypeVar


class Auth():
    """ class auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth method """
        if path and excluded_paths:
              if path[-1] != '/':
                    path += '/'
              for route in excluded_paths:

                    path = path.replace('/', '')
                    route = route.replace('/', '')

                    if pth[-1] == '*':
                        pth = pth.replace('*', '.*')

                    if re.search(pth, path):
                        return False

          return True

    def authorization_header(self, request=None) -> str:
        """ auth header method """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        return None

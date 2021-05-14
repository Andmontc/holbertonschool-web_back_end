#!/usr/bin/env python3
""" Module of auth
"""

from flask import request


class Auth:
    """ class auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth method """
        return False

    def authorization_header(self, request=None) -> str:
        """ auth header method """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        return None

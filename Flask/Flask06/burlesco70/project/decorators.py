from functools import wraps
from flask import g
from .errors import forbidden
from project.ruoli.models import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Permessi insufficienti')
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):    
    return permission_required(Permission.ADMIN)(f)

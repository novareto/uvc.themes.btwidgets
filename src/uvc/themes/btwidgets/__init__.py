# this is a package.

import os.path
from dolmen.template import TALTemplate

try:
    from cromlech.browser import ITypedRequest as ISkin
except ImportError:
    from zope.interface import Interface as ISkin


TEMPLATES = os.path.join(os.path.dirname(__file__), 'templates')


def getTemplate(path):
    return TALTemplate(os.path.join(TEMPLATES, path))


class IBootstrapRequest(ISkin):
    pass
    

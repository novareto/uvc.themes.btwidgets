
try:
    from cromlech.browser import ITypedRequest as ISkin
except ImportError:
    from zope.interface import Interface as ISkin


class IBootstrapRequest(ISkin):
    pass

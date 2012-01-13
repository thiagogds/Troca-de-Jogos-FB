# coding: utf-8
from logging import getLogger, LoggerAdapter


def _format_dict(var, tabindent=1):
    # Do nothing if received non-dict
    if not isinstance(var, dict):
        return var

    dict_ = var # Just a better name
    keys = sorted(dict_.keys())

    lines = ['{']

    for k in keys:
        line = "%s%s: %s," % ('\t' * tabindent, repr(k), repr(dict_[k]))
        lines.append(line)

    lines.append('%s},' % ('\t' * (tabindent - 1)))

    return '\n'.join(lines)


def getRequestLogger(name):
    """Returns a logger aware of HttpRequest attributes"""
    return RequestLoggerAdapter(getLogger(name), {})


class RequestLoggerAdapter(LoggerAdapter):
    message = u'\n\t%(method)s %(path)s\n\tHEADERS: %(META)s\n\tDATA: %(POST)s\n\tCOOKIES: %(COOKIES)s'

    def _requestProperties(self, request):
        properties = {
            u'POST'   : _format_dict(request.POST, 2),
            u'COOKIES': _format_dict(request.COOKIES, 2),
            u'META'   : _format_dict(request.META, 2),
            u'method' : request.method,
            u'path'   : request.path,
        }
        return properties

    def process(self, msg, kwargs):
        request = kwargs.pop('request', {})
        if request:
            params = self._requestProperties(request)
            msg += self.message % params

        return msg, kwargs

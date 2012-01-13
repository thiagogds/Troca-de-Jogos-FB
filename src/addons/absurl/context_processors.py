from django.conf import settings
from django.db.models import Count


def absurl(request):
    scheme = request.is_secure() and 'https' or 'http'
    hostname = request.get_host()
    return { '_ABSURL': '%s://%s' % (scheme, hostname) }

from urlparse import urljoin

from django.template import Library
from django.template.defaulttags import URLNode, url
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import iri_to_uri
from django.contrib.sites.models import Site
from django.db.models import get_app


register = Library()

class AbsoluteURLNode(URLNode):
    def _get_baseurl(self, context):
        baseurl = None

        if '_ABSURL' in context:
            baseurl = context['_ABSURL']
        elif get_app('sites', emptyOK=True):
            baseurl = u'http://' + Site.objects.get_current().domain
        else:
            raise ImproperlyConfigured('ABSURL demands a Context Processor OR the django.contrib.sites app. Pick one!')

        return baseurl

    def _get_path(self, context):
        path = super(AbsoluteURLNode, self).render(context)

        if self.asvar:
            path = context[self.asvar]

        return path

    def render(self, context):
        baseurl = self._get_baseurl(context)
        path = self._get_path(context)

        url = iri_to_uri(urljoin(baseurl, path))

        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url

def absurl(parser, token):
    """Just like {% url %} but ads the domain of the current site."""
    # invoke url setup just to parse the arguments.
    node = url(parser, token)
    # then pass the parsed args to the actual node instance
    return AbsoluteURLNode(view_name=node.view_name,
                           args=node.args,
                           kwargs=node.kwargs,
                           asvar=node.asvar)

register.tag('absurl', absurl)

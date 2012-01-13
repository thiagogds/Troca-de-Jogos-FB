from django.test import TestCase, RequestFactory
from django.template import Template, RequestContext, TemplateSyntaxError
from django.conf import settings

from lib.settingsmanager import TestSettingsManager
import urls as dummy_urlconf


class AbsurlBaseTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(AbsurlBaseTest, self).__init__(*args, **kwargs)
        self.settings_manager = TestSettingsManager()

    def tearDown(self):
        self.settings_manager.revert()

class AbsurlWithContextProcessorTest(AbsurlBaseTest):
    def setUp(self):
        self.settings_manager.set(ROOT_URLCONF=dummy_urlconf)
        self.settings_manager.append('TEMPLATE_CONTEXT_PROCESSORS', 'lib.absurl.context_processors.absurl')
        self.settings_manager.filter('INSTALLED_APPS', 'django.contrib.sites')

        rf = RequestFactory()
        self.context = RequestContext(rf.get('/'), {})

    def test_success(self):
        self.assertFalse('django.contrib.sites' in settings.INSTALLED_APPS)
        self.assertTrue('lib.absurl.context_processors.absurl' in settings.TEMPLATE_CONTEXT_PROCESSORS)

        t = Template('{% load absurl %}{% absurl dummy_url "THISISAHASH" %}')
        self.assertEqual('http://testserver/dummy-url/THISISAHASH/', t.render(self.context))


class AbsurlWithSitesAppTest(AbsurlBaseTest):
    def setUp(self):
        self.settings_manager.set(ROOT_URLCONF=dummy_urlconf)
        self.settings_manager.filter('TEMPLATE_CONTEXT_PROCESSORS', 'context_processors.absurl')
        self.settings_manager.append('INSTALLED_APPS', 'django.contrib.sites')

        rf = RequestFactory()
        self.context = RequestContext(rf.get('/'), {})

        from django.contrib.sites.models import Site
        if not Site.objects.exists():
            Site.objects.create(domain='example.com', name='example.com')

    def test_success(self):
        self.assertTrue('django.contrib.sites' in settings.INSTALLED_APPS)
        self.assertFalse('lib.absurl.context_processors.absurl' in settings.TEMPLATE_CONTEXT_PROCESSORS)

        t = Template('{% load absurl %}{% absurl dummy_url "THISISAHASH" %}')
        self.assertEqual('http://example.com/dummy-url/THISISAHASH/', t.render(self.context))


class AbsurlContextProcessorPreceedsSitesApp(AbsurlBaseTest):
    def setUp(self):
        self.settings_manager.set(ROOT_URLCONF=dummy_urlconf)
        self.settings_manager.append('INSTALLED_APPS', 'django.contrib.sites')
        self.settings_manager.append('TEMPLATE_CONTEXT_PROCESSORS', 'lib.absurl.context_processors.absurl')

        rf = RequestFactory()
        self.context = RequestContext(rf.get('/'), {})

    def test_success(self):
        self.assertTrue('django.contrib.sites' in settings.INSTALLED_APPS)
        self.assertTrue('lib.absurl.context_processors.absurl' in settings.TEMPLATE_CONTEXT_PROCESSORS)

        t = Template('{% load absurl %}{% absurl dummy_url "THISISAHASH" %}')
        self.assertEqual('http://testserver/dummy-url/THISISAHASH/', t.render(self.context))


class AbsurlImproperlyConfiguredTest(AbsurlBaseTest):
    def setUp(self):
        self.settings_manager.set(ROOT_URLCONF=dummy_urlconf)
        self.settings_manager.set(TEMPLATE_CONTEXT_PROCESSORS=tuple())
        self.settings_manager.filter('INSTALLED_APPS', 'django.contrib.sites')

        rf = RequestFactory()
        self.context = RequestContext(rf.get('/'), {})

    def test_improperly_configured(self):
        self.assertFalse('django.contrib.sites' in settings.INSTALLED_APPS)
        self.assertFalse('lib.absurl.context_processors.absurl' in settings.TEMPLATE_CONTEXT_PROCESSORS)

        t = Template('{% load absurl %}{% absurl dummy_url "THISISAHASH" %}')
        self.assertRaises(TemplateSyntaxError, lambda: t.render(self.context))

from zope.interface import Interface, implements, Attribute
from zope.browser.interfaces import IBrowserView
from Products.Five.browser import BrowserView
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IResultsRenderer(IBrowserView):
    """Interface for results renderer."""

    title = Attribute(u"Displayable name of the template")

    def __call__(self, results):
        """Render results."""

class DefaultResultsRenderer(BrowserView):
    """Default results list renderer."""

    title = _(u"Default template")

    implements(IResultsRenderer)

    template = ViewPageTemplateFile('renderer.pt')

    def __call__(self, results):
        """Render results."""
        return self.template(results=results)

class AlternativeResultsRenderer(DefaultResultsRenderer):
    """Alternative list renderer."""
    
    title = _(u"No links template")

    template = ViewPageTemplateFile('alternative.pt')

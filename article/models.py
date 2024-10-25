from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class ArticlePage(Page):
    parent_page_type = ['home.HomePage']
    subpage_types = []

    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [     
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
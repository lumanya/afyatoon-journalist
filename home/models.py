from django.db import models

from wagtail.models import Page


class HomePage(Page):
    subpage_types = ['article.ArticlePage']


 
    

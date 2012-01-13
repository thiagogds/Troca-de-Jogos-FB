#-*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from userena.models import UserenaBaseProfile

from app.core.models import Game

class Profile(UserenaBaseProfile):

    user = models.OneToOneField(User,
                                    unique=True,
                                    verbose_name=_('user'),
                                    related_name='my_profile')

    games = models.ManyToManyField(Game, through='Trade')

    class Meta:
        verbose_name = _(u'Profile')

class Trade(models.Model):
    profile = models.ForeignKey(Profile)
    game = models.ForeignKey(Game)
    tradable = models.BooleanField(_('Trocavel'))

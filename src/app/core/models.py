#-*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Game(models.Model):

    ADVENTURE    = u"ADV"
    ACTION       = u"ACT"
    BASKETBALL   = u"BKT"
    CAR_COMBAT   = u"CRC"
    RACE         = u"RAC"
    RTS          = u"RTS"
    TBS          = u"TBS"
    FOOTBALL     = u"FTB"
    GOLF         = u"GLF"
    FIGHTING     = u"FGT"
    OTHER        = u"OTR"
    OTHER_SPORTS = u"OTS"
    PARTY        = "PTY"
    PLATAFORM    = u"PLT"
    PUZZLE       = u"PZL"
    RPG          = u"RPG"
    MUSIC        = u"MSC"
    SIMULATOR    = u"SIM"
    FPS          = u"FPS"
    TPS          = u"TPS"

    GENRE_CHOICES = (
        (ADVENTURE, _(u"Aventura")),
        (ACTION, _(u"Ação")),
        (BASKETBALL, _(u"Basquete")),
        (CAR_COMBAT, _(u"Batalha de carros")),
        (RACE, _(u"Corrida")),
        (RTS, _(u"Estratégia em tempo real")),
        (TBS, _(u"Estratégia em turnos")),
        (FOOTBALL, _(u"Futebol")),
        (GOLF, _(u"Golf")),
        (FIGHTING, _(u"Luta")),
        (OTHER, _(u"Outros")),
        (OTHER_SPORTS, _(u"Outros Esportes")),
        (PARTY, _(u"Party Games")),
        (PLATAFORM, _(u"Plataforma")),
        (PUZZLE, _(u"Puzzle")),
        (RPG, _(u"RPG")),
        (MUSIC, _(u"Ritmo musical")),
        (SIMULATOR, _(u"Simulador")),
        (FPS, _(u"Tiro em primeira pessoa")),
        (TPS, _(u"Tiro em terceira pessoa")),
    )

    name = models.CharField(_(u'Nome'), max_length=100)
    cover = models.CharField(_(u'Capa'), max_length=200)
    genre = models.CharField(_(u'Gênero'), max_length=3, choices=GENRE_CHOICES)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Jogo')
        verbose_name_plural = _(u'Jogos')



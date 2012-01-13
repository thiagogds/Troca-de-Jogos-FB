from django.contrib import admin
from models import Game

from addons.decorators import admin_attrs

class GameAdmin(admin.ModelAdmin):
    list_display = ['cover_image', 'name']

    @admin_attrs(allow_tags=True, short_description=u"Capa", admin_order_field=u"cover")
    def cover_image(self, obj):
        return "<img src='%s' style='max-width: 200px;'>" % (obj.cover)

admin.site.register(Game, GameAdmin)

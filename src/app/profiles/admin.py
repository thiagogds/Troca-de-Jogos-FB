from django.contrib import admin

from models import Trade

class TradeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trade, TradeAdmin)


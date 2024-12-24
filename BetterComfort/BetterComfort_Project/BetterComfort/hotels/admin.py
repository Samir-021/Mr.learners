from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *
from django.contrib.admin import ModelAdmin, register

# Change the admin site header and title
admin.site.site_header = _("BetterComfort Administration")
admin.site.site_title = _("BetterComfort Admin Portal")
admin.site.index_title = _("Welcome to BetterComfort Admin")

admin.site.register(HotelRestro)
admin.site.register(FavoriteHotel)
admin.site.register(Review)
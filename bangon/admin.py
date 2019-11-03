from django.contrib import admin
from bangon import models

# Register your models here.
admin.site.register(models.City)
admin.site.register(models.Area)
admin.site.register(models.Item)
admin.site.register(models.Donation)
admin.site.register(models.DonationItem)

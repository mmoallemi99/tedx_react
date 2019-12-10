from django.contrib import admin

from .models import (
    # Event,
    Staff,
    Speaker,
    Sponsor
)

# admin.site.register(Event)
admin.site.register(Staff)
admin.site.register(Speaker)
admin.site.register(Sponsor)


from django.contrib import admin

from .models import (
    # Event,
    Staff,
    Speaker,
    Sponsor,
    Attendee,
)

# admin.site.register(Event)
admin.site.register(Staff)
admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Attendee)


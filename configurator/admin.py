from django.contrib import admin
from .models import (
    ButtonBody,
    ContactType,
    ButtonBodyContactType,
    IlluminationColor,
    IlluminationVoltage,
    SurroundType,
    SurroundColor,
    SurroundForm
)

admin.site.register(ButtonBody)
admin.site.register(ContactType)
admin.site.register(ButtonBodyContactType)
admin.site.register(IlluminationColor)
admin.site.register(IlluminationVoltage)
admin.site.register(SurroundType)
admin.site.register(SurroundColor)
admin.site.register(SurroundForm)

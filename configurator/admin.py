from django.contrib import admin
from .models import (
    ButtonBody,
    ContactType,
    IlluminationColor,
    IlluminationVoltage,
    SurroundType,
    SurroundColor,
    SurroundForm,
    Pressel,
    PresselType,
    PresselLegend,
    PresselFinish,
    PresselPolycarbonateColour
)

admin.site.register(ButtonBody)
admin.site.register(ContactType)
admin.site.register(IlluminationColor)
admin.site.register(IlluminationVoltage)
admin.site.register(SurroundType)
admin.site.register(SurroundColor)
admin.site.register(SurroundForm)
admin.site.register(Pressel)
admin.site.register(PresselType)
admin.site.register(PresselLegend)
admin.site.register(PresselFinish)
admin.site.register(PresselPolycarbonateColour)

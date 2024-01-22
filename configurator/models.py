from django.db import models


class ButtonBody(models.Model):
    body_code = models.CharField(max_length=5)
    body = models.CharField(max_length=50)

    def __str__(self):
        return self.body


class ContactType(models.Model):
    contact_code = models.CharField(max_length=5)
    contact = models.CharField(max_length=50)
    body_type = models.ManyToManyField(ButtonBody, related_name='contact_types')

    def __str__(self):
        return self.contact


class IlluminationColor(models.Model):
    led_code = models.CharField(max_length=5)
    led_color = models.CharField(max_length=50)

    def __str__(self):
        return self.led_color


class IlluminationVoltage(models.Model):
    volt_code = models.CharField(max_length=5)
    voltage = models.CharField(max_length=50)
    led_colors = models.ManyToManyField(IlluminationColor, related_name="led_voltages")

    def __str__(self):
        return self.voltage


class SurroundType(models.Model):
    surround_code = models.CharField(max_length=5)
    surround = models.CharField(max_length=50)

    def __str__(self):
        return self.surround


class SurroundColor(models.Model):
    sur_color_code = models.CharField(max_length=5)
    surround_color = models.CharField(max_length=50)

    def __str__(self):
        return self.surround_color


class SurroundForm(models.Model):
    form_code = models.CharField(max_length=5)
    surround_form = models.CharField(max_length=50)

    def __str__(self):
        return self.surround_form


class Pressel(models.Model):
    type = models.CharField(max_length=10)
    legend = models.CharField(max_length=40)
    pressel_stock_code = models.CharField(max_length=20)
    pressel_finish = models.CharField(max_length=20)
    polycarbonate_colour = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.type}'


class PresselType(models.Model):
    pressel_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.pressel_type}'


class PresselLegend(models.Model):
    legend = models.CharField(max_length=40)
    types = models.ManyToManyField(PresselType, related_name='legends')

    def __str__(self):
        return f'{self.legend}'


class PresselFinish(models.Model):
    pressel_finish = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.pressel_finish}'


class PresselPolycarbonateColour(models.Model):
    polycarbonate_colour = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.polycarbonate_colour}'

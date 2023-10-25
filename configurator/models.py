from django.db import models


class ButtonBody(models.Model):
    body_code = models.CharField(max_length=5)
    body = models.CharField(max_length=50)

    def __str__(self):
        return self.body


class ContactType(models.Model):
    contact_code = models.CharField(max_length=5)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.contact


class ButtonBodyContactType(models.Model):
    button_body = models.ForeignKey(ButtonBody, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)


class IlluminationColor(models.Model):
    led_code = models.CharField(max_length=5)
    led_color = models.CharField(max_length=50)

    def __str__(self):
        return self.led_color


class IlluminationVoltage(models.Model):
    volt_code = models.CharField(max_length=5)
    voltage = models.CharField(max_length=50)

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
    shape_code = models.CharField(max_length=5)
    surround_form = models.CharField(max_length=50)

    def __str__(self):
        return self.surround_form

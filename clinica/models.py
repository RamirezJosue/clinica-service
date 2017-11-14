from django.db import models

# Create your models here.


class Paciente(models.Model):

    codigo = models.CharField(max_length=60)
    tipo_sangre = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return '%s' % (self.codigo)

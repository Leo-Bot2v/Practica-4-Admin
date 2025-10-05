from django.db import models

# Create your models here.
class Faculty(models.Model):
    nombrefacultad = models.CharField(max_length=100)
    cod_facultad = models.CharField(max_length=20)
    ubicación = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='facultad_fotos/', null=True, blank= True)

    def __str__(self):
        return self.nombrefacultad
    
class Meta:
    verbose_name = "Facultad"
    verbose_name_plural = "Facultades"
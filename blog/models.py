from django.conf import settings
from django.db import models
from django.utils import timezone

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Este objeto es el que se encarga de los post del 
# blog que conta: 
# 
# "Autor (author)" 
# "Titulo (title)"
# "Contenido (text)"
# "Fecha de creación (created_date)"
# "Fecha de publicación (published_date)" 
# 
# y de una función publish() para hacer publico el post
# 
# .
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Esto va a sacar la fecha y hora de la horra actual 
    # y para poder hacer eso nesesita saber cual es tu uso 
    # horarios. 
    # 
    # En el archivo "./tutorial_djangogrirls_org/settings.py" 
    # existe una constante llamada "TIME_ZONE" que se ve
    # mas o menos asi "TIME_ZONE = 'UTC'" se configura que
    # uso horarios es el actual (en el ese caso UTC)
    # 
    # Podrias poner cualquier uso orario pero lo idea seria 
    # el horarios de la consta este (US), el uso horario de 
    # del meridiano 0 grados o el de Japon (Tokio) que serian
    # los tres usos orarios que nos podrian llegar a interesar en 
    # este caso.
    #
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    # 
    # .
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
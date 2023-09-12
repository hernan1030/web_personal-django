from django.db import models


def custom_upload_to(instance, filename):
    if instance.pk:
        try:
            old_instance = Portfolio.objects.get(pk=instance.pk)
            old_instance.image.delete()
            print(old_instance.image)

        except Portfolio.DoesNotExist as e:
            print(f"MENSAJE DE ERRO--------{e}")

    return 'porfolioImg/' + filename

# Create your models here.


class Portfolio(models.Model):

    title = models.CharField(max_length=70, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen",
                              upload_to=custom_upload_to)
    link = models.URLField(verbose_name="Link a proyecto")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contenido"
        ordering = ["-create"]

    def __str__(self) -> str:
        return self.title

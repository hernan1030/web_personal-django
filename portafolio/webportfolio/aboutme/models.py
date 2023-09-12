from django.db import models

# Create your models here.


def custom_upload_to(instance, filename):
    if instance.pk:
        try:
            old_instance = AboutMePerfil.objects.get(pk=instance.pk)
            old_instance.image.delete()
            print(old_instance.image)

        except AboutMePerfil.DoesNotExist as e:
            print(f"MENSAJE DE ERRO--------{e}")

    return 'perfilImg/' + filename


class AboutMePerfil(models.Model):

    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Portada",
                              upload_to=custom_upload_to)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fechade creacion")
    update = models.DateTimeField(
        auto_now=True, verbose_name="fecha de actualizacion")

    class Meta:
        verbose_name = "Perfil"
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title

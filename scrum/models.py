from django.db import models


class Project(models.Model):
    class Meta:
        verbose_name = u"Projeto"
        verbose_name_plural = u"Projetos"

    name = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20, null=True, blank=True)      
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
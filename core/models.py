from django.db import models


class Funcao(models.Model):
    id = models.AutoField(primary_key=True)
    funcao = models.CharField(blank=False, max_length=255)

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funcões'
        ordering = ['id']

    def __str__(self):
        return self.funcao


class Regiao(models.Model):
    id = models.AutoField(primary_key=True)
    nomeregiao = models.CharField(blank=False, max_length=255)
    lore_regiao = models.TextField(blank=False, default='')
    fotoregiao = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'
        ordering = ['id']

    def __str__(self):
        return self.nomeregiao


class Campeao(models.Model):
    id = models.AutoField(primary_key=True)
    campeao = models.CharField(blank=False, max_length=100)
    funcao = models.ForeignKey(Funcao, blank=False, on_delete=models.CASCADE)
    lore = models.TextField(blank=False, default='')
    regiao = models.ForeignKey(Regiao, blank=False, on_delete=models.CASCADE)
    passiva = models.CharField(blank=False, max_length=255)
    descricaopassiva = models.TextField(blank=False, default='')
    skillq = models.CharField(blank=False, max_length=255)
    descricaoskillq = models.TextField(blank=False, default='')
    skillw = models.CharField(blank=False, max_length=255)
    descricaoskillw = models.TextField(blank=False, default='')
    skille = models.CharField(blank=False, max_length=255)
    descricaoskille = models.TextField(blank=False, default='')
    skillr = models.CharField(blank=False, max_length=255)
    descricaoskillr = models.TextField(blank=False, default='')
    descricao = models.CharField(max_length=30)
    foto = models.ImageField()

    class Meta:
        verbose_name = 'Personagem'
        verbose_name_plural = 'Personagens'
        ordering = ['id']

    def __str__(self):
        return self.campeao

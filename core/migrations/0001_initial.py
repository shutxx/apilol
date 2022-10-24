# Generated by Django 4.1.2 on 2022-10-24 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('funcao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Função',
                'verbose_name_plural': 'Funcões',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomeregiao', models.CharField(max_length=255)),
                ('lore_regiao', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Região',
                'verbose_name_plural': 'Regiões',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Campeao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('lore', models.TextField(default='')),
                ('passiva', models.CharField(max_length=255)),
                ('descricaopassiva', models.TextField(default='')),
                ('skillq', models.CharField(max_length=255)),
                ('descricaoskillq', models.TextField(default='')),
                ('skillw', models.CharField(max_length=255)),
                ('descricaoskillw', models.TextField(default='')),
                ('skille', models.CharField(max_length=255)),
                ('descricaoskille', models.TextField(default='')),
                ('skillr', models.CharField(max_length=255)),
                ('descricaoskillr', models.TextField(default='')),
                ('descricao', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='')),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.funcao')),
                ('regiao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.regiao')),
            ],
            options={
                'verbose_name': 'Personagem',
                'verbose_name_plural': 'Personagens',
                'ordering': ['id'],
            },
        ),
    ]
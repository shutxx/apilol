# Generated by Django 4.1.2 on 2022-10-28 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regiao',
            name='fotoregiao',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
# Generated by Django 2.1.1 on 2018-09-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='foto', verbose_name='Imagem'),
        ),
    ]

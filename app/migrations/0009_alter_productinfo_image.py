# Generated by Django 4.0.3 on 2022-03-31 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_productinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/images', verbose_name='image'),
        ),
    ]

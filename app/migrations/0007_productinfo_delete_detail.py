# Generated by Django 4.0.3 on 2022-03-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_detail_alter_product_ingredients_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='productinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures/images', verbose_name='image')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('description', models.TextField(max_length=2000, verbose_name='description')),
            ],
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]

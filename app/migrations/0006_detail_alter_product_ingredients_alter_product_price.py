# Generated by Django 4.0.3 on 2022-03-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_product_image_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures/images', verbose_name='image')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('description', models.CharField(max_length=120, verbose_name='description')),
                ('charges', models.TextField(max_length=300, verbose_name='charges')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(max_length=300, verbose_name='ingredients'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=120, verbose_name='price'),
        ),
    ]

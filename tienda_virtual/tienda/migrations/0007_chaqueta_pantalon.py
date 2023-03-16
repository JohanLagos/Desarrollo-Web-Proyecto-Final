# Generated by Django 4.1.7 on 2023-03-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_rename_ropa_camiseta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chaqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pantalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
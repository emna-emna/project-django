# Generated by Django 3.0.3 on 2020-04-04 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catégorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(db_index=True, max_length=200)),
                ('libellé', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Catégorie ',
                'verbose_name_plural': 'Catégories ',
                'ordering': ('nom',),
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(db_index=True, max_length=200)),
                ('libellé', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stock', models.PositiveIntegerField()),
                ('disponible', models.BooleanField(default=True)),
                ('créé', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('catégorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produit', to='boutique.Catégorie')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ('-créé',),
                'index_together': {('id', 'libellé')},
            },
        ),
    ]

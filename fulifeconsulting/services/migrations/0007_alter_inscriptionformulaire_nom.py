# Generated by Django 4.0 on 2023-07-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_inscriptionformulaire_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscriptionformulaire',
            name='nom',
            field=models.CharField(max_length=150),
        ),
    ]

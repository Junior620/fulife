# Generated by Django 4.0 on 2023-07-02 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_alter_client_contact_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client_contact',
        ),
    ]

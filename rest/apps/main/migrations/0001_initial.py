# Generated by Django 3.0.6 on 2020-05-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restorant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_restorant', models.CharField(max_length=20)),
                ('rescription_restorant', models.CharField(max_length=20)),
            ],
        ),
    ]

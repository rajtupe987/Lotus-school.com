# Generated by Django 4.2.4 on 2023-08-30 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotusedt', '0003_expertise_remove_instructor_expertise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='expertise',
            field=models.ManyToManyField(to='lotusedt.expertise'),
        ),
    ]

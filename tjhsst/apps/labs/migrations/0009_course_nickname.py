# Generated by Django 2.1.7 on 2019-05-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0008_auto_20190513_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='nickname',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]

# Generated by Django 2.1.7 on 2019-05-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20190426_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='club_photos/'),
        ),
        migrations.AlterField(
            model_name='club',
            name='keywords',
            field=models.ManyToManyField(blank=True, related_name='clubs', to='clubs.Keyword'),
        ),
    ]

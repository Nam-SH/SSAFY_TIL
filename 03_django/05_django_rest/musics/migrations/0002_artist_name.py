# Generated by Django 2.2.6 on 2019-10-28 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
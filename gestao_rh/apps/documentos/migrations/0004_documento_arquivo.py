# Generated by Django 3.1 on 2020-08-31 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20200829_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=' ', upload_to='documentos'),
            preserve_default=False,
        ),
    ]
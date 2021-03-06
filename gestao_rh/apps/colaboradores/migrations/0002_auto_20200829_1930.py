# Generated by Django 3.1 on 2020-08-29 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departamentos', '0001_initial'),
        ('empresas', '0001_initial'),
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='departamentos',
            field=models.ManyToManyField(to='departamentos.Departamento'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='empresas.empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colaborador',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
    ]

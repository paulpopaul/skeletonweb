# Generated by Django 3.1 on 2020-11-19 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True, null=True, verbose_name='fecha')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('asunto', models.CharField(max_length=20, verbose_name='Asunto')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('mensaje', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalContacto',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='fecha')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('asunto', models.CharField(max_length=20, verbose_name='Asunto')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('mensaje', models.TextField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Mensaje',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

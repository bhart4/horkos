# Generated by Django 2.2.2 on 2019-10-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_query_auto_update_trailing_revision'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='server_type',
            field=models.CharField(choices=[('mysql', 'MySQL'), ('mssql', 'MSSQL')], default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='query',
            name='database_server',
            field=models.CharField(default='', max_length=2000),
        ),
    ]

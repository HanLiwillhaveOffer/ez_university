# Generated by Django 2.1.1 on 2018-09-23 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('courseinfo', '0002_auto_20180923_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='courseinfo.Semester'),
        ),
    ]

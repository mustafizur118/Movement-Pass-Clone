# Generated by Django 3.1.5 on 2021-05-30 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0003_auto_20210530_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movementpass',
            name='time_spand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='fuser.timespend'),
        ),
    ]

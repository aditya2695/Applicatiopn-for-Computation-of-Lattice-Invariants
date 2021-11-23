# Generated by Django 3.0.5 on 2021-08-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattice', '0003_lattice_2d_data_lattice_3d_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lattice_2d_data',
            old_name='alpha',
            new_name='gamma',
        ),
        migrations.RemoveField(
            model_name='lattice_2d_data',
            name='beta',
        ),
        migrations.RemoveField(
            model_name='lattice_2d_data',
            name='identifier',
        ),
        migrations.AlterField(
            model_name='lattice_2d_data',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.0.4 on 2018-06-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='bureau',
        ),
        migrations.AlterField(
            model_name='demande',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='demande',
            name='host',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='demande',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='demande',
            name='os',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='demande',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='demande',
            name='prenom',
            field=models.CharField(max_length=100),
        ),
    ]

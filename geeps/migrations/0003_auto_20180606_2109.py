# Generated by Django 2.0.4 on 2018-06-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeps', '0002_auto_20180606_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='bureau',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='demande',
            name='email',
            field=models.EmailField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='demande',
            name='nom',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='demande',
            name='phone',
            field=models.CharField(default='Unknown', max_length=10),
        ),
        migrations.AlterField(
            model_name='demande',
            name='prenom',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]

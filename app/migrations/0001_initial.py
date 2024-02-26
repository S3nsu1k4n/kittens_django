# Generated by Django 5.0.2 on 2024-02-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the kitten', max_length=32, verbose_name='Name')),
                ('age', models.IntegerField(help_text='Age of the kitten', verbose_name='Age')),
                ('cuteness', models.IntegerField(help_text='Cuteness of the kitten', verbose_name='Cuteness')),
                ('softness', models.IntegerField(help_text='Softness of the kitten', verbose_name='Softness')),
            ],
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitten',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None, help_text='When the entry was created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kitten',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='When the entry was last updated'),
        ),
    ]

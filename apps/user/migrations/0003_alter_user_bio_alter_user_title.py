# Generated by Django 4.2.4 on 2023-08-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_bio_user_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, help_text='Your profession', max_length=100, null=True),
        ),
    ]

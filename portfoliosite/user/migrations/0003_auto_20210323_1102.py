# Generated by Django 2.1.5 on 2021-03-23 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210226_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, default='...Default About Me text', help_text='Tell us something about you.'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), help_text='Get a cool-sounding alias.', max_length=50, null=True, unique=True, verbose_name='Display Name: '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
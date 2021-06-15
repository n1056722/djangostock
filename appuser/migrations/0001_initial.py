# Generated by Django 2.2.9 on 2021-06-11 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('token', models.CharField(max_length=10)),
                ('secret_key', models.CharField(max_length=20)),
                ('is_enable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AppUserLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('path', models.CharField(max_length=20)),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appuser.AppUser')),
            ],
        ),
    ]
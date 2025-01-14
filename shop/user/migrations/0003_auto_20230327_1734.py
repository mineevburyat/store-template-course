# Generated by Django 3.2 on 2023-03-27 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified_email',
            field=models.BooleanField(default=False, verbose_name='верефикация email'),
        ),
        migrations.CreateModel(
            name='VerifideUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(unique=True, verbose_name='uuid')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('expiration', models.DateTimeField(verbose_name='действует до')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]

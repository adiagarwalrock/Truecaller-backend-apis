# Generated by Django 3.2.6 on 2021-08-27 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_usercontact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='imported_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]

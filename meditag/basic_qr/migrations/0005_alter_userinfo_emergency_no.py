# Generated by Django 3.2.7 on 2021-09-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_qr', '0004_auto_20210906_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='emergency_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

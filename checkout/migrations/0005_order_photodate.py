# Generated by Django 3.2.16 on 2022-11-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='photodate',
            field=models.DateField(blank=True, null=True),
        ),
    ]

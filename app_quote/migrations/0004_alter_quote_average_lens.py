# Generated by Django 3.2.7 on 2022-03-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quote', '0003_auto_20220302_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='average_lens',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
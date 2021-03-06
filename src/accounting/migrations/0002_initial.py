# Generated by Django 3.2.7 on 2021-10-22 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallets', '0001_initial'),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallets.coinwallet', verbose_name='Cuenta'),
        ),
        migrations.CreateModel(
            name='NegativeMovement',
            fields=[
            ],
            options={
                'proxy': (True,),
                'indexes': [],
                'constraints': [],
            },
            bases=('accounting.movement',),
        ),
        migrations.CreateModel(
            name='PositiveMovement',
            fields=[
            ],
            options={
                'proxy': (True,),
                'indexes': [],
                'constraints': [],
            },
            bases=('accounting.movement',),
        ),
    ]

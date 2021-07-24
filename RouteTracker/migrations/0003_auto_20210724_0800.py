# Generated by Django 3.1.2 on 2021-07-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RouteTracker', '0002_route_maxdeparturepow'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='dockedChargingMethod',
            field=models.CharField(choices=[('grid power', 'Grid Power'), ('engine power', 'Engine Power')], default='grid power', max_length=20, null=True, verbose_name='docked charging method'),
        ),
        migrations.AddField(
            model_name='route',
            name='propulsionMethod',
            field=models.CharField(choices=[('full electric', 'Full Electric'), ('hybrid electric', 'Hybrid Electric')], default='full electric', max_length=20, verbose_name='propulsion method'),
        ),
        migrations.AlterField(
            model_name='route',
            name='thresholdPower',
            field=models.IntegerField(blank=True, null=True, verbose_name='Engine Power (kw)'),
        ),
    ]
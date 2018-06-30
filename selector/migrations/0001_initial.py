# Generated by Django 2.0.6 on 2018-06-30 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stake', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_description', models.CharField(max_length=200)),
                ('odds_numerator', models.IntegerField(default=1)),
                ('odds_denominator', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selector.Line'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-22 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breaks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_breaks', models.IntegerField()),
                ('break_type', models.CharField(choices=[('short', 'SHORT'), ('long', 'LONG')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('completed', models.BooleanField()),
                ('break_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Breaks')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='session.UserModel')),
            ],
        ),
    ]

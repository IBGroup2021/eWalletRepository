# Generated by Django 3.1.6 on 2021-03-01 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.transferencia')),
            ],
        ),
    ]
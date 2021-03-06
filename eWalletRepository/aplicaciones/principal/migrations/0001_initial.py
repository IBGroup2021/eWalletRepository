# Generated by Django 3.1.6 on 2021-02-27 18:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('num_cuenta', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('fondos', models.DecimalField(blank=True, decimal_places=3, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=100)),
                ('contraseña_val', models.CharField(max_length=100)),
                ('condicionval', models.BooleanField()),
                ('documento', models.CharField(choices=[('D', 'Dni'), ('P', 'Pasaporte')], max_length=1)),
                ('num_documento', models.CharField(max_length=24)),
                ('telefono', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(regex='^[0-9]{9}$')])),
                ('direccion', models.CharField(max_length=100)),
                ('val_email', models.BooleanField()),
                ('num_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_cuenta', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$')])),
                ('monto', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('validacion', models.BooleanField()),
                ('tipo_trans', models.CharField(choices=[('N', 'Nacionales'), ('E', 'Exteriores')], max_length=1)),
                ('num_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='Retiro',
            fields=[
                ('id_retiro', models.BigAutoField(primary_key=True, serialize=False)),
                ('banco', models.CharField(max_length=50)),
                ('monto', models.FloatField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('nomtitular', models.CharField(max_length=100)),
                ('num_cuenta', models.ForeignKey(db_column='num_cuenta', on_delete=django.db.models.deletion.CASCADE, to='principal.cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialTransferencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('receptor', models.CharField(max_length=24)),
                ('monto', models.PositiveIntegerField()),
                ('Emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.transferencia')),
            ],
        ),
        migrations.CreateModel(
            name='Depositos',
            fields=[
                ('id_deposito', models.BigAutoField(primary_key=True, serialize=False)),
                ('monto', models.FloatField()),
                ('banco', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('nomtitular', models.CharField(max_length=100)),
                ('num_cuenta', models.ForeignKey(db_column='num_cuenta', on_delete=django.db.models.deletion.CASCADE, to='principal.cuenta')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-27 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='estado',
            field=models.CharField(choices=[('AP', 'Amapá'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('ES', 'Espirito Santo'), ('PR', 'Paraná'), ('RO', 'Rondônia'), ('PE', 'Pernambuco'), ('RR', 'Roraima'), ('RJ', 'Rio de Janeiro'), ('MT', 'Mato Grosso'), ('RS', 'Rio Grande do Sul'), ('TO', 'Tocantins'), ('MS', 'Mato Grosso do Sul'), ('SE', 'Sergipe'), ('SC', 'Santa Catarina'), ('AC', 'Acre'), ('DF', 'Distrito Federal'), ('PA', 'Pará'), ('GO', 'Goiás'), ('AL', 'Alagoas'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PI', 'Piauí'), ('BA', 'Bahia'), ('PB', 'Praíba'), ('AM', 'amazonas'), ('SP', 'São Paulo')], default='SP', max_length=2),
        ),
    ]

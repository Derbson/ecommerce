# Generated by Django 4.1.7 on 2023-02-27 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_perfil_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='estado',
            field=models.CharField(choices=[('PR', 'Paraná'), ('MG', 'Minas Gerais'), ('AC', 'Acre'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('SP', 'São Paulo'), ('SC', 'Santa Catarina'), ('MS', 'Mato Grosso do Sul'), ('PA', 'Pará'), ('SE', 'Sergipe'), ('RO', 'Rondônia'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('BA', 'Bahia'), ('MT', 'Mato Grosso'), ('RS', 'Rio Grande do Sul'), ('RJ', 'Rio de Janeiro'), ('PI', 'Piauí'), ('RR', 'Roraima'), ('PB', 'Praíba'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('ES', 'Espirito Santo'), ('AM', 'amazonas'), ('TO', 'Tocantins'), ('AP', 'Amapá'), ('DF', 'Distrito Federal')], default='SP', max_length=2),
        ),
    ]
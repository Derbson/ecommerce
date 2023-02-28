# Generated by Django 4.1.7 on 2023-02-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_alter_perfil_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='estado',
            field=models.CharField(choices=[('SE', 'Sergipe'), ('MS', 'Mato Grosso do Sul'), ('CE', 'Ceará'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('GO', 'Goiás'), ('SC', 'Santa Catarina'), ('MG', 'Minas Gerais'), ('PB', 'Praíba'), ('SP', 'São Paulo'), ('AC', 'Acre'), ('MA', 'Maranhão'), ('RN', 'Rio Grande do Norte'), ('TO', 'Tocantins'), ('RS', 'Rio Grande do Sul'), ('RR', 'Roraima'), ('PR', 'Paraná'), ('PA', 'Pará'), ('DF', 'Distrito Federal'), ('AM', 'amazonas'), ('RO', 'Rondônia'), ('ES', 'Espirito Santo'), ('RJ', 'Rio de Janeiro'), ('PI', 'Piauí'), ('PE', 'Pernambuco'), ('BA', 'Bahia'), ('MT', 'Mato Grosso')], default='SP', max_length=2),
        ),
    ]

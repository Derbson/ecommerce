# Generated by Django 4.1.7 on 2023-03-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0007_alter_pedido_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='preco_promocional',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('C', 'Criado'), ('A', 'Aprovado'), ('F', 'Finalizado'), ('P', 'Pendente'), ('E', 'Enviado'), ('R', 'Reprovado')], default='C', max_length=1),
        ),
    ]

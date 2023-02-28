# Generated by Django 4.1.7 on 2023-02-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos_imagens/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='preço'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_promocional',
            field=models.FloatField(default=0, verbose_name='preço promo'),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='preco',
            field=models.FloatField(verbose_name='preço'),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='preco_promocional',
            field=models.FloatField(default=0, verbose_name='preço promo'),
        ),
    ]
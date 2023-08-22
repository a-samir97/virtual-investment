# Generated by Django 4.2.4 on 2023-08-20 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('purchase_price', models.FloatField(default=0.0)),
                ('type', models.IntegerField(choices=[(1, 'Buy'), (2, 'Sell')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.account')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='stocks.stock')),
            ],
        ),
    ]
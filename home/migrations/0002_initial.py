# Generated by Django 4.1.7 on 2023-04-19 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userinfo', verbose_name='用户邮箱'),
        ),
        migrations.AddField(
            model_name='orders',
            name='merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.merchants', verbose_name='所属商家'),
        ),
        migrations.AddField(
            model_name='orders',
            name='thing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.things', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='logs',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employees', verbose_name='员工编号'),
        ),
        migrations.AddField(
            model_name='logs',
            name='merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.merchants', verbose_name='所属商家'),
        ),
        migrations.AlterUniqueTogether(
            name='things',
            unique_together={('number', 'merchant')},
        ),
        migrations.AlterUniqueTogether(
            name='orders',
            unique_together={('email', 'merchant', 'thing', 'time')},
        ),
        migrations.AlterUniqueTogether(
            name='logs',
            unique_together={('employee', 'merchant', 'time')},
        ),
    ]

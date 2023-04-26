# Generated by Django 4.0.4 on 2023-04-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_core', '0002_po_so_luong_alter_hopdong_ma_nhan_vien_tao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hopdong',
            name='ma_hang_hoa',
            field=models.ManyToManyField(blank=True, null=True, to='web_core.hanghoa', verbose_name='Mã hàng hoá'),
        ),
        migrations.RemoveField(
            model_name='ncc',
            name='ma_hang_hoa',
        ),
        migrations.AddField(
            model_name='ncc',
            name='ma_hang_hoa',
            field=models.ManyToManyField(blank=True, null=True, to='web_core.hanghoa', verbose_name='Mã hàng hoá'),
        ),
    ]

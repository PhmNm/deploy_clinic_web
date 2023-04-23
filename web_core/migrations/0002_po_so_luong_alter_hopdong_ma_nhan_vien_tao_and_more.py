# Generated by Django 4.0.4 on 2023-04-18 15:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='po',
            name='so_luong',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Số lượng'),
        ),
        migrations.AlterField(
            model_name='hopdong',
            name='ma_nhan_vien_tao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nv_tao_HD', to='web_core.nhanvien', verbose_name='Mã nhân viên tạo'),
        ),
        migrations.AlterField(
            model_name='hopdong',
            name='ma_quan_ly_duyet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quan_ly_HD', to='web_core.nhanvien', verbose_name='Mã quản lý duyệt'),
        ),
        migrations.AlterField(
            model_name='ncc',
            name='ma_hang_hoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.hanghoa', verbose_name='Mã hàng hoá'),
        ),
        migrations.AlterField(
            model_name='ncc',
            name='ma_nhan_vien_tao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.nhanvien', verbose_name='Mã nhân viên tạo'),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='chuc_vu',
            field=models.CharField(choices=[('Quản lí', 'Quản lí'), ('Nhân viên', 'Nhân viên')], max_length=50, null=True, verbose_name='Chức vụ'),
        ),
        migrations.AlterField(
            model_name='nhapkho',
            name='danh_gia_chat_luong',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Đánh giá chất lượng'),
        ),
        migrations.AlterField(
            model_name='nhapkho',
            name='ma_PO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.po', verbose_name='Mã PO'),
        ),
        migrations.AlterField(
            model_name='nhapkho',
            name='ma_nhan_vien_kho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.nhanvien', verbose_name='Mã nhân viên kho'),
        ),
        migrations.AlterField(
            model_name='nhapkho',
            name='vi_tri_luu_kho',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Vị trí lưu kho'),
        ),
        migrations.AlterField(
            model_name='po',
            name='ma_PR',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_core.pr', verbose_name='Mã PR'),
        ),
        migrations.AlterField(
            model_name='po',
            name='ma_hang_hoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_core.hanghoa', verbose_name='Mã hàng hoá'),
        ),
        migrations.AlterField(
            model_name='po',
            name='ma_hop_dong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.hopdong', verbose_name='Mã hợp đồng'),
        ),
        migrations.AlterField(
            model_name='po',
            name='ma_ncc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.ncc', verbose_name='Mã nhà cung cấp'),
        ),
        migrations.AlterField(
            model_name='po',
            name='ma_quan_ly_duyet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quan_ly', to='web_core.nhanvien', verbose_name='Mã quản lý duyệt'),
        ),
        migrations.AlterField(
            model_name='po',
            name='trang_thai',
            field=models.CharField(blank=True, choices=[('Đang xem xét', 'Đang xem xét'), ('Đã đặt hàng', 'Đã đặt hàng'), ('Đang giao hàng', 'Đang giao hàng'), ('Đã giao hàng', 'Đã giao hàng')], max_length=100, null=True, verbose_name='Trạng thái PO'),
        ),
        migrations.AlterField(
            model_name='pr',
            name='ma_nhan_vien_phu_trach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nv_phutrach_PR', to='web_core.nhanvien', verbose_name='Mã nhân viên phụ trách'),
        ),
        migrations.AlterField(
            model_name='pr',
            name='ma_nhan_vien_tao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nv_tao_PR', to='web_core.nhanvien', verbose_name='Mã nhân viên tạo'),
        ),
        migrations.AlterField(
            model_name='pr_hh',
            name='ma_PR',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_core.pr', verbose_name='Mã PR'),
        ),
        migrations.AlterField(
            model_name='pr_hh',
            name='ngay_can_hang',
            field=models.DateField(blank=True, null=True, verbose_name='Ngày cần hàng'),
        ),
        migrations.AlterField(
            model_name='pr_hh',
            name='yeu_cau',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Yêu cầu'),
        ),
        migrations.AlterField(
            model_name='thanhtoan',
            name='chung_tu_thanh_toan',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='', verbose_name='Chứng từ thanh toán'),
        ),
        migrations.AlterField(
            model_name='thanhtoan',
            name='ma_HD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.hopdong', verbose_name='Mã hợp đồng'),
        ),
        migrations.AlterField(
            model_name='thanhtoan',
            name='ma_PO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.po', verbose_name='Mã PO'),
        ),
        migrations.AlterField(
            model_name='thanhtoan',
            name='ma_nhan_vien_tao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.nhanvien', verbose_name='Mã nhân viên tạo'),
        ),
    ]

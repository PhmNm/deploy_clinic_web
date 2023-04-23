# Generated by Django 4.0.4 on 2023-04-17 13:51

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HANGHOA',
            fields=[
                ('ma_HH', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='HH', primary_key=True, serialize=False, verbose_name='Mã hàng hoá')),
                ('ten_hang_hoa', models.CharField(max_length=100, null=True, verbose_name='Tên hàng hoá')),
                ('so_luong_ton', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Số lượng tồn')),
            ],
        ),
        migrations.CreateModel(
            name='HOPDONG',
            fields=[
                ('ma_HD', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='HD', primary_key=True, serialize=False, verbose_name='Mã hợp đồng')),
                ('ngay_tao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày tạo')),
                ('ngay_cap_nhat', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày cập nhật')),
                ('ngay_hieu_luc', models.DateField(null=True, verbose_name='Ngày hiệu lực')),
                ('ngay_het_han', models.DateField(null=True, verbose_name='Ngày hết hạn')),
                ('file_hop_dong', models.CharField(max_length=500, null=True, verbose_name='File hợp động')),
                ('phu_luc_hop_dong', models.CharField(max_length=20000, null=True, verbose_name='Phụ lục hợp đồng')),
                ('trang_thai', models.CharField(choices=[('Đang xem xét', 'Đang xem xét'), ('Đã ký', 'Đã ký'), ('Đang có hiệu lực', 'Đang có hiệu lực'), ('Đã hết hạn', 'Đã hết hạn')], max_length=100, null=True, verbose_name='Trạng thái hợp đồng')),
                ('ma_hang_hoa', models.ManyToManyField(to='web_core.hanghoa', verbose_name='Mã hàng hoá')),
            ],
        ),
        migrations.CreateModel(
            name='NCC',
            fields=[
                ('ma_NCC', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='NC', primary_key=True, serialize=False, verbose_name='Mã nhà cung cấp')),
                ('ma_so_thue', models.CharField(max_length=20, null=True, verbose_name='Mã số thuế')),
                ('ten_doanh_nghiep', models.CharField(max_length=100, null=True, verbose_name='Tên doanh nghiệp')),
                ('dia_chi', models.CharField(max_length=300, null=True, verbose_name='Địa chỉ')),
                ('nguoi_lien_he', models.CharField(max_length=100, null=True, verbose_name='Người liên hệ')),
                ('sdt', models.CharField(max_length=20, null=True, verbose_name='Số điện thoại')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='Email')),
                ('stk', models.CharField(max_length=20, null=True, verbose_name='Số tài khoản')),
                ('giay_phep', models.CharField(max_length=100, null=True, verbose_name='Giấy phép')),
                ('nang_luc_hang_hoa', models.CharField(max_length=100, null=True, verbose_name='Năng lực hàng hoá')),
                ('ngay_cap_nhat', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày cập nhật')),
                ('cong_no', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Công nợ')),
                ('ma_hang_hoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.hanghoa', verbose_name='Mã hàng hoá')),
            ],
        ),
        migrations.CreateModel(
            name='NHANVIEN',
            fields=[
                ('ma_NV', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='NV', primary_key=True, serialize=False, verbose_name='Mã nhân viên')),
                ('ho_ten', models.CharField(max_length=100, null=True, verbose_name='Họ tên')),
                ('phong_ban', models.CharField(choices=[('Thu mua', 'Thu mua'), ('Kho', 'Kho'), ('Kế toán', 'Kế toán'), ('Khác', 'Khác')], max_length=50, null=True, verbose_name='Phòng ban')),
                ('chuc_vu', models.CharField(choices=[('Quản lý', 'Quản lý'), ('Nhân viên', 'Nhân viên')], max_length=50, null=True, verbose_name='Chức vụ')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PO',
            fields=[
                ('ma_PO', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='PO', primary_key=True, serialize=False, verbose_name='Mã PO')),
                ('ngay_tao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày tạo')),
                ('ngay_cap_nhat', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày cập nhật')),
                ('trang_thai', models.CharField(choices=[('Đang xem xét', 'Đang xem xét'), ('Đã đặt hàng', 'Đã đặt hàng'), ('Đang giao hàng', 'Đang giao hàng'), ('Đã giao hàng', 'Đã giao hàng')], max_length=100, null=True, verbose_name='Trạng thái PO')),
            ],
        ),
        migrations.CreateModel(
            name='PR',
            fields=[
                ('ma_PR', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='PR', primary_key=True, serialize=False, verbose_name='Mã PR')),
                ('ngay_tao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày tạo')),
                ('ngay_cap_nhat', models.DateField(default=datetime.datetime.now, verbose_name='Ngày cập nhật')),
                ('ten_PR', models.CharField(max_length=300, verbose_name='Tên PR')),
                ('trang_thai', models.CharField(choices=[('Đang xem xét', 'Đang xem xét'), ('Đang thực hiện', 'Đang thực hiện'), ('Đã hoàn thành', 'Đã hoàn thành')], default='Đang xem xét', max_length=100, null=True, verbose_name='Trạng thái PR')),
                ('ma_nhan_vien_phu_trach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nv_phutrach_PR', to='web_core.nhanvien', verbose_name='Mã nhân viên phụ trách')),
                ('ma_nhan_vien_tao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nv_tao_PR', to='web_core.nhanvien', verbose_name='Mã nhân viên tạo')),
            ],
        ),
        migrations.CreateModel(
            name='THANHTOAN',
            fields=[
                ('ma_TT', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='TT', primary_key=True, serialize=False, verbose_name='Mã thanh toán')),
                ('ngay_tao', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('so_tien', models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Số tiền')),
                ('ngay_cap_nhat', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày cập nhật')),
                ('trang_thai', models.CharField(choices=[('Đang chờ thanh toán', 'Đang chờ thanh toán'), ('Đã thanh toán', 'Đã thanh toán'), ('Đã thanh toán lần 1', 'Đã thanh toán lần 1'), ('Đã thanh toán lần 2', 'Đã thanh toán lần 2'), ('Đã hoàn thành', 'Đã hoàn thành')], max_length=100, verbose_name='Trạng thái thanh toán')),
                ('chung_tu_thanh_toan', models.ImageField(max_length=200, null=True, upload_to='', verbose_name='Chứng từ thanh toán')),
                ('ma_HD', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.hopdong', verbose_name='Mã hợp đồng')),
                ('ma_PO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.po', verbose_name='Mã PO')),
                ('ma_nhan_vien_tao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.nhanvien', verbose_name='Mã nhân viên tạo')),
            ],
        ),
        migrations.CreateModel(
            name='PR_HH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_luong', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Số lượng')),
                ('ngay_can_hang', models.DateField(null=True, verbose_name='Ngày cần hàng')),
                ('ngay_cap_nhat', models.DateField(default=datetime.datetime.now, verbose_name='Ngày cập nhật')),
                ('yeu_cau', models.CharField(max_length=300, null=True, verbose_name='Yêu cầu')),
                ('trang_thai', models.CharField(choices=[('Đang xem xét', 'Đang xem xét'), ('Đang thực hiện', 'Đang thực hiện'), ('Đã hoàn thành', 'Đã hoàn thành')], default='Đang xem xét', max_length=100, null=True, verbose_name='Trạng thái PR')),
                ('ma_PR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_core.pr', verbose_name='Mã PR')),
                ('ma_hang_hoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.hanghoa', verbose_name='Mã hàng hoá')),
            ],
        ),
        migrations.AddField(
            model_name='po',
            name='ma_PR',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_core.pr', verbose_name='Mã PR'),
        ),
        migrations.AddField(
            model_name='po',
            name='ma_hang_hoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_core.hanghoa', verbose_name='Mã hàng hoá'),
        ),
        migrations.AddField(
            model_name='po',
            name='ma_hop_dong',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.hopdong', verbose_name='Mã hợp đồng'),
        ),
        migrations.AddField(
            model_name='po',
            name='ma_ncc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.ncc', verbose_name='Mã nhà cung cấp'),
        ),
        migrations.AddField(
            model_name='po',
            name='ma_nhan_vien_tao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nv_tao_PO', to='web_core.nhanvien', verbose_name='Mã nhân viên tạo'),
        ),
        migrations.AddField(
            model_name='po',
            name='ma_quan_ly_duyet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quan_ly', to='web_core.nhanvien', verbose_name='Mã quản lý duyệt'),
        ),
        migrations.CreateModel(
            name='NHAPKHO',
            fields=[
                ('ma_NK', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=10, max_length=12, prefix='NK', primary_key=True, serialize=False, verbose_name='Mã PO')),
                ('ngay_tao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ngày tạo')),
                ('danh_gia_chat_luong', models.CharField(max_length=50, null=True, verbose_name='Đánh giá chất lượng')),
                ('so_luong_nhap_kho', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Số lượng nhập kho')),
                ('vi_tri_luu_kho', models.CharField(max_length=300, null=True, verbose_name='Vị trí lưu kho')),
                ('ma_PO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.po', verbose_name='Mã PO')),
                ('ma_nhan_vien_kho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.nhanvien', verbose_name='Mã nhân viên kho')),
            ],
        ),
        migrations.AddField(
            model_name='ncc',
            name='ma_nhan_vien_tao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.nhanvien', verbose_name='Mã nhân viên tạo'),
        ),
        migrations.AddField(
            model_name='hopdong',
            name='ma_ncc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_core.ncc', verbose_name='Nhà cung cấp'),
        ),
        migrations.AddField(
            model_name='hopdong',
            name='ma_nhan_vien_tao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nv_tao_HD', to='web_core.nhanvien', verbose_name='Mã nhân viên tạo'),
        ),
        migrations.AddField(
            model_name='hopdong',
            name='ma_quan_ly_duyet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quan_ly_HD', to='web_core.nhanvien', verbose_name='Mã quản lý duyệt'),
        ),
    ]

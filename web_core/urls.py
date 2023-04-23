from django.urls import path

from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', lambda request: redirect('dspr', permanent=False), name='home'),
    # path('', views.dskb, name='home'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('dshh/', views.dshh, name='quanli_dshh'),

    path('dspr/', views.dspr, name='quanli_dspr'),
    path('them_pr/', views.add_pr, name='quanli_them_pr'),
    path('xem_pr/<str:ma_PR>', views.view_pr, name='quanli_xem_pr'),

    path('ca_nhan/dspr/', views.dspr_canhan, name='canhan_dspr'),
    path('ca_nhan/them_pr/', views.add_pr, name='canhan_them_pr'),
    path('ca_nhan/xem_pr/<str:ma_PR>', views.view_pr_canhan, name='canhan_xem_pr'),
    path('ca_nhan/sua_pr/<str:ma_PR>-<str:ma_HH>', views.edit_pr_canhan, name='canhan_sua_pr'),

    path('dspo/', views.dspo, name='quanli_dspo'),
    path('xem_po/<str:ma_PO>', views.view_po, name='quanli_xem_po'),

    path('ca_nhan/dspo/', views.dspo_canhan, name='canhan_dspo'),
    path('ca_nhan/xem_po/<str:ma_PO>', views.view_po_canhan, name='canhan_xem_po'),
    # path('dsbn', views.dsbn, name='quanli_dsbn'),
    # path('sua_bn/<str:id>', views.edit_benhnhan, name='quanli_sua_benhnhan'),
    # path('xoa_bn/<str:id>', views.del_benhnhan, name='quanli_xoa_benhnhan'),

    # path('xuathoadon', views.xuathoadon, name='quanli_xuathoadon'),
    # path('hoadon/<str:pk>/', views.hoadon, name='quanli_xuathoadon_hoadon'),

    # path('lsk',views.lsk, name='quanli_lsk'),

    # path('dspk',views.dspk, name='quanli_dspk'),
    # path('them_pk', views.add_phieukham, name='quanli_them_phieukham'),
    # path('sua_pk/<str:id>', views.edit_phieukham, name='quanli_sua_phieukham'),
    # path('xoa_pk/<str:id>', views.del_phieukham, name='quanli_xoa_phieukham'),

    # path('lapbaocao/', views.lap_bao_cao, name='quanli_lapbaocao'),
    # path('lapbaocao/doanhthuthang/', views.baocao_doanhthuthang, name='quanli_lapbaocao_bcdtt'),
    # path('lapbaocao/sudungthuoc/', views.baocao_sudungthuoc, name='quanli_lapbaocao_bcsdt'),

    # path('thaydoi/', views.thaydoi_quydinh, name='quanli_thaydoi'),
    # path('thaydoi/soluongbenhnhan', views.thaydoi_slbn, name='quanli_thaydoi_slbn'),
    # path('thaydoi/tienkham', views.thaydoi_tienkham, name='quanli_thaydoi_tienkham'),

    # path('thaydoi/loaibenh', views.thaydoi_loaibenh, name='quanli_thaydoi_loaibenh'),
    # path('thaydoi/loaibenh/them', views.thaydoi_loaibenh_them, name='quanli_thaydoi_loaibenh_them'),
    # path('thaydoi/loaibenh/xoa/<str:id>', views.thaydoi_loaibenh_xoa, name='quanli_thaydoi_loaibenh_xoa'),

    # path('thaydoi/donvitinh', views.thaydoi_dvt, name='quanli_thaydoi_dvt'),
    # path('thaydoi/donvitinh/them', views.thaydoi_dvt_them, name='quanli_thaydoi_dvt_them'),
    # path('thaydoi/donvitinh/xoa/<str:id>', views.thaydoi_dvt_xoa, name='quanli_thaydoi_dvt_xoa'),

    # path('thaydoi/cachdung', views.thaydoi_cachdung, name='quanli_thaydoi_cachdung'),
    # path('thaydoi/cachdung/them', views.thaydoi_cachdung_them, name='quanli_thaydoi_cachdung_them'),
    # path('thaydoi/cachdung/xoa/<str:id>', views.thaydoi_cachdung_xoa, name='quanli_thaydoi_cachdung_xoa'),

    # path('thaydoi/thuoc', views.thaydoi_thuoc, name='quanli_thaydoi_thuoc'),
    # path('thaydoi/thuoc/them', views.thaydoi_thuoc_them, name='quanli_thaydoi_thuoc_them'),
    # path('thaydoi/thuoc/xoa/<str:id>', views.thaydoi_thuoc_xoa, name='quanli_thaydoi_thuoc_xoa'),
    # path('thaydoi/thuoc/sua/<str:id>', views.thaydoi_thuoc_sua, name='quanli_thaydoi_thuoc_sua'),
]

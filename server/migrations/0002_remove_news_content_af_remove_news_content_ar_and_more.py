# Generated by Django 4.1.2 on 2023-02-14 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content_af',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ar',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ar_dz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ast',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_az',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_be',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_bg',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_bn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_br',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_bs',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ca',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_cs',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_cy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_da',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_de',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_dsb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_el',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_en_au',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_en_gb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_eo',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_es',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_es_ar',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_es_co',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_es_mx',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_es_ni',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_es_ve',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_et',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_eu',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_fa',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_fi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_fr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_fy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ga',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_gd',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_gl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_he',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_hi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_hr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_hsb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_hu',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_hy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ia',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ig',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ind',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_io',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_is',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_it',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ja',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ka',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_kab',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_kk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_km',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_kn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ko',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_lb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_lt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_lv',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_mk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ml',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_mn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_mr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ms',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_my',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_nb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ne',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_nl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_nn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_os',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_pa',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_pl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_pt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_pt_br',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ro',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_sk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_sl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_sq',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_sr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_sr_latn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_sv',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_sw',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ta',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_te',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_tg',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_th',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_tk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_tr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_tt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_udm',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_uk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ur',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_vi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_zh_hans',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_zh_hant',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_af',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ar',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ar_dz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ast',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_az',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_be',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_bg',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_bn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_br',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_bs',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ca',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_cs',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_cy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_da',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_de',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_dsb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_el',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_en_au',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_en_gb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_eo',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_es',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_es_ar',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_es_co',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_es_mx',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_es_ni',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_es_ve',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_et',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_eu',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_fa',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_fi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_fr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_fy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ga',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_gd',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_gl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_he',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_hi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_hr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_hsb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_hu',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_hy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ia',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ig',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ind',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_io',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_is',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_it',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ja',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ka',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_kab',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_kk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_km',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_kn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ko',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_lb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_lt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_lv',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_mk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ml',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_mn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_mr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ms',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_my',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_nb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ne',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_nl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_nn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_os',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_pa',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_pl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_pt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_pt_br',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ro',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_sk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_sl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_sq',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_sr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_sr_latn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_sv',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_sw',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ta',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_te',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_tg',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_th',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_tk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_tr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_tt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_udm',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_uk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_ur',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_vi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_zh_hans',
        ),
        migrations.RemoveField(
            model_name='news',
            name='preview_zh_hant',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_af',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ar',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ar_dz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ast',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_az',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_be',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_bg',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_bn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_br',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_bs',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ca',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_cs',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_cy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_da',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_dsb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_el',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_en_au',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_en_gb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_eo',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_es',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_es_ar',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_es_co',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_es_mx',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_es_ni',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_es_ve',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_et',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_eu',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_fa',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_fi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_fy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ga',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_gd',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_gl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_he',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_hi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_hr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_hsb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_hu',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_hy',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ia',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ig',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ind',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_io',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_is',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_it',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ja',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ka',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_kab',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_kk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_km',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_kn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ko',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_lb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_lt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_lv',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_mk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ml',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_mn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_mr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ms',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_my',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_nb',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ne',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_nl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_nn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_os',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_pa',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_pl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_pt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_pt_br',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ro',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_sk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_sl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_sq',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_sr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_sr_latn',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_sv',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_sw',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ta',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_te',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_tg',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_th',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_tk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_tr',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_tt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_udm',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_uk',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ur',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_vi',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_zh_hans',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_zh_hant',
        ),
        migrations.AddField(
            model_name='news',
            name='rubric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.rubrics'),
        ),
    ]

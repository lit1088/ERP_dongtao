# -*- coding: utf-8 -*-

# Created on 2020-5-15
# author: adolph

# description:

{
    'name': '东涛数字信息系统(Creat by Adolph)',
    'version': '13.20.05.10',
    'author': 'adolph，东涛',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
     东涛系统配置文件
    """,
    'description': """
    """,
    'images': ['static/description/banner.gif'],
    'depends': [
        'base_setup',
        'web',
        'mail',
        'iap',
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    'data': [
        'views/app_odoo_customize_views.xml',
        'views/app_theme_config_settings_views.xml',
        'views/res_config_settings_views.xml',
        'views/ir_views.xml',
        'views/ir_module_module_views.xml',
        'views/ir_ui_menu_views.xml',
        # data
        'data/ir_config_parameter.xml',
        'data/ir_module_module.xml',
        # 'data/digest_template_data.xml',
        'data/res_company_data.xml',
        'data/res_groups.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': True,
}

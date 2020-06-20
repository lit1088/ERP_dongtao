# -*- coding: utf-8 -*-

# Created on 2018-11-26
# author: 广州尚鹏，https://www.dongtao.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12在线用户手册（长期更新）
# https://www.dongtao.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.dongtao.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.dongtao.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.dongtao.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.dongtao.cn/odoo10_developer_document_offline/
# description:

{
    'name': '东涛数字信息系统',
    'version': 'V1.0',
    'author': 'adolph',
    'category': 'Productivity',
    'website': 'https://www.dongtao.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    """,
    'description': """
    东涛数字信息系统专用
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

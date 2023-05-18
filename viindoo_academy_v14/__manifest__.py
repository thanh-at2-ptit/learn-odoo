# -*- coding: utf-8 -*-
{
    'name': "viindoo_academy_v14",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Academy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/root_menu.xml',
        'wizard/education_enrollment_views.xml',
        'views/education_class_views.xml',
        'views/education_class_views2.xml',
        'views/education_student_views.xml',
        'views/education_enrollment_views.xml',
        'views/res_ethnic_views.xml',
        'reports/education_class_report_views2.xml',
        'views/education_class_views.xml',
        'views/academy_templates.xml',
        'views/academy_teacher.xml',
        # neu khai bao o day se luon luon co du lieu demo
        # 'demo/demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'application': True,
}

# -*- coding: utf-8 -*-
{
    'name': "CRM_Customizations",

    'summary': "customization of CRM according to ConnecTech Needs",

    'description': """
Long description of module's purpose
    """,

    'author': "Cymax Technologies",
    'website': "https://www.cymaxtech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    'category': 'CRM',
    'depends': ['base', 'crm', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/crm_stage.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': False,
}

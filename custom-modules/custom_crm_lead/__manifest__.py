{
    'name': 'CRM Leads',
    'version': '1.0',
    'summary': 'Custom lead form for CRM module',
    'depends': ['crm', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/lead_form_view.xml',
        'views/cus_lead_report_view.xml',
        'views/cus_lead_report_print_view.xml',
        'views/crm_lead_filter_report_view.xml',
        'views/crm_form_custom_fields_view.xml',
        'views/custom_crm_menu_views.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

{
    'name': 'Custom CRM Styling',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Custom styles for the CRM module',
    'description': 'This module customizes the styling of the CRM module.',
    'author': 'Your Name/Company',
    'depends': ['crm', 'web','project','crm_iap_mine'],
    'data': [
        'views/crm_templates.xml',  # Template overrides
        'views/remove_lead_button.xml'
    ],
    'assets': {
        'web.assets_backend': [
            '/rfqm_styling/static/src/css/crm_custom_styles.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

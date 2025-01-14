{
    'name': 'Custom Login Page',
    'version': '1.0',
    'summary': 'Customize the Odoo login page with custom branding and styles',
    'description': 'This module allows you to replace the default Odoo login page with a custom design.',
    'author': 'Cymax Technologies',
    'category': 'Custom',
    'depends': ['web'],  # Specify the dependent modules
    'data': [
        'views/custom_login.xml',  # Add your XML file for customizations
    ],
    'assets': {
        'web.assets_frontend': [
            '/custom_login_page/static/src/css/custom_login.css',  # Add CSS
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

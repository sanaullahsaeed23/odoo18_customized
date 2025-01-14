{
    'name': 'Ecommerce Lead Generation',
    'version': '1.0',
    'summary': 'Generate CRM leads from product inquiries on the website.',
    'category': 'Website',
    'depends': [
        'website_sale',  # Dependency for e-commerce functionality
        'crm'            # Dependency for lead creation
    ],
    'data': [
        'views/custom_cart_form.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

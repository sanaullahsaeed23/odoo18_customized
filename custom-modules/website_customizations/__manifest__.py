{
    'name': 'Website Request for Quote',
    'version': '1.0',
    'author': 'Sanaullah Saeed',
    'depends': ['website_sale', 'crm'],
    'data': [
        'views/request_quote_template.xml',
        # 'views/request_quote_snippet.xml',
        # 'data/request_quote_lead.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/website_customizations/static/src/css/custom.css',  # Optional custom styles
        ],
    },
    'installable': True,  # Mark the module as installable
    'application': False,  # Set to False if this is a supporting module, not a standalone application
    'auto_install': False,
}

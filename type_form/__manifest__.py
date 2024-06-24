{
    'name': 'Type Form',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Type Form',
    'sequence': '10',
    'description': """This is not for sales. First try input in apps.odoo. This module installed at contact menu configuration.""",
    'license': 'LGPL-3',
    'author': 'Sokehpwar',
    'maintainer': 'Sokehpwar',
    'website': 'https://sokehpwarlay.blogspot.com/',
    'depends': ['base',],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/type_info.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/index.html',
        'static/description/icon.png'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

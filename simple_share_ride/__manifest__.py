# -*- coding: utf-8 -*-
{
    'name': "simple_share_ride",

    'summary': """
        simple share ride.
    """,
    'description': """
        simple share ride.
    """,
    'author': "Michael",
    'website': "https://boming0529.github.io/",
    'category': 'website',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'website',
        'product',
        'sale',
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/templates.xml',
        'data/product_template.xml'
    ],
}

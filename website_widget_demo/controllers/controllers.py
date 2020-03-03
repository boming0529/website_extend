# -*- coding: utf-8 -*-
from odoo import http


class WebsiteWidgetDemo(http.Controller):

    @http.route('/demo/index', type="http", auth='public', method=["Get"], website=True)
    def demo_indexs(self, **kw):
        return http.request.render('website_widget_demo.index', {
            'heroes':  [
                {'id': 11, 'name': 'Mr. Nice'},
                {'id': 12, 'name': 'Narco'},
                {'id': 13, 'name': 'Bombasto'},
                {'id': 14, 'name': 'Celeritas'},
                {'id': 15, 'name': 'Magneta'},
                {'id': 16, 'name': 'RubberMan'},
                {'id': 17, 'name': 'Dynama'},
                {'id': 18, 'name': 'Dr IQ'},
                {'id': 19, 'name': 'Magma'},
                {'id': 20, 'name': 'Tornado'}
            ]
        })

    @http.route('/get/heroes/', type="json", auth='public', website=True, method=['POST'], csrf=False)
    def get_heroes(self, **kw):
        return {'heroes':  [
                {'id': 11, 'name': 'Mr. Nice'},
                {'id': 12, 'name': 'Narco'},
                {'id': 13, 'name': 'Bombasto'},
                {'id': 14, 'name': 'Celeritas'},
                {'id': 15, 'name': 'Magneta'},
                {'id': 16, 'name': 'RubberMan'},
                {'id': 17, 'name': 'Dynama'},
                {'id': 18, 'name': 'Dr IQ'},
                {'id': 19, 'name': 'Magma'},
                {'id': 20, 'name': 'Tornado'}
            ]
        }

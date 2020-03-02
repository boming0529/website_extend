# -*- coding: utf-8 -*-
from odoo import http


class WebsiteWidgetDemo(http.Controller):

    @http.route('/demo/index', type="http", auth='public', method=["Get"], website=True)
    def demo_indexs(self, **kw):
        return http.request.render('website_widget_demo.index', {})

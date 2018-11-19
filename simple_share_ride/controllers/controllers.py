# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class share_ride(http.Controller):

    @http.route(['/share/share_ride'], type="http", auth='public', method=["Get"], website=True)
    def index(self, **kw):
        origin = request.env['product.attribute.value'].search([
            ('attribute_id', '=', request.env.ref('simple_share_ride.share_origin_attribute').id)
        ])
        destination = request.env['product.attribute.value'].search([
            ('attribute_id', '=', request.env.ref('simple_share_ride.share_destination_attribute').id)
        ])
        return request.render('simple_share_ride.share_page', {
            'origin': origin,
            'destination': destination,
        })

    @http.route(['/share/create_order'], type="http", auth='public', method=["Post"], website=True, csrf=False)
    def create_order(self, **post):
        # find product for user choise
        origin = request.env['product.attribute.value'].search([
            ('attribute_id', '=', request.env.ref('simple_share_ride.share_origin_attribute').id), 
            ('name', '=', post.get('start'))
        ])
        destination = request.env['product.attribute.value'].search([
            ('attribute_id', '=', request.env.ref('simple_share_ride.share_destination_attribute').id),
            ('name', '=', post.get('end'))
        ])
        attribute_val_ids = "-".join([str(x) for x in origin.ids + destination.ids])
        product = request.env['product.product'].search([('share_ride_code', '=', attribute_val_ids)])
        # create sale order and send mail
        sale_order = request.env['sale.order']
        new_so = sale_order.create({
            'partner_id': request.env.user.partner_id.id,
            'order_line': [(0, False, {
                'product_id': product.id,
            })],
            'user_id': False,
        })
        new_so.force_quotation_send()
        return request.redirect('/page/homepage')

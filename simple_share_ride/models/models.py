# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_attribute_value(models.Model):
    _inherit = 'product.attribute.value'

    lat = fields.Float(string="lat") 
    lng = fields.Float(string="lng") 


class product_product(models.Model):
    _inherit = 'product.product'

    @api.depends('attribute_value_ids')
    def _compute_share_ride_code(self):
        for record in self:
            record.share_ride_code = "-".join([str(x) for x in record.attribute_value_ids.ids])

    share_ride_code = fields.Char(
        string='share ride code',
        store=True,
        compute='_compute_share_ride_code'
    )

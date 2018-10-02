# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class website_config_settings(models.TransientModel):

    _inherit = "website.config.settings"

    website_slide_Slideshare_app_key = fields.Char(string='Slideshare app key')
    website_slide_slideshare_sharedsecret = fields.Char(string='Slideshare sharedsecret')

    @api.model
    def get_default_website_slide_Slideshare_app_key(self, fields):
        website_slide_Slideshare_app_key = False
        if 'website_slide_Slideshare_app_key' in fields:
            website_slide_Slideshare_app_key = self.env['ir.config_parameter'].sudo().get_param('website_slides.slideshare_api_key')
        return {
            'website_slide_Slideshare_app_key': website_slide_Slideshare_app_key
        }

    @api.multi
    def set_website_slide_Slideshare_app_key(self):
        for wizard in self:
            self.env['ir.config_parameter'].sudo().set_param(
                'website_slides.slideshare_api_key', wizard.website_slide_Slideshare_app_key)

    @api.model
    def get_default_website_slide_slideshare_sharedsecret(self, fields):
        website_slide_slideshare_sharedsecret = False
        if 'website_slide_slideshare_sharedsecret' in fields:
            website_slide_slideshare_sharedsecret = self.env['ir.config_parameter'].sudo().get_param('website_slides.slideshare_sharedsecret')
        return {
            'website_slide_slideshare_sharedsecret': website_slide_slideshare_sharedsecret
        }

    @api.multi
    def set_website_slide_slideshare_sharedsecret(self):
        for wizard in self:
            self.env['ir.config_parameter'].sudo().set_param(
                'website_slides.slideshare_sharedsecret', wizard.website_slide_slideshare_sharedsecret)

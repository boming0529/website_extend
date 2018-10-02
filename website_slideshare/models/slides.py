# -*- coding: utf-8 -*-

import re
from odoo import models, fields, api
from . import slideshare


class website_slideshare(models.Model):
    _inherit = 'slide.slide'


    def _find_document_data_from_url(self, url):
        expr = re.compile(r'^http(s?):\/\/www.slideshare.net\/[\w\-]+\/[\w\-]+$')
        arg = expr.match(url)
        document_id = arg and arg.group(0) or False
        if document_id:
            return ('slideshare', document_id)
        return super(website_slideshare, self)._find_document_data_from_url(url)

    @api.model
    def _parse_slideshare_document(self, document_id, only_preview_fields):
        api_key = self.env['ir.config_parameter'].sudo().get_param('website_slides.slideshare_api_key')
        sharedsecret = self.env['ir.config_parameter'].sudo().get_param('website_slides.slideshare_sharedsecret')
        Slide = slideshare.SlideshareAPI(api_key=api_key, sharedsecret=sharedsecret)
        fetch_res = Slide.get_slideshow(slideshow_url=document_id)
        if fetch_res.get('error'):
            return fetch_res
        slideshare_values = fetch_res['values']
        values = {}
        if slideshare_values.get('Slideshow'):
            Slideshow = slideshare_values['Slideshow']
            values = {
                'slide_type': 'video',
                'document_id': Slideshow['SecretKey'],
            }
            url_scheme = 'https:'
            if only_preview_fields:
                values.update({
                    'url_src': url_scheme + Slideshow['ThumbnailXXLargeURL'],
                    'title': Slideshow['Title'],
                    'description': Slideshow['Description'],
                })
                return values
            values.update({
                'name': Slideshow['Title'],
                'image': self._fetch_data(url_scheme + Slideshow['ThumbnailXXLargeURL'], {}, 'image')['values'],
                'description': Slideshow['Description'],
                'mime_type': False,
            })
        return {'values': values}
 
    def _get_embed_code(self): 
        super(website_slideshare, self)._get_embed_code()
        for record in self:
            expr = re.compile(r'^http(s?):\/\/www.(slideshare).net\/[\w\-]+\/[\w\-]+$')
            arg = expr.match(record.url)
            is_slideshare = arg and arg.group(2) or False
            if record.slide_type == 'video' and record.document_id and is_slideshare == 'slideshare':
                record.embed_code = '<iframe src="https://www.slideshare.net/slideshow/embed_code/key/%s" allowFullScreen="true" frameborder="0"></iframe>' % (record.document_id)

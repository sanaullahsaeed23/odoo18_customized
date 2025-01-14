# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteCustomizations(http.Controller):
#     @http.route('/website_customizations/website_customizations', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_customizations/website_customizations/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_customizations.listing', {
#             'root': '/website_customizations/website_customizations',
#             'objects': http.request.env['website_customizations.website_customizations'].search([]),
#         })

#     @http.route('/website_customizations/website_customizations/objects/<model("website_customizations.website_customizations"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_customizations.object', {
#             'object': obj
#         })


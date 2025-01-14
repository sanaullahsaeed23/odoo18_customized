# -*- coding: utf-8 -*-
# from odoo import http


# class ConnectechCrmCustomization(http.Controller):
#     @http.route('/connectech_crm_customization/connectech_crm_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/connectech_crm_customization/connectech_crm_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('connectech_crm_customization.listing', {
#             'root': '/connectech_crm_customization/connectech_crm_customization',
#             'objects': http.request.env['connectech_crm_customization.connectech_crm_customization'].search([]),
#         })

#     @http.route('/connectech_crm_customization/connectech_crm_customization/objects/<model("connectech_crm_customization.connectech_crm_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('connectech_crm_customization.object', {
#             'object': obj
#         })


# -*- coding: utf-8 -*-
# from odoo import http


# class RfqmStyling(http.Controller):
#     @http.route('/rfqm_styling/rfqm_styling', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rfqm_styling/rfqm_styling/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rfqm_styling.listing', {
#             'root': '/rfqm_styling/rfqm_styling',
#             'objects': http.request.env['rfqm_styling.rfqm_styling'].search([]),
#         })

#     @http.route('/rfqm_styling/rfqm_styling/objects/<model("rfqm_styling.rfqm_styling"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rfqm_styling.object', {
#             'object': obj
#         })


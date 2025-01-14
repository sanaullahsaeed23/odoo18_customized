# -*- coding: utf-8 -*-
# from odoo import http


# class CustomLoginPage(http.Controller):
#     @http.route('/custom_login_page/custom_login_page', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_login_page/custom_login_page/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_login_page.listing', {
#             'root': '/custom_login_page/custom_login_page',
#             'objects': http.request.env['custom_login_page.custom_login_page'].search([]),
#         })

#     @http.route('/custom_login_page/custom_login_page/objects/<model("custom_login_page.custom_login_page"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_login_page.object', {
#             'object': obj
#         })


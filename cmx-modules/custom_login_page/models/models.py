# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_login_page(models.Model):
#     _name = 'custom_login_page.custom_login_page'
#     _description = 'custom_login_page.custom_login_page'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


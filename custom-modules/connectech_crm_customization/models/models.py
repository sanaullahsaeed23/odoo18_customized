# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class connectech_crm_customization(models.Model):
#     _name = 'connectech_crm_customization.connectech_crm_customization'
#     _description = 'connectech_crm_customization.connectech_crm_customization'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


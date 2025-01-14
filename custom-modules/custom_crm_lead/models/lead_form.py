from odoo import models, fields

class CustomLead(models.Model):
    _inherit = 'crm.lead'

    product_id = fields.Many2one('product.product', string="Requested Product")
    product_name = fields.Char(string="Product Name")
    qty = fields.Integer(string="Quantity")
    size = fields.Char(string="Size")
    technical_specs = fields.Text(string="Technical Specifications")
    product_color = fields.Char(string="Product Color")
    material = fields.Char(string="Material")
    dimensions = fields.Char(string="Dimensions")
    weight = fields.Float(string="Weight")
    image = fields.Binary(string="Product Image")


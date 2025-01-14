from odoo import http
from odoo.http import request

class WebsiteRequestQuote(http.Controller):

    @http.route('/request/quote', type='http', auth="public", website=True)
    def request_quote_form(self, product_id=None, **kwargs):
        # Fetch the product using the product_id from the URL parameter
        product = request.env['product.product'].sudo().browse(int(product_id)) if product_id else None

        # Render the form page with product details
        return request.render('website_customizations.request_quote_page', {
            'product': product,
        })

    @http.route('/request/quote/submit', type='http', auth="public", website=True, csrf=True)
    def submit_quote(self, **kwargs):
        # Retrieve form data
        product_id = kwargs.get('product_id')
        product_name = None
        if product_id:
            product = request.env['product.product'].sudo().browse(int(product_id))
            product_name = product.display_name

        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        message = kwargs.get('message')

        # Check if a customer already exists
        customer = request.env['res.partner'].sudo().search([('email', '=', email)], limit=1)

        if not customer:
            # Create a new customer
            customer = request.env['res.partner'].sudo().create({
                'name': name,
                'email': email,
                'phone': phone,
                'customer_rank': 1,  # Mark as a customer
            })
        else:
            # Update existing customer details if needed
            customer.sudo().write({
                'name': name,
                'phone': phone,
            })

        lead_vals = {
            'name': f"{name} requested quotation for {product_name}",
            'partner_id': customer.id,
            'contact_name': name,
            'email_from': email,
            'phone': phone,
            'description': message,
            'product_id': int(product_id) if product_id else None,  # Link the product
        }

        request.env['crm.lead'].sudo().create(lead_vals)

        # Redirect to a thank-you page
        return request.render('website_customizations.thank_you_page')

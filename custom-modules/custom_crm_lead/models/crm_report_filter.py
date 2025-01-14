
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class CrmLeadReportWizard(models.TransientModel):
    _name = 'crm.lead.report.wizard'
    _description = 'CRM Lead Report Wizard'

    stage_id = fields.Many2one('crm.stage', string='Stage', help="Filter by the lead stage")
    country_id = fields.Many2one('res.country', string='Country', help="Filter by the lead country")
    min_revenue = fields.Float(string='Minimum Expected Revenue', help="Filter by minimum expected revenue")
    max_revenue = fields.Float(string='Maximum Expected Revenue', help="Filter by maximum expected revenue")
    assigned_user_id = fields.Many2one('res.users', string='Assigned User', help="Filter by assigned user")

    def generate_report(self):
        _logger.info("Generating report with the following filters:")
        _logger.info(f"Stage: {self.stage_id}")
        _logger.info(f"Country: {self.country_id}")
        _logger.info(f"Minimum Revenue: {self.min_revenue}")
        _logger.info(f"Maximum Revenue: {self.max_revenue}")
        _logger.info(f"Assigned User: {self.assigned_user_id}")

        # Initialize the domain to filter records
        domain = []

        if self.stage_id:
            domain.append(('stage_id', '=', self.stage_id.id))
        if self.country_id:
            domain.append(('country_id', '=', self.country_id.id))
        if self.min_revenue:
            domain.append(('expected_revenue', '>=', self.min_revenue))
        if self.max_revenue:
            domain.append(('expected_revenue', '<=', self.max_revenue))
        if self.assigned_user_id:
            domain.append(('user_id', '=', self.assigned_user_id.id))

        _logger.info(f"Generated domain: {domain}")

        # Search leads based on the domain
        leads = self.env['crm.lead'].search(domain)
        _logger.info(f"Number of leads found: {len(leads)}")

        # Generate the report with the filtered records
        return self.env.ref('custom_crm_lead.action_report_print_crm_leads').report_action(leads)

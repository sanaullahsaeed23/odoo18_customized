from odoo import models, api

class ReportCrmLead(models.AbstractModel):
    _name = 'report.custom_crm_lead.report_crm_lead_template'
    _description = 'CRM Lead Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Default behavior if no docids are provided
        if not docids:
            # Define default filter: e.g., active leads or leads created in the last 30 days
            docs = self.env['crm.lead'].search([])  # Customize the domain as needed
            print("No specific docids provided. Returning all leads.")
        else:
            # Fetch records based on docids
            docs = self.env['crm.lead'].browse(docids)

        return {
            'doc_ids': docids or docs.ids,
            'doc_model': 'crm.lead',
            'docs': docs,
            'data': data or {},
        }

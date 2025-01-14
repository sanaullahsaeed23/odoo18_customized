import logging
from odoo import models, api, fields

_logger = logging.getLogger(__name__)


class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    def write(self, vals):
        """
        Override write method to send email notifications when the lead's stage changes.
        """
        if 'stage_id' in vals:
            # Retrieve the email template
            mail_template = self.env.ref(
                'connectech_crm_customization.email_lead_stage_change_template',
                raise_if_not_found=False
            )

            if not mail_template:
                _logger.error("ERROR: Email template 'email_lead_stage_change_template' not found.")
                return super(CrmLeadInherit, self).write(vals)

            # Fetch all CRM administrators' partner IDs
            crm_admins = self.env['res.users'].search([
                ('groups_id', 'in', self.env.ref('sales_team.group_sale_manager').id),
                ('email', '!=', False)  # Ensure users have valid email addresses
            ])

            admin_emails = crm_admins.mapped('email')
            if not admin_emails:
                _logger.warning("WARNING: No valid CRM admin email addresses found.")
                return super(CrmLeadInherit, self).write(vals)

            for lead in self:
                old_stage = lead.stage_id.name or "Undefined"
                new_stage = self.env['crm.stage'].browse(vals['stage_id']).name or "Undefined"

                # Check if the stage actually changed
                if old_stage != new_stage:
                    _logger.info(f"INFO: Lead '{lead.name}' stage changed from '{old_stage}' to '{new_stage}'.")

                    try:
                        # Prepare context with dynamic variables
                        email_context = {
                            'lead_name': lead.name,
                            'old_stage': old_stage,
                            'new_stage': new_stage,
                            'responsible_user': lead.user_id.name or "Team Member",
                        }

                        # Send email
                        mail_template.with_context(email_context).send_mail(lead.id, force_send=True)

                        _logger.info(f"INFO: Email successfully sent to: {', '.join(admin_emails)} "
                                     f"for lead '{lead.name}'.{email_context}")
                    except Exception as e:
                        _logger.error(f"ERROR: Failed to send email for lead '{lead.name}': {str(e)}")

        # Call the original write method
        return super(CrmLeadInherit, self).write(vals)

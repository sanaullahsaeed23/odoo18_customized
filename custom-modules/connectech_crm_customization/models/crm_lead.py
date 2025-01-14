# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # @api.onchange('stage_id')
    # def _onchange_stage_id_ach(self):
    #     for rec in self:
    #         if rec.stage_id.mail_template_id:
    #             try:
    #                 email_values = {
    #                     'auto_delete': True,
    #                     'message_type': 'comment',
    #                     'is_notification': True,
    #                 }
    #                 mail_id = rec.stage_id.mail_template_id.send_mail(rec._origin.id, force_send=True, raise_exception=True, email_values=email_values)
    #             except:
    #                 print('Not send')

    def write(self, values):
        # Check if stage_id is being updated
        if 'stage_id' in values:
            for rec in self:
                # Log the stage change
                _logger.info(f"Stage changed for lead: {rec.name}, New Stage ID: {values['stage_id']}")

                # Fetch the new stage
                new_stage = self.env['crm.stage'].browse(values['stage_id'])

                # Check if the stage has an email template
                if new_stage.mail_template_id:
                    try:
                        _logger.info(f"Sending email using template: {new_stage.mail_template_id.name}")

                        # Prepare email values
                        email_values = {
                            'auto_delete': True,
                            'message_type': 'comment',
                            'is_notification': True,
                        }

                        # Send email
                        mail_id = new_stage.mail_template_id.send_mail(
                            rec.id,
                            force_send=True,
                            raise_exception=True,
                            email_values=email_values
                        )

                        # Log success
                        _logger.info(f"Email sent successfully with mail_id: {mail_id}")
                        _logger.info(f"Sending email for record ID: {rec.id}")
                    except Exception as e:
                        # Log errors
                        _logger.error(f"Error sending email for lead {rec.name}: {e}")
        # Call the original write method
        return super(CrmLead, self).write(values)
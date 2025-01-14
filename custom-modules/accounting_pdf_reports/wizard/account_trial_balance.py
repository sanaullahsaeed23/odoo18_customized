# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import io  # Importing io to handle in-memory file operations
import base64
from datetime import datetime
import logging
import json


_logger = logging.getLogger(__name__)


class AccountBalanceReport(models.TransientModel):
    _name = 'account.balance.report'
    _inherit = "account.common.account.report"
    _description = 'Trial Balance Report'

    journal_ids = fields.Many2many('account.journal', 'account_balance_report_journal_rel',
                                   'account_id', 'journal_id', 
                                   string='Journals', required=True, default=[])
    analytic_account_ids = fields.Many2many('account.analytic.account',
                                            'account_trial_balance_analytic_rel',
                                            string='Analytic Accounts')

    def _get_report_data(self, data):
        data = self.pre_print_report(data)
        records = self.env[data['model']].browse(data.get('ids', []))
        return records, data

    def _print_report(self, data):
        records, data = self._get_report_data(data)
        # _logger.info("Fetched report records for PDF download: %s", records)
        return self.env.ref('accounting_pdf_reports.action_report_trial_balance').report_action(records, data=data)



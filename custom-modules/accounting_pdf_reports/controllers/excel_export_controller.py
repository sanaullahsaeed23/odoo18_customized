from odoo import http
from odoo.http import request
import logging
import base64
import io
import xlsxwriter
from datetime import datetime

# Initialize logger
_logger = logging.getLogger(__name__)

class ExcelExportController(http.Controller):

    @http.route('/web/export_trial_balance_excel', type='http', auth='user')
    def export_trial_balance_excel(self, id=None, model=None):
        # _logger.info("Excel export initiated for model=%s with id=%s", model, id)

        if not id or not model:
            _logger.error("Missing required parameters: id=%s, model=%s", id, model)
            return request.not_found()

        wizard = request.env[model].browse(int(id))
        if not wizard.exists():
            _logger.error("No wizard found for model=%s with id=%s", model, id)
            return request.not_found()

        try:
            data = {
                'form': wizard.read(['date_from', 'date_to', 'journal_ids', 'target_move', 'company_id'])[0]
            }
            data['form']['display_account'] = data['form'].get('display_account', 'all')
            data['form']['analytic_account_ids'] = data['form'].get('analytic_account_ids', [])
            data['form']['used_context'] = wizard._build_contexts({'form': data['form']})

            # Add active_model to the context
            request.env.context = dict(request.env.context, active_model=model)
            # _logger.info("Updated context with active_model: %s", model)

            # _logger.info("Final data passed to _get_report_values: %s", data)

            # Fetch report values
            report_values = request.env['report.accounting_pdf_reports.report_trialbalance']._get_report_values(
                docids=wizard.ids, data=data
            )
            # _logger.info("Report values fetched successfully.")
            accounts = report_values['Accounts']
            journals = report_values['print_journal']
            analytic_accounts = report_values.get('analytic_accounts', [])

            # Deduplicate accounts
            unique_accounts = []
            seen = set()
            for account in accounts:
                account_key = (
                account['code'], account['name'], account['debit'], account['credit'], account['balance'])
                if account_key not in seen:
                    unique_accounts.append(account)
                    seen.add(account_key)

            accounts = unique_accounts
            # _logger.info("Filtered unique accounts: %s", accounts)

        except Exception as e:
            _logger.exception("Error preparing report values: %s", e)
            return request.not_found()

        # Create Excel file in memory
        try:
            # Filter accounts with movements and deduplicate them
            accounts_with_movements = [
                account for account in accounts
                if account['debit'] != 0.0 or account['credit'] != 0.0 or account['balance'] != 0.0
            ]

            unique_accounts = {}
            for account in accounts_with_movements:
                if account['code'] not in unique_accounts or (
                        account['debit'] != 0.0 or account['credit'] != 0.0 or account['balance'] != 0.0
                ):
                    unique_accounts[account['code']] = account

            deduplicated_accounts = list(unique_accounts.values())

            # Create Excel file
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            sheet = workbook.add_worksheet('Trial Balance')

            bold = workbook.add_format({'bold': True})
            currency_format = workbook.add_format({'num_format': '#,##0.00'})

            # Header
            sheet.merge_range('A1:E1', "OSLO power and energy company PVT LTD", bold)
            sheet.merge_range('A2:E2', "Trial Balance", bold)
            sheet.write('A3', 'Date:', bold)
            sheet.write('B3', f"{data['form'].get('date_from', '')} to {data['form'].get('date_to', '')}")
            sheet.write('A4', 'Display Account:', bold)
            sheet.write('B4', "With movements")
            sheet.write('A5', 'Target Moves:', bold)
            sheet.write('B5', "All Posted Entries")
            sheet.write('A6', 'Journals:', bold)
            sheet.write('B6', ', '.join(journals))
            sheet.write('A7', 'Analytic Accounts:', bold)
            sheet.write('B7', ', '.join(analytic_accounts))

            # Table Header
            headers = ['Code', 'Account', 'Debit', 'Credit', 'Balance']
            for col, header in enumerate(headers):
                sheet.write(8, col, header, bold)

            # Populate rows
            row = 9
            for account in deduplicated_accounts:
                sheet.write(row, 0, account['code'])
                sheet.write(row, 1, account['name'])
                sheet.write(row, 2, account['debit'], currency_format)
                sheet.write(row, 3, account['credit'], currency_format)
                sheet.write(row, 4, account['balance'], currency_format)
                row += 1

            workbook.close()

        except Exception as e:
            _logger.exception("Error generating Excel file: %s", e)
            return request.not_found()

        # Return the Excel file
        try:
            output.seek(0)
            xls_data = output.read()
            output.close()

            filename = f"Trial_Balance_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
            # _logger.info("Excel file generated successfully: %s", filename)
            return request.make_response(
                xls_data,
                headers=[
                    ('Content-Type', 'application/vnd.ms-excel'),
                    ('Content-Disposition', f'attachment; filename={filename}')
                ],
            )
        except Exception as e:
            _logger.exception("Error returning Excel file: %s", e)
            return request.not_found()
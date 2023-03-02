from odoo import models, fields, api, _


class Analysis(models.Model):
    _name = 'hr.hospital.analysis'
    _description = 'List of patient analyzes'

    name = fields.Char(required=True)
    date_analysis = fields.Date(string='Date of analysis')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    sample_type = fields.Char()
    result_analysis = fields.Text()
    
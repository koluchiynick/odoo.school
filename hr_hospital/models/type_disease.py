from odoo import models, fields


class HospitalTypeDisease(models.Model):
    _name = 'hr.hospital.type.disease'
    _description = 'Type of disease'

    name = fields.Char(required=True)
    category_id = fields.Many2one(comodel_name='hr.hospital.disease.category')

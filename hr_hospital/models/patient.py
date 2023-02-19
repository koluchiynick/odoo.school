from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patients of Hospital'

    name = fields.Char(required=True)
    birth_date = fields.Date(string='Date of birth')

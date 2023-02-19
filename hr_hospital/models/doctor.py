from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor of Hospital'

    name = fields.Char(required=True)

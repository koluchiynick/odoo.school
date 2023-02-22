from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor of Hospital'
    _inherit = 'hr.hospital.person'

    specialty = fields.Char()
    is_intern = fields.Boolean(default=False)
    mentor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                domain="[('is_intern', '=', False)]")

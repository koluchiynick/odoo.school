from odoo import models, fields, _


class Person(models.AbstractModel):
    _name = 'hr.hospital.person'
    _description = 'basic information about the person'

    name = fields.Char(string='First name', required=True)
    last_name = fields.Char(string='Last name', required=True)
    phone = fields.Char()
    email = fields.Char()
    foto = fields.Image(max_width=1920, max_height=1920)
    gender = fields.Selection(selection=[('male', _('Male')),
                                         ('female', _('Female'))],
                              default='male')
    history_personal_doctor_ids = fields.One2many(
        comodel_name='hr.hospital.history.personal.doctor',
        inverse_name='patient_id',
    )

    history_diagnosis_ids = fields.One2many(
        comodel_name='hr.hospital.diagnosis',
        inverse_name='patient_id',
    )


class ContactPerson(models.Model):
    _name = 'hr.hospital.contact.person'
    _description = 'Contact person'
    _inherit = 'hr.hospital.person'

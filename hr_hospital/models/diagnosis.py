from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'List of patient diagnoses'

    name = fields.Char(required=True)
    date_diagnosis = fields.Date(string='Date of diagnosis')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    type_disease_id = fields.Many2one(comodel_name='hr.hospital.type.disease')
    appointment = fields.Text(string='Appointment for treatment')
    comment = fields.Text(string='Doctor comment')

    @api.constrains('doctor_id')
    def checking_if_doctor_is_intern(self):
        if self.doctor_id.is_intern and not self.comment:
            raise ValidationError(_('Еhe mentor should put his/her comment.'))

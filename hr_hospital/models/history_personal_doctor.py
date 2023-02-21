from odoo import models, fields


class HistoryPersonalDoctor(models.Model):
    _name = 'hr.hospital.history.personal.doctor'
    _description = 'History of changes to the personal doctor'
    _rec_name = 'patient_id'

    appointment_date = fields.Date(string='Date of appointment')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    
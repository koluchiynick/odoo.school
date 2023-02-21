from datetime import date

from odoo import api, models, fields


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patients of Hospital'
    _inherit = 'hr.hospital.person'

    # name = fields.Char(required=True)
    birth_date = fields.Date(string='Date of birth')
    age = fields.Integer(compute='_compute_age')
    passport = fields.Char()
    contact_person_id = fields.Many2one(
        comodel_name='hr.hospital.contact.person')
    personal_doktor_id = fields.Many2one(comodel_name='hr.hospital.doctor')

    @api.depends('birth_date')
    def _compute_age(self):
        self.ensure_one
        if self.birth_date:
            odds_date = date.today() - self.birth_date
            self.age = odds_date.days // 365
        else:
            self.age = 0
    
    @api.model
    def create(self, vals):
        record = super(HospitalPatient, self).create(vals)
        if 'personal_doktor_id' in vals:
            values = {
                'appointment_date': fields.Datetime.now(),
                'patient_id': record.id,
                'doctor_id': vals['personal_doktor_id'],
                
            }
            self.env['hr.hospital.history.personal.doctor'].create(values)
        return record

    def write(self, vals):
        record = super(HospitalPatient, self).write(vals)
        if 'personal_doktor_id' in vals:
            for record in self:
                if record.personal_doktor_id != vals['personal_doktor_id']:
                    values = {
                        'appointment_date': fields.Datetime.now(),
                        'patient_id': record.id,
                        'doctor_id': vals['personal_doktor_id'],
                    }
                self.env['hr.hospital.history.personal.doctor'].create(values)
        return record

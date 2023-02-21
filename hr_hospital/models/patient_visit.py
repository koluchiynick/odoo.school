from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class HospitalPatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Visits of Hospital Patients'
    _rec_name = 'patient_id'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    visit_date = fields.Datetime(string='Date/time visit',
                                 default=fields.Datetime.now())
    type_disease_id = fields.Many2one(comodel_name='hr.hospital.type.disease')
    diagnosis_id = fields.Many2one(comodel_name='hr.hospital.diagnosis')
    active = fields.Boolean(default=True)
    is_visit_done = fields.Boolean(string='Done', default=False)

    def action_archive(self):
        for record in self:
            if record.diagnosis_id:
                raise UserError(
                    _('This visitor has already filled in the diagnosis, '
                        'archiving is not possible.'))
        return super(HospitalPatientVisit, self).action_archive()

    def unlink(self):
        for record in self:
            if record.diagnosis_id:
                raise UserError(
                    _('This visitor has already filled in the diagnosis, '
                        'delete is not possible.'))
        return super(HospitalPatientVisit, self).unlink()

    def write(self, vals):
        if 'visit_date' in vals:
            visit_date_val = vals['visit_date']
            for rec in self:
                if rec.is_visit_done and visit_date_val != rec.visit_date:
                    raise UserError(_('You cannot change the date and time of '
                        'a visit that has already taken place.'))
        if 'doctor_id' in vals:
            doctor_id_val = vals['doctor_id']
            for rec in self:
                if rec.is_visit_done and doctor_id_val != rec.doctor_id:
                    raise UserError(_('You cannot change your doctor '
                        'a visit that has already taken place.'))
        return super(HospitalPatientVisit, self).write(vals)

    @api.constrains('visit_date')
    def check_visit_time(self):
        visit_list = self.env['hr.hospital.patient.visit'].search([])
        for rec in self:
            for visit in visit_list:
                if rec.id == visit.id:
                    continue
                if rec.visit_date == visit.visit_date:
                    raise ValidationError(
                        _('There is already a record at this time'))

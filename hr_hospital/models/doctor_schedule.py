from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DoctorSchedule(models.Model):
    _name = 'hr.hospital.doctor.schedule'
    _description = 'Doctor schedule'
    _rec_name = 'doctor_id'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    admission_date = fields.Date(string='Date admission', required=True)
    start_time = fields.Float()
    end_time = fields.Float()

    @api.constrains('start_time', 'end_time')
    def check_schedule_time(self):
        schedule_list = self.env['hr.hospital.doctor.schedule'].search([])
        for rec in self:
            for schedule in schedule_list:
                if rec.id == schedule.id:
                    continue
                if rec.admission_date != schedule.admission_date:
                    continue
                if rec.start_time <= schedule.start_time <= rec.end_time:
                    raise ValidationError(_('This time is already taken'))
                if schedule.end_time >= rec.start_time >= schedule.start_time:
                    raise ValidationError(_('This time is already taken'))

from odoo import models, fields, _

from datetime import timedelta


class FillingDoctorScheduleWizard(models.TransientModel):
    _name = 'hr.hospital.filling.doctor.schedule.wizard'
    _description = 'Filling in the doctor work schedule'
    
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    start_time_even = fields.Float(string='Start Time')
    end_time_even = fields.Float(string='End Time')
    start_time_odd = fields.Float(string='Start Time')
    end_time_odd = fields.Float(string='End Time')

    def action_open_wizard(self):
        return {
            'name': _('Filling in the doctor work schedule'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hospital.filling.doctor.schedule.wizard',
            'target': 'new',            
        }

    def action_change_visit(self):
        self.ensure_one()
        current_day = self.start_date
        while current_day <= self.end_date:
            start_time = self.start_time_odd
            end_time = self.end_time_odd
            if current_day.day % 2 == 0:
                start_time = self.start_time_even
                end_time = self.end_time_even            
            self.env['hr.hospital.doctor.schedule'].create(
                {
                    'doctor_id': self.doctor_id.id,
                    'admission_date': current_day,
                    'start_time': start_time,
                    'end_time': end_time,
                })
            current_day = current_day + timedelta(days=1)

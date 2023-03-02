from odoo import models, fields, _


class ReschedulingVisitDoctorWizard(models.TransientModel):
    _name = 'hr.hospital.rescheduling.visit.doctor.wizard'
    _description = 'Rescheduling a visit to the doctor'

    patient_visit_id = fields.Many2one(
        comodel_name='hr.hospital.patient.visit',
        string='Visit',
        required=True)
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True)
    visit_date = fields.Datetime(string='Date/time visit',
                                 default=fields.Datetime.now, required=True)

    def action_open_wizard(self):
        return {
            'name': _('Rescheduling a visit to the doctor'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hospital.rescheduling.visit.doctor.wizard',
            'target': 'new',
        }

    def action_change_visit(self):
        self.ensure_one()
        self.patient_visit_id.write(
            {
                'doctor_id': self.doctor_id.id,
                'visit_date': self.visit_date,
            })

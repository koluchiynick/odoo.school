from odoo import models, fields


class ChangeDoctorWizard(models.TransientModel):
    _name = 'hr.hospital.change.doctor.wizard'
    _description = 'Change of personal doctor'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True)
    patient_ids = fields.Many2many(comodel_name='hr.hospital.patient',
                                   required=True)
    
    def action_change_doctor(self):
        self.ensure_one()
        self.patient_ids.write({'personal_doktor_id': self.doctor_id.id})

    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        res['patient_ids'] = [(6, None, self._context.get("active_ids"))]
        return res

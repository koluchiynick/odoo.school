from odoo import models, fields, _


class ChangeDoctorWizard(models.TransientModel):
    _name = 'hr.hospital.change.doctor.wizard'
    _description = 'Change of personal doctor'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True)
    patient_ids = fields.Many2many(comodel_name='hr.hospital.patient',
                                   required=True)

    def action_open_wizard(self):
        return {
            'name': _('Multi Change doctor'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hospital.change.doctor.wizard',
            'target': 'new',
        }

    def action_change_doctor(self):
        self.ensure_one()
        self.patient_ids.write({'personal_doctor_id': self.doctor_id.id})

    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if self._context.get("active_ids"):
            res['patient_ids'] = [(6, None, self._context.get("active_ids"))]
        return res

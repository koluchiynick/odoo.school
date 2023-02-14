import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HospitalPatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Visits of Hospital Patients'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one('hr.hospital.patient')
    visit_date = fields.Date()
    type_disease_id = fields.Many2one('hr.hospital.type.disease')

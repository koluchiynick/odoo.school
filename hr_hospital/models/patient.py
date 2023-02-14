import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patients of Hospital'  # Бажано додавати більш розгорнутий опис

    name = fields.Char("Name", required=True)  # Кожний параметр краще вказувати з доданням назви параметру
    birth_date = fields.Date(string='Date of birth')  # Кожний параметр краще вказувати з доданням назви параметру

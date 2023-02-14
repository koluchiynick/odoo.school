import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)  # Логування не використовується у поточному файлі


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(required=True)  # Кожний параметр краще вказувати з доданням назви параметру

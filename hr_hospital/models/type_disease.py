import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HospitalTypeDisease(models.Model):
    _name = 'hr.hospital.type.disease'
    _description = 'Type of disease'

    name = fields.Char("Name", required=True)
    
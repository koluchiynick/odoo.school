import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doсtor'

    name = fields.Char("Name", required=True)
    
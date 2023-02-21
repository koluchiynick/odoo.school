from odoo import models, fields


class DiseaseReportWizard(models.TransientModel):
    _name = 'hr.hospital.disease.report.wizard'
    _description = 'Disease report'

    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    def action_print_disease_report(self):
        self.ensure_one()
        domain_line = [
            ('date_diagnosis', '>=', self.start_date),
            ('date_diagnosis', '<=', self.end_date),
        ]
        diagnosis_list = self.env['hr.hospital.diagnosis'].search(domain_line)
        report_res = []
        for rec in diagnosis_list.mapped('type_disease_id'):
            filter_diagnosis = diagnosis_list.filtered(
                lambda r: r.type_disease_id == rec)
            list_diagnosis = []
            for diagnosis in filter_diagnosis:
                list_diagnosis.append(diagnosis.name)

            report_res.append({
                'disease': rec.name,
                'count': len(filter_diagnosis),
                'diagnosis': list_diagnosis,
            })
        return self.env.ref('hr_hospital.action_disease_report').report_action(
            self, data={'data_report': report_res})

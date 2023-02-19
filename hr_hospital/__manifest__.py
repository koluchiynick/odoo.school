{
    'name': "hr_hospital",
    'summary': """
        Hospital management. 
        Management of records of doctors' visits with patients""",
    'author': "Mykola Ostroukh",
    'website': "https://github.com/koluchiynick",
    'category': 'Customizations',
    'version': '15.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_type_disease_views.xml',
        'views/hr_hospital_patient_visit_views.xml',
        'data/hr_hospital_type_disease_data.xml',
    ],
    'demo': [
        'data/hr_hospital_doctor_demo.xml',
        'data/hr_hospital_patient_demo.xml',
    ],
    'application': True,
}

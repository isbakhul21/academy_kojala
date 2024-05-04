{
    'name': 'Academy Kojala',
    'summary': 'Modul ini di gunakan untuk Mangement Perkuliahan',
    'description': ' Modul ini mengatur informasi tentang Mahasiswa, Dosen, dan Tenaga Pendidik',
    'sequence': -99,
    'author': 'Koding Jalanan Team',
    'website': 'kodingjalanan.com',
    'category': 'Education',
    'depends': ['base','mail'],
    'data': [
        #security
        'security/ir.model.access.csv',

        #views
        'views/academy_student_view.xml',
        'views/student_female.xml',
        'views/thesis_guidance.xml',

        #data
        'data/ir_ui_menu.xml',
    ],
    'application': True,
    'instalable': True,
    'license': 'LGPL-3'
}
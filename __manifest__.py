{
    'name': 'School System',
    'version': '1.0',
    'summary': 'manage the student courses and grades',
    'category': 'Tools',
    'author': 'Nayera',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/course_registration_menu.xml',
        'views/courses_menu.xml',
        'views/student_profile_menu.xml',
    ],

    'installable': True,
    'application': True,
}
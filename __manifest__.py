{
    'name': 'School System',
    'version': '1.0',
    'summary': 'manage the student courses and grades',
    'category': 'Tools',
    'author': 'Nayera',

    'depends': ['base','web','website','mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/course_registration_menu.xml',
        'views/courses_menu.xml',
        'views/role_selection.xml',
        'views/student_dashboard_menu.xml',
        'views/student_profile_menu.xml',
        'views/teacher_profile_menu.xml',
        'report/student_report.xml'
    ],

    'installable': True,
    'application': True,
}
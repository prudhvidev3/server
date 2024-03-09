{
    'name':"Student Record",
    'summary':"""this moudle will add a record to store students details""",
    'description':"""this module will add a record to store student details""",
    'depends':[],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/branch_view.xml',
        'views/student_view.xml',
        'views/department_view.xml'
            ],
    'installable':True,
    'auto_install':False,
    'application':False,
}
from odoo import models, api, _, fields
class studentrecord(models.Model):
    _name = "student.student"

    def _get_nationality(self):
        nationality = self.env['res.country'].search([('code','=','IN')])
        return nationality

    # def name_get(self):
    #     result =[]
    #     for student in self:
    #         name= student.middle_name +' '+student.last_name
    #         result.append((student.id , name))
    #     return result

    first_name = fields.Selection([('mr', 'MR'),('m', 'MISS'),('O','OTHER')], string='First_Name')
    middle_name = fields.Char(string='Middle Name', required=True)
    last_name= fields.Char(string='Last Name', required=True)
    photo = fields.Binary(string='Photo')
    student_age = fields.Integer(string='Age')
    student_dob = fields.Date(string='Date of Birth')
    student_gender = fields.Selection([('m', 'Male'), ('f', 'Female'),('o','Other')], string='Gender')
    student_blood_group = fields.Selection(
        [('A+','A+ve'), ('B+','B+ve'), ('O+','O+ve'), ('AB+','AB+ve'),('A-','A-ve'),('B-','B-ve'),('O-', 'O-ve'),('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', required=True,default=_get_nationality)

class Depart(models.Model):
    _name = "department.department"

    def name_get(self):
        result =[]
        for student in self:
            name= student.middle_name +' '+student.last_name
            result.append((student.id , name))
        return result

    branch_name= fields.Char(string='Name')



class information(models.Model):
    _name="branch.branch"

    def name_get(self):
        result=[]
        for branch in self:
            if branch.branch:
                name=branch.student_name.middle_name +' ' +branch.student_name.last_name +'-'+ branch.branch
            else:
                name = branch.student_name.middle_name + ' ' + branch.student_name.last_name
            result.append((branch.id , name))
        return result

    student_name=fields.Many2one('student.student', string='Student Name', required=True)
    phone_number= fields.Char(string='Phone Number')
    branch=fields.Many2one([('ECE','ECE'),('EEE','EEE'),('MECHANICAL','MECHANICAL'),('CIVIL','CIVIL'),('CSE','CSE')],string='Branch',default="ECE")
    joining_Date=fields.Date(string='Joining Date')
    address=fields.Char(string='address')



from odoo import api, fields, models
from datetime import date


class AcademyStudent(models.Model):
    _name = "academy.student"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Academy Student'

    @api.depends('birthday')
    def _compute_age(self):
        for this in self:
            year = date.today().year
            if this.birthday:
                this.age = year - this.birthday.year
            else:
                this.age = 0


    nim = fields.Integer(string="NIM",tracking=True)
    name = fields.Char(string="Name" ,tracking=True)
    email = fields.Char(string="Email" ,tracking=True)
    no_phone = fields.Integer(string="Phone" ,tracking=True)
    birthday = fields.Date(string="Birthday")
    age = fields.Integer(string="Age",compute=_compute_age,store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], default='male')
    active = fields.Boolean(string="Active", default=True)
    profile_picture_student = fields.Image(string=" Foto Profil MAHASISWA")

    partner_id = fields.Many2one("res.partner", string="Friend")
    thesis_guidance_id = fields.Many2one("thesis.guidance", string="Thesis")



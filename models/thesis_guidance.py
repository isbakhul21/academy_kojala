from odoo import api, fields, models


class ThesisGuidance(models.Model):
    _name = "thesis.guidance"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Thesis Guidance'
    _rec_name = 'student_id'

    student_id = fields.Many2one("academy.student", string="Name")
    guidance_date = fields.Date(string="Guidance Date", default=fields.Date.context_today)
    accept_date =  fields.Datetime(string="Accept Date", default=fields.Datetime.now)
    notes = fields.Html(string="Notes")
    priority = fields.Selection([
        ('0','Lazy'),
        ('1','Normal'),
        ('2','Smart'),
        ('3','Very Smart')], string="Priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('consultation', 'In Consultation'),
        ('proposal', 'Proposal'),
        ('test_thesis', 'Test Thesis'),
        ('graduate', 'Graduate')], string="State")


    gender = fields.Selection(related='student_id.gender')
    nim = fields.Integer(string="NIM",tracking=True)

    @api.onchange('student_id')
    def onchange_student_id(self):
        self.nim = self.student_id.nim


    def action_test(self):
        print("BUTTON INI DI KLIK BROOOOHHHH!!!!")
        return {
            'effect': {
                'fadeout': 'fast',
                'message': 'HOREEEEE BUTTTON NYA DI CLICK, KAMU KEREN !',
                'type': 'rainbow_man',
            }
        }




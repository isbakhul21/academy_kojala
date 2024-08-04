from odoo import api, fields, models


class ThesisGuidance(models.Model):
    _name = "thesis.guidance"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Thesis Guidance'
    _rec_name = 'student_id'

    student_id = fields.Many2one("academy.student", string="Name")
    guidance_date = fields.Date(string="Guidance Date", default=fields.Date.context_today)
    accept_date = fields.Datetime(string="Accept Date", default=fields.Datetime.now)
    notes = fields.Html(string="Notes")
    date_consultation = fields.Date(string="Date Consultation")
    date_proposal = fields.Date(string="Date Proposal")
    date_test_thesis = fields.Date(string="Date Test Thesis")
    date_graduate = fields.Date(string="Date Graduate")

    # LineGuidance
    thesis_guidance_line_ids = fields.One2many('thesis.guidance.line','thesis_guidance_id',string="Thesis Guidance Line")
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
        ('graduate', 'Graduate')], string="State", default='draft')


    gender = fields.Selection(related='student_id.gender')
    nim = fields.Integer(string="NIM",tracking=True)
    lecturer_id = fields.Many2one('res.users', string="Lecture")
    hide_price_subject = fields.Boolean(string="Sembunyikan Biaya Mata Kuliah ?")

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
    def action_consultation(self):
        for this in self:
            this.state = 'consultation'

    def action_proposal(self):
        for this in self:
            this.state = 'proposal'

    def action_thesis(self):
        for this in self:
            this.state = 'test_thesis'

    def action_graduate(self):
        for this in self:
            this.state = 'graduate'


class ThesisGuidanceLine(models.Model):
    _name = "thesis.guidance.line"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Thesis Guidance Line'

    thesis_guidance_id = fields.Many2one('thesis.guidance',string="Thesis Guidance")

    subject = fields.Char(string="Mata Kuliah")
    lecturer = fields.Char(string="Dosen")
    price_subject = fields.Float(string="BIAYA MATA KULIAH")














class HewanOrm(models.Model):
    _name = "hewan.orm"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'Hewan Orm'

    nama = fields.Char(string="Nama")
    umur = fields.Integer(string="Umur")


























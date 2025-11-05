# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ChessStudent(models.Model):
    _name = 'chess.student'
    _description = 'Chess Academy Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Student Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    partner_id = fields.Many2one('res.partner', string='Related Contact', ondelete='cascade')
    parent_id = fields.Many2one('res.partner', string='Parent/Guardian', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    
    # Chess specific fields
    rating = fields.Integer(string='Chess Rating', default=0)
    skill_level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ], string='Skill Level', default='beginner', tracking=True)
    
    enrollment_date = fields.Date(string='Enrollment Date', default=fields.Date.today)
    active = fields.Boolean(string='Active', default=True)
    
    lesson_ids = fields.One2many('chess.lesson', 'student_id', string='Lessons')
    lesson_count = fields.Integer(string='Lesson Count', compute='_compute_lesson_count')
    
    notes = fields.Text(string='Notes')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = fields.Date.today()
                record.age = today.year - record.date_of_birth.year
            else:
                record.age = 0

    @api.depends('lesson_ids')
    def _compute_lesson_count(self):
        for record in self:
            record.lesson_count = len(record.lesson_ids)


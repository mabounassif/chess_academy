# -*- coding: utf-8 -*-

from odoo import models, fields


class ChessCoach(models.Model):
    _name = 'chess.coach'
    _description = 'Chess Academy Coach'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Coach Name', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Related Contact', ondelete='cascade')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    
    # Chess credentials
    rating = fields.Integer(string='Chess Rating')
    title = fields.Selection([
        ('cm', 'Candidate Master'),
        ('fm', 'FIDE Master'),
        ('im', 'International Master'),
        ('gm', 'Grandmaster'),
        ('none', 'No Title'),
    ], string='FIDE Title', default='none')
    
    specialization = fields.Selection([
        ('beginner', 'Beginner Training'),
        ('intermediate', 'Intermediate Training'),
        ('advanced', 'Advanced Training'),
        ('tournament', 'Tournament Preparation'),
        ('opening', 'Opening Theory'),
        ('endgame', 'Endgame Training'),
    ], string='Specialization')
    
    hourly_rate = fields.Float(string='Hourly Rate')
    active = fields.Boolean(string='Active', default=True)
    
    lesson_ids = fields.One2many('chess.lesson', 'coach_id', string='Lessons')
    
    bio = fields.Text(string='Biography')
    notes = fields.Text(string='Internal Notes')


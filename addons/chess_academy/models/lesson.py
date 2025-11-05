# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ChessLesson(models.Model):
    _name = 'chess.lesson'
    _description = 'Chess Lesson'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Lesson', compute='_compute_name', store=True)
    student_id = fields.Many2one('chess.student', string='Student', required=True, tracking=True)
    coach_id = fields.Many2one('chess.coach', string='Coach', required=True, tracking=True)
    
    date = fields.Datetime(string='Date & Time', required=True, tracking=True)
    duration = fields.Float(string='Duration (hours)', default=1.0)
    
    lesson_type = fields.Selection([
        ('individual', 'Individual'),
        ('group', 'Group'),
        ('online', 'Online'),
        ('tournament', 'Tournament Prep'),
    ], string='Lesson Type', default='individual', required=True)
    
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ], string='Status', default='scheduled', tracking=True)
    
    topics_covered = fields.Text(string='Topics Covered')
    homework = fields.Text(string='Homework Assigned')
    progress_notes = fields.Text(string='Progress Notes')
    
    calendar_event_id = fields.Many2one('calendar.event', string='Calendar Event')

    @api.depends('student_id', 'coach_id', 'date')
    def _compute_name(self):
        for record in self:
            if record.student_id and record.coach_id and record.date:
                record.name = f"{record.student_id.name} - {record.coach_id.name} ({fields.Date.to_string(record.date)})"
            else:
                record.name = "New Lesson"


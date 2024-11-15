# -*- coding: utf-8 -*-
from odoo import models, fields

class RegistroTarea(models.Model):
    _name = 'agenda.registro.tarea'
    _description = 'Registro de Fotos de Tareas Revisadas'

    tarea_revisada_id = fields.Many2one(
        'agenda.alumno_revisado',
        string='Tarea Revisada',
        ondelete='cascade',
        required=True,
        help="Registro de la tarea revisada para el alumno"
    )

    foto_tarea = fields.Binary(
        string="Foto de la Tarea",
        help="Foto de la tarea que se capturó desde la aplicación móvil"
    )

    texto_original = fields.Text(
        string="Texto Extraído",
        help="Texto extraído de la foto de la tarea mediante el microservicio"
    )

    texto_ia = fields.Text(
        string="Texto generado con ia",
        help="Texto generado por la IA en base a la tarea revisada"
    )

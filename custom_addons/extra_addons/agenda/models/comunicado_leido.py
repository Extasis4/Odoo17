# -*- coding: utf-8 -*-
from odoo import models, fields

class ComunicadoLeido(models.Model):
    _name = 'agenda.comunicado.leido'

    _description = "Comunicado Leído"

    # Campos básicos para controlar la lectura

    comunicado_id = fields.Many2one(
        'agenda.comunicado', 
        string='Comunicado', 
        ondelete='cascade', 
        required=True,
        help="Comunicado que ha sido leído."
    )
    destinatario_id = fields.Many2one(
        'res.users', 
        string='Destinatario', 
        required=True,
        help="Usuario que leyó el comunicado."
    )
    fecha_lectura = fields.Datetime(
        string='Fecha de Lectura', 
        default=fields.Datetime.now, 
        readonly=True,
        help="Fecha y hora en que el destinatario leyó el comunicado."
    )

    # Relación al modelo de envío para rastreo
    envio_id = fields.Many2one(
        'agenda.comunicado.enviado',
        string='Envío',
        ondelete='cascade',
        help="Registro de envío relacionado."
    )

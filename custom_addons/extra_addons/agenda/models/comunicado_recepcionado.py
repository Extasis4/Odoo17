# -*- coding: utf-8 -*-
from odoo import models, fields

class ComunicadoRecepcionado(models.Model):
    _name = 'agenda.comunicado.recepcionado'
    _description = 'Comunicado Recepcionado'

    comunicado_id = fields.Many2one(
        'agenda.comunicado', 
        string='Comunicado', 
        ondelete='cascade', 
        required=True,
        help="Comunicado que ha sido recepcionado."
    )
    destinatario_id = fields.Many2one(
        'res.users', 
        string='Destinatario', 
        required=True,
        help="Usuario que recepcionó el comunicado."
    )
    fecha_recepcion = fields.Datetime(
        string='Fecha de Recepción', 
        default=fields.Datetime.now, 
        readonly=True,
        help="Fecha y hora en que el destinatario recepcionó el comunicado."
    )
    
    # Relación al modelo de envío para rastreo
    envio_id = fields.Many2one(
        'agenda.comunicado.enviado',
        string='Envío',
        ondelete='cascade',
        help="Registro de envío relacionado."
    )

# -*- coding: utf-8 -*-
from odoo import models, fields

class ComunicadoEnviado(models.Model):
    _name = 'agenda.comunicado.enviado'
    _description = 'Comunicado Enviado'

    comunicado_id = fields.Many2one(
        'agenda.comunicado', 
        string='Comunicado', 
        ondelete='cascade')
    
    destinatario_id = fields.Many2one(
        'res.users', 
        string='Destinatario', 
        required=True,
        help="Usuario que recibió el comunicado."
    )
    fecha_envio = fields.Datetime(
        string='Fecha de Envío', 
        default=fields.Datetime.now, 
        readonly=True,
        help="Fecha y hora en que se envió el comunicado."
    )

    recepcionado_id = fields.One2many(
        'agenda.comunicado.recepcionado',
        'envio_id',
        string="Recepción"
    )
    leido_ids = fields.One2many(
        'agenda.comunicado.leido',
        'envio_id',
        string="Lecturas"
    )
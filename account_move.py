from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    # cfed_nms_sale_id = fields.Many2one('cfed.retail.point.sale.nms', string="Sale Ref")
    is_nms_sale_payment = fields.Boolean()
    is_nms_cfed_sale_move = fields.Boolean('Sale Customer bill')
    nms_sale_number = fields.Char()
    nms_voucher_type = fields.Selection([
        ('Sales', 'Sales'),
        ('Purchase', 'Purchase'),
        ('Debit_Note', 'Debit Note Voucher')
    ])
    nms_purchase_id = fields.Many2one('purchase.order')
    nms_invoice_payment_id = fields.Many2one('account.move')
    nms_purchase_payment_id = fields.Many2one('purchase.order')
    nms_advance_payment_id = fields.Many2one('nms.advance.payment')
    is_nms_bill = fields.Boolean()
    general_discount = fields.Float("Total Discount")
    roundoff_value = fields.Float("Roundoff value")
    global_discount = fields.Float()
    final_amount = fields.Float()
    amount = fields.Float()
    stock_nms_in_out_entry_id = fields.Many2one('nms.transfer.in.out','Stock In/Out Entry')

    # @api.depends('invoice_line_ids', 'invoice_line_ids.discount_amount', 'global_discount', 'roundoff_value',
    #              'general_discount', 'amount_total', 'amount')
    # def compute_total_discount(self):
    #     for rec in self:
    #         discount = 0.0
    #         for line in rec.invoice_line_ids:
    #             discount += line.discount_amount
    #         rec.update({
    #             'general_discount': discount
    #         })
    #         rec.amount_total = rec.amount_total - rec.general_discount
    #         rec.amount = rec.amount_total - rec.global_discount
    #         rec.final_amount = rec.amount - rec.roundoff_value


class NmsAccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Integer(string="Discount")


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # nms_cfed_sale_line_id = fields.Many2one('cfed.retail.sale.line.nms', string="Sale Line", ondelete='set null',
    #                                         index=True)
    # nms_cfed_sale_id = fields.Many2one('cfed.retail.point.sale.nms', 'Sale Order')

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[
        ('pending_approval', 'Pending Approval'),
        ('rejected', 'Rejected')
    ])

    discount_approval_required = fields.Boolean(
        string='Discount Approval Required', compute='_compute_discount_approval_required', store=True)

    @api.depends('order_line.discount')
    def _compute_discount_approval_required(self):
        """Check if any line in the sale order exceeds 15% discount."""
        for order in self:
            order.discount_approval_required = any(
                line.discount > 15 for line in order.order_line
            )

    def action_confirm(self):
        """Override the confirm action to handle discount approvals."""
        if self.discount_approval_required:
            self.state = 'pending_approval'
        else:
            super(SaleOrder, self).action_confirm()

    def action_approve_order(self):
        """Manager approves the order."""
        self.state = 'sale'

    def action_reject_order(self):
        """Manager rejects the order."""
        self.state = 'rejected'
        raise UserError(_('The sale order has been rejected.'))

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount = fields.Float(string='Discount (%)', default=0.0)

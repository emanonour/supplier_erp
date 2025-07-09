from odoo import models, fields

class SupplierERP(models.Model):
    _name = 'supplier.erp'
    _description = 'Supplier ERP Custom Model'

    supplier_id = fields.Char(string="Supplier ID", required=True)
    name = fields.Char(string="Supplier Name", required=True)
    website = fields.Char(string="Website Link")
    presence_worldwide = fields.Text(string="Presence in Other Countries")

    business_category = fields.Selection([
        ('service', 'Service Provider'),
        ('materials', 'Materials Supplier'),
        ('both', 'Service & Materials Supplier')
    ], string="Supplier Business Category", required=True)

    business_type = fields.Text(string="Supplier Business Type", required=True)

    supplier_type = fields.Selection([
        ('qast', 'QAST Staff'),
        ('customer', 'Customer'),
        ('supplier', 'Supplier'),
        ('man', 'Man'),
        ('vendor', 'Vendor'),
        ('individual', 'Individual'),
        ('consult', 'Consult')
    ], string="Supplier Type", required=True)

    supplier_ranking = fields.Selection([
        ('rank1', 'Rank-1'),
        ('rank2', 'Rank-2'),
        ('rank3', 'Rank-3'),
        ('rank4', 'Rank-4'),
        ('rank5', 'Rank-5'),
        ('rank6', 'Rank-6'),
        ('rank7', 'Rank-7'),
    ], string="Supplier Ranking", required=True)

    account_payable_id = fields.Many2one('account.account', string="Supplier Account Payable", required=True)
    vendor_advance_account_id = fields.Many2one('account.account', string="Vendor Advance Payment Account", required=True)

    tpra_certified = fields.Boolean(string="TPRA Certified?")
    tpra_cert_no = fields.Char(string="TPRA Certificate No")
    tpra_cert_expiry = fields.Date(string="TPRA Certificate Expiry Date")
    tpra_cert_attachment = fields.Binary(string="TPRA Certificate Attachment")

    tax_certified = fields.Boolean(string="TAX Certified?")
    tax_cert_no = fields.Char(string="TAX Certificate No")
    tax_cert_expiry = fields.Date(string="TAX Certificate Expiry Date")
    tax_cert_attachment = fields.Binary(string="TAX Certificate Attachment")

    account_no = fields.Char(string="Account Number", required=True)

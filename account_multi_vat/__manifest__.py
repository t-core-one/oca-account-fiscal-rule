# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Multi Vat",
    "summary": """
        Allows setting multiple VAT numbers on any partner and select the right one
        depending on the fiscal position and delivery address of the invoice.""",
    "version": "15.0.1.0.0",
    "development_status": "Beta",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "maintainers": ["ThomasBinsfeld"],
    "website": "https://github.com/OCA/account-fiscal-rule",
    "depends": ["account", "base_vat", "partner_identification"],
    "data": [
        "views/account_tax.xml",
        "data/res_partner_id_category.xml",
        "views/account_move.xml",
        "views/res_partner.xml",
        "views/account_fiscal_position.xml",
        "views/report_invoice.xml",
    ],
}

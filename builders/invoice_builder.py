class InvoiceBuilder:
    def __init__(self):
        self.invoice = {}
        self.tax_percent = 0

    def for_sale(self, sale):
        self.invoice = {
            "id_sale": sale.id,
            "client": sale.client,
            "product": sale.product,
            "subtotal": sale.total,
        }
        return self

    def with_tax(self, percent):
        self.tax_percent = percent
        taxes = self.invoice["subtotal"] * (percent / 100)
        self.invoice["total"] = self.invoice["subtotal"] + taxes
        self.invoice["taxes"] = taxes
        return self

    def build(self):
        return self.invoice

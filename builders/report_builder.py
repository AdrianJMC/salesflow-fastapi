class ReportBuilder:
    def __init__(self):
        self.sales = []
        self.report = {}

    def with_sales(self, sales):
        self.sales = sales
        return self

    def add_summary(self):
        total_sales = len(self.sales)
        total_amount = sum([s.total for s in self.sales])
        self.report["summary"] = {
            "total_sales": total_sales,
            "total_amount": total_amount
        }
        return self

    def build(self):
        self.report["data"] = [
            {"id": s.id, "client": s.client, "product": s.product, "date": s.date, "total": s.total}
            for s in self.sales
        ]
        return self.report

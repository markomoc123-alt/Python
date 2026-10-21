"""A report class that uses TransactionRecord objects."""


class RetailReport:
    def __init__(self, records):
        self.records = records

    def sales_total(self, records):
        total = 0.0
        for record in records:
            total += record.sales
        return total

    def show(self, raw_count, clean_count):
        retention = 0.0
        if raw_count > 0:
            retention = clean_count / raw_count * 100
        print(f"Valid records: {clean_count} of {raw_count}")
        print(f"Clean record retention: {retention:.2f}%")
        print(f"Gross sales: ${self.sales_total(self.records):.2f}")
        top_branch = "None"
        top_sales = -1.0
        for branch in ["A", "B"]:
            group = [r for r in self.records if r.branch == branch]
            sales = self.sales_total(group)
            if len(group) > 0 and sales > top_sales:
                top_branch = branch
                top_sales = sales
        print("Top branch:", top_branch)
        for tier in ["REGULAR", "GOLD"]:
            group = [r for r in self.records if r.tier == tier]
            print(f"{tier} sales: ${self.sales_total(group):.2f}")
        for record in self.records:
            print(f"{record.branch}: margin {record.margin:.2f}%, "
                  f"tax ${record.tax:.2f}")

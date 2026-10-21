"""Calculate results without changing the original records."""

from pipeline.schema import TransactionRecord


def calculate(record):
    fields = [record.branch, record.date, record.tier, record.items,
              record.sales, record.cost, "YES"]
    result = TransactionRecord(fields)
    rate = 0.05
    if record.branch == "B":
        rate = 0.08
    result.tax = record.sales * rate
    if record.sales > 0:
        result.margin = (record.sales - record.cost) / record.sales * 100
    return result


def transform(records):
    active = list(filter(lambda record: record.active, records))
    return list(map(calculate, active))

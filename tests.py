"""Three small tests. True means the test passed."""

from pipeline.validator import validate
from pipeline.transformer import transform
from pipeline.reporter import RetailReport


def test_validation():
    rows = [" a |2026-10-01| gold |2|100|60|yes",
            "|2026-10-01|GOLD|2|100|60|YES",
            "A|2026-02-30|GOLD|2|100|60|YES",
            "A|2026-10-01|GOLD|2|-100|60|YES", None]
    clean = validate(rows)
    return (len(clean) == 1 and clean[0].branch == "A"
            and type(clean[0].items) == int
            and type(clean[0].sales) == float)


def test_transformation():
    clean = validate(["A|2026-10-01|GOLD|2|100|60|YES",
                      "B|2026-10-01|REGULAR|1|50|30|NO"])
    active = transform(clean)
    return (len(active) == 1 and active[0].margin == 40
            and active[0].tax == 5 and clean[0].tax == 0
            and clean[0].margin == 0)


def test_total():
    clean = validate(["A|2026-10-01|GOLD|2|100|60|YES",
                      "B|2026-10-01|REGULAR|3|200|120|YES"])
    report = RetailReport(clean)
    return report.sales_total(clean) == 300


print("Validation passed:", test_validation())
print("Transformation passed:", test_transformation())
print("Total passed:", test_total())

"""Run a small example using six made-up shop transactions."""

from pipeline.validator import validate
from pipeline.transformer import transform
from pipeline.reporter import RetailReport

# Branch | date | tier | items | sales | cost | active
rows = [
    " a |2026-10-01| gold |2|100|60|yes",
    "B|2026-10-02|REGULAR|3|200|120|YES",
    "A|2026-10-03|REGULAR|1|50|30|NO",
    "|2026-10-04|GOLD|2|100|60|YES",
    "B|2026-02-30|REGULAR|1|80|50|YES",
    "A|2026-10-06|GOLD|1|-40|20|YES"
]

clean = validate(rows)
active = transform(clean)
report = RetailReport(active)
report.show(len(rows), len(clean))

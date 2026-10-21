# Retail Pipeline

This small project cleans made-up shop transactions and prints a sales report.
It helps someone see which records are usable and which branch sold the most.

## Open and run

Python 3 is required. No extra packages are needed.

1. Download or clone this repository. If you download a ZIP, extract it first.
2. In VS Code, select **File > Open Folder** and open the folder containing
   `main.py`.
3. Select **Terminal > New Terminal** and run:

```text
python main.py
```

To run the three tests:

```text
python tests.py
```

On Windows, you can use `py` instead of `python` if that is your installed
Python launcher. Each test result should say `True`; rejected test rows are
intentional.

The prepared local copy also has **Terminal > Run Task > Run project** and
**Run tests** shortcuts. Its `.vscode` settings are specific to that computer
and are excluded from Git. The commands above work without those settings.

## What the files do

- `main.py`: holds the sample data and runs the steps.
- `pipeline/schema.py`: defines the `TransactionRecord` class.
- `pipeline/validator.py`: cleans text and rejects bad records.
- `pipeline/transformer.py`: keeps active records and calculates margin and tax.
- `pipeline/reporter.py`: defines `RetailReport`, which uses the transaction objects.
- `tests.py`: runs three tests. Each result should say `True`.

## Example rules

Each row follows `branch|YYYY-MM-DD|tier|items|sales|cost|active`.
Use branch A or B, tier GOLD or REGULAR, and active status YES or NO.
Extra spaces and letter case are cleaned. Dates must exist on the calendar.
Items are positive whole numbers. Sales and costs are non-negative whole-dollar
numbers, for example `100`, not `100.50`. These three numbers allow up to eight
digits. Missing fields, negative values, and invalid rows are rejected.

Only active, valid records count towards sales. All valid records count towards
retention. Margin is `(sales - cost) / sales * 100`; zero sales gives 0%.
Tax is calculated separately from sales, using invented rates: A = 5%, B = 8%.
Branch A wins a sales tie. No active records means no top branch.
The original records are not changed by the calculations.

The sample has 6 rows, 3 valid records, 50% retention, and $300 in active sales.
Branch B leads. REGULAR sales are $200 and GOLD sales are $100. Both margins
are 40%; the taxes are $5 and $16. The rejected rows are intentional.

AI helped prepare this draft. Record the actual student/team contributions
when you prepare the submission.

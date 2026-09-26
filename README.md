# Beginner Python Assignment Workbooks

The exercises are grouped into topic folders to avoid creating one file per question. Each workbook uses short names, small functions, and plain examples. Existing folders and files were left unchanged.

## Folders and Run Commands

Run commands from the `python` workspace folder in PowerShell:

```powershell
python file_io_assignments/file_basics.py
python file_io_assignments/file_processing.py
python file_io_assignments/records_and_safety.py
python functions_assignments/functions_workbook.py
python oop_relationships_assignments/relationships_workbook.py
python operators_assignments/operators_workbook.py
python polymorphism_assignments/polymorphism_workbook.py
```

To start the interactive file manager:

```powershell
python file_io_assignments/records_and_safety.py --menu
```

The file-I/O examples create their sample text, CSV, and JSON files inside `file_io_assignments`, not in the workspace root. Run them again to recreate the examples.

## Assignment Coverage

- `file_io_assignments/file_basics.py`: File I/O Levels 1-3. Run it to create/read sample files and see `read`, `readline`, `readlines`, `write`, `writelines`, `tell`, and `seek` examples.
- `file_io_assignments/file_processing.py`: File I/O Levels 4-6. Includes text counts and filters, text changes, and number-file calculations and transformations.
- `file_io_assignments/records_and_safety.py`: File I/O Levels 7-10. Includes student records, CSV and JSON examples, exception-safe helpers, file copying, and the menu-driven file manager.
- `functions_assignments/functions_workbook.py`: Function Levels 1-5 and collection exercises. Related operations are reusable functions; sample calls are in `main()`. Mini-project building blocks include calculator, student records, banking, cart totals, contacts, number tools, and library search.
- `oop_relationships_assignments/relationships_workbook.py`: IS-A, HAS-A, USES-A, relationship-identification examples, and combined relationship examples.
- `operators_assignments/operators_workbook.py`: Operator Levels 1-10, including a small calculator and real-world checks.
- `polymorphism_assignments/polymorphism_workbook.py`: Shared methods, overriding, duck typing, operator overloading, abstract classes, and small payment/report examples.

Related prompts that ask for the same behavior use one shared function or class rather than duplicate files. To try a function example, look at its name in the workbook and add a small call in `main()`.

"""Check data.csv against the schema in datapackage.yml (Frictionless can't open a .yml package directly)."""
import sys

import yaml
from frictionless import Package

with open("datapackage.yml", encoding="utf-8") as f:
    descriptor = yaml.safe_load(f)

report = Package.from_descriptor(descriptor, basepath=".").validate()
if not report.valid:
    print(report.to_summary())
    sys.exit("data.csv does not match datapackage.yml")
print("data.csv matches datapackage.yml")

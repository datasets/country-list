"""Build data.csv from the ISO 3166-1 list that ships with pycountry (Debian iso-codes)."""
import csv
import sys
from importlib.metadata import version

import pycountry

output = "data.csv"


def build():
    rows = sorted((country.name, country.alpha_2) for country in pycountry.countries)
    if len(rows) < 200:
        sys.exit("Only {} countries found; pycountry looks wrong.".format(len(rows)))
    codes = [code for _, code in rows]
    if len(set(codes)) != len(codes):
        sys.exit("Duplicate country codes found.")
    return rows


def write(rows):
    with open(output, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["Name", "Code"])
        writer.writerows(rows)


if __name__ == "__main__":
    print("pycountry {}".format(version("pycountry")))
    rows = build()
    write(rows)
    print("{} countries written to {}".format(len(rows), output))

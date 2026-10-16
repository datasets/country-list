<a className="gh-badge" href="https://datahub.io/core/country-list"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# ISO 3166-1 Country List

English country names and their ISO 3166-1 alpha-2 code elements, in one CSV file. The list is rebuilt from the ISO 3166-1 data in the [pycountry][pycountry] package.

Column definitions and types are in `datapackage.yml`.

## Data

`data.csv` has one row per country or territory, sorted by `Name`:

| Column | Meaning |
|---|---|
| `Name` | English short name, as pycountry gives it, for example `Korea, Republic of`. Names with a comma are in quotes, so they stay one column |
| `Code` | ISO 3166-1 alpha-2 code: two upper-case letters, for example `KR`. Each code appears once |

### Known limitations

* "NA" is a code, not a missing value. The code for Namibia is the two letters `NA`. Many tools read the text `NA` as "missing" by default. For example, `pd.read_csv("data.csv")` returns an empty value (`NaN`) for Namibia. To keep it, read the file with `keep_default_na=False`:

  ```python
  import pandas as pd
  df = pd.read_csv("data.csv", keep_default_na=False)
  ```
* Many names contain a comma, for example `"Korea, Republic of"` and `"Virgin Islands, U.S."`. They are in quotes in the file, and any CSV reader keeps each name in one column.
* Names are formal short names, not always everyday usage. For example `Holy See (Vatican City State)`, `Taiwan, Province of China` and `Congo, The Democratic Republic of the`. Match countries by `Code`, not by `Name`.
* Names can change when the list is rebuilt, because the source updates its names. Codes change much less often, so use them as the key.

## Data sources

* [pycountry][pycountry], a Python package that gives the ISO 3166-1 country codes and English short names. It includes a copy of the data of the Debian [iso-codes][isocodes] project, used as it is (the iso-codes site refuses scripts, so that link could not be checked automatically). Licence: LGPL-2.1 for the package and its data; ISO's position on the names is unclear (see [License](#license)).

Changes made to the source data: the script takes each country's English name and alpha-2 code from pycountry and sorts the rows by name. Nothing else is changed. The names are the ones pycountry gives, not ISO's own style with brackets such as `Bahamas (the)`.

Not endorsed by, or affiliated with, ISO, the United Nations, pycountry or the iso-codes project.

[pycountry]: https://github.com/pycountry/pycountry
[isocodes]: https://salsa.debian.org/iso-codes-team/iso-codes

## Preparation

You need Python 3.12 or greater. To rebuild the data from the repository root:

```bash
pip install -r scripts/requirements.txt
python scripts/process.py
python scripts/validate.py
```

The script prints the pycountry version it used and writes `data.csv`. It stops with an error if pycountry returns fewer than 200 countries or a repeated code.

A GitHub workflow runs the script on the first day of every month (at 00:00 UTC) and when started by hand. It checks `data.csv` against `datapackage.yml` with [Frictionless](https://framework.frictionlessdata.io/) (`scripts/validate.py`) and commits `data.csv` if it changed.

## License

The names and codes come from pycountry, which is licensed under the LGPL-2.1 and includes iso-codes data. The LGPL is a software licence. We found nothing that puts LGPL terms on this CSV.

The licence of the ISO 3166-1 list itself is unclear. What we checked:

* ISO states on its site: "ISO allows free-of-charge use of its country, currency and language codes from ISO 3166, ISO 4217 and ISO 639, respectively" ([ISO 3166-1 page](https://committee.iso.org/iso-3166-1-new-access.html)).
* The same ISO site says: "Any use, including reproduction requires our written permission" ([ISO copyright page](https://committee.iso.org/copyright.html)).
* ISO also says it does not define the names of countries: "this information comes from United Nations sources". We did not find the terms for those names.
* We found no ISO page that says whether the full list, with the names, may be republished under an open licence. ISO's own site and the Online Browsing Platform refuse scripted requests, so the pages above were read on ISO's committee site.

We could not establish whether the full list with the names may be reused. Using the codes is free of charge according to ISO. We think the risk is low, but the position is unclear. If you plan to republish or sell the list, ask ISO for written confirmation first.

The maintainers place only their own work (the script, the selection and arrangement of the list and the file) under the [Public Domain Dedication and License (PDDL)](https://opendatacommons.org/licenses/pddl/1.0/). This does not cover the ISO codes or the names themselves. See also [ATTRIBUTION.txt](ATTRIBUTION.txt).

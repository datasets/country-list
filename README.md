<a className="gh-badge" href="https://datahub.io/core/country-list"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# ISO 3166-1 Country List

English country names and their ISO 3166-1 alpha-2 code elements, in one CSV file. The names are the short names in English, in alphabetical order, as listed in [ISO 3166-1][ISO 3166-1].

Column definitions and types are in `datapackage.yml`.

## Data

`data.csv` has 249 rows, one per country or territory, sorted by `Name`:

| Column | Meaning |
|---|---|
| `Name` | English short name, written as ISO gives it, for example `Korea (the Republic of)`. Names with a comma are in quotes, for example `"Palestine, State of"` |
| `Code` | ISO 3166-1 alpha-2 code: two upper-case letters, for example `KR`. Each code appears once |

### Known limitations

* "NA" is a code, not a missing value. The code for Namibia is the two letters `NA`. Many tools read the text `NA` as "missing" by default. For example, `pd.read_csv("data.csv")` returns an empty value (`NaN`) for Namibia. To keep it, read the file with `keep_default_na=False`:

  ```python
  import pandas as pd
  df = pd.read_csv("data.csv", keep_default_na=False)
  ```
* Names follow ISO's style, not everyday usage. A qualifier can be in brackets, for example `Korea (the Republic of)`, `Cayman Islands (the)` and `Virgin Islands (U.S.)`. One name has a second form in square brackets: `Falkland Islands (the) [Malvinas]`. Match countries by `Code`, not by `Name`.
* `Western Sahara` is written `Western Sahara*` in the source. The asterisk is part of the name in the file. It marks a provisional name.

## Data sources

* [ISO 3166-1][ISO 3166-1] country codes, from the ISO 3166 Maintenance Agency (ISO Online Browsing Platform). It provides the alpha-2 codes and the English short names. ISO says the names come from United Nations sources. Licence: unclear (see [License](#license)).

Changes made to the source data: none intended. The file is edited by hand (there is no script), and the codes and names are kept as ISO writes them.

Not endorsed by, or affiliated with, ISO or the United Nations.

[ISO 3166-1]: https://www.iso.org/obp/ui/#search/code/

## Preparation

There is no script and no automatic job. The file is edited by hand, from the [ISO Online Browsing Platform][ISO 3166-1], when ISO changes the list. After an edit, the codes can be compared with the `ISO3166-1-Alpha-2` column of the [country-codes](https://github.com/datasets/country-codes) dataset: the two lists have the same codes.

## License

The licence of the ISO 3166-1 list is unclear. What we checked:

* ISO states on its site: "ISO allows free-of-charge use of its country, currency and language codes from ISO 3166, ISO 4217 and ISO 639, respectively" ([ISO 3166-1 page](https://committee.iso.org/iso-3166-1-new-access.html)).
* The same ISO site says: "Any use, including reproduction requires our written permission" ([ISO copyright page](https://committee.iso.org/copyright.html)).
* ISO also says it does not define the names of countries: "this information comes from United Nations sources". We did not find the terms for those names.
* We found no ISO page that says whether the full list, with the names, may be republished under an open licence. ISO's own site and the Online Browsing Platform refuse scripted requests, so the pages above were read on ISO's committee site.

We could not establish whether the full list with the names may be reused. Using the codes is free of charge according to ISO. If you plan to republish or sell the list, ask ISO for written confirmation first.

The list is a short, simple set of facts. There is an argument that no rights exist in such a collection. We have not confirmed this.

The maintainers place only their own work (the selection and arrangement of the list and the file) under the [Public Domain Dedication and License (PDDL)](https://opendatacommons.org/licenses/pddl/1.0/). This does not cover the ISO codes or the names themselves. See also [ATTRIBUTION.txt](ATTRIBUTION.txt).

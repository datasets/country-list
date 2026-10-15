<a className="gh-badge" href="https://datahub.io/core/country-list"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

ISO 3166-1-alpha-2 English country names and code elements. This list states
the country names (official short names in English) in alphabetical order as
given in [ISO 3166-1][] and the corresponding ISO 3166-1-alpha-2 code elements.

[ISO 3166-1]: https://www.iso.org/obp/ui/#search/code/

This list is edited by hand when the official code list in ISO 3166-1 changes
(see "How it is updated" below). Nothing updates it automatically.

It lists 249 official short names and code elements as of May 2026.

**Data note:** `Western Sahara` appears as `Western Sahara*` in the ISO source. The asterisk denotes a provisional name.

## Data

The file `data.csv` has 249 rows and 2 columns:

- `Name`: the English short name, written as ISO gives it. This includes ISO's
  style of putting a qualifier in brackets, for example `Korea (the Republic of)`,
  `Cayman Islands (the)`, `Bahamas (The)` and `Virgin Islands (U.S.)`. It also
  includes the asterisk in `Western Sahara*`.
- `Code`: the ISO 3166-1 alpha-2 code, two upper-case letters. Each code appears
  once.

The rows are sorted by `Name`.

### Note: "NA" is a code, not a missing value

The code for Namibia is the two letters `NA`. Many tools read the text `NA` as
"missing" by default. For example, `pandas.read_csv("data.csv")` returns an empty
value (`NaN`) for Namibia. To keep it, read the file with `keep_default_na=False`:

```python
import pandas as pd
df = pd.read_csv("data.csv", keep_default_na=False)
```

## How it is updated

There is no script and no automatic job. The file is edited by hand, from the
[ISO Online Browsing Platform][ISO 3166-1], when ISO changes the list. After an
edit, the 249 codes can be compared with the `ISO3166-1-Alpha-2` column of the
[country-codes](https://github.com/datasets/country-codes) dataset: the two lists
have the same codes.

## License

This material is licensed by its maintainers under the Public Domain Dedication
and License.

Nevertheless, it should be noted that this material is ultimately sourced from
ISO and their rights and licensing policy is somewhat unclear. As this is a
short, simple database of facts there is a strong argument that no rights can
subsist in this collection. However, ISO state on [their
site](https://www.iso.org/obp/ui/#search/code/): 

> ISO makes the list of alpha-2 country codes available for internal use and
> non-commercial purposes free of charge. 

This carries the implication (though not spelled out) that other uses are not
permitted and that, therefore, there may be rights preventing further general
use and reuse.


# Free Sample — Japan Prefecture Behavior & Consumption Master

A cleaned, analysis-ready table of **how people in Japan's 47 prefectures eat,
spend, commute, sleep and learn** — built by Japan Open Data Lab from official
Japanese statistics, with every column defined and sourced.

- `japan_prefecture_behavior_consumption_sample.csv` — 47 rows × 18 columns, no missing values
- `data-dictionary.md` — units, years, coverage and the exact definition of every column
- `data-quality-report-v1.md` — our verification report (in Japanese): what we checked, what matched, and what we have not verified

## Why this sample exists

Public statistics are free, but they are rarely usable as-is: item codes,
capital-city coverage, and differing survey years have to be reconciled before
the numbers mean anything. This sample is a small, fully documented slice of
that cleaning work — the same quality bar we apply to the full datasets.

## How this data was verified

Before release, every column was checked against its dictionary definition,
missing values were confirmed to be genuinely zero (not confused with real
zeros), distributions were sanity-checked against known regional patterns,
and six indicators were spot-checked against the publishers' official values
— all matched. The full report, **including the limits of that verification
and why one column was deliberately left out on licensing grounds**, is in
[`data-quality-report-v1.md`](data-quality-report-v1.md) (Japanese).

## Sources and attribution

All values are published official statistics. When you use this data, please
keep the source attributions:

- Family Income and Expenditure Survey and Survey on Time Use and Leisure
  Activities (Statistics Bureau, Ministry of Internal Affairs and
  Communications, Japan) — columns marked "via SSDSE" in the dictionary were
  processed by Japan Open Data Lab from SSDSE-C-2026 / SSDSE-D-2023
  (Statistics Center, NSTAC).
- Housing and Land Survey 2023 (Statistics Bureau, MIC).

## Terms of use

Free to use, **including commercially**, under the terms of the original
statistics (Government of Japan Standard Terms of Use / Public Data License
1.0-compatible), with the source attributions above. Only columns whose
sources permit commercial use are included in this sample.

## Feedback

If you use this sample in a product, a pitch or an analysis, we would love to
hear what you used it for — open an issue in this repository. Usage stories
decide what we clean and release next.

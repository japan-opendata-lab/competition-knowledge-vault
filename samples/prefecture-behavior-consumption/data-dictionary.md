# Data Dictionary — Japan Prefecture Behavior & Consumption Master (Free Sample)

47 prefectures × 18 columns. One row per prefecture. Values are published
official statistics only — no imputation, no allocation down to municipalities.
Household-survey columns are measured in the prefectural capital city
(two-or-more-person households), exactly as the source publishes them; this is
stated per column in the "Coverage" field and is never hidden.

## Identifier columns

| Column | Type | Description |
|---|---|---|
| `prefecture_code` | string | Two-digit prefecture code (JIS X 0401), `01`–`47` |
| `prefecture` | string | Prefecture name (Japanese) |
| `capital_city` | string | Capital city name — the survey city for household-survey columns (e.g. 東京都区部 for Tokyo) |

## Indicator columns

| Column | Unit | Years | Coverage | Source | Definition |
|---|---|---|---|---|---|
| `eating_out_ratio_pct` | % | 2023–2025 avg | Capital city, 2+ person households | MIC Family Income and Expenditure Survey (FIES), via SSDSE-C-2026 | Eating-out expenditure (LB12) ÷ total food expenditure (LB00) × 100 |
| `prepared_food_ratio_pct` | % | 2023–2025 avg | Capital city, 2+ person households | MIC FIES, via SSDSE-C-2026 | Prepared-food expenditure (LB09) ÷ food expenditure (LB00) × 100 |
| `noodles_expenditure_jpy` | JPY/year | 2023–2025 avg | Capital city, 2+ person households | MIC FIES, via SSDSE-C-2026 | Total noodle expenditure: fresh udon/soba (LB013001) + dried udon/soba (LB013002) + pasta (LB013003) + Chinese noodles (LB013004) + cup noodles (LB013005) + instant noodles (LB013006) + other noodles (LB013007) |
| `liquor_ratio_pct` | % | 2023–2025 avg | Capital city, 2+ person households | MIC FIES, via SSDSE-C-2026 | Alcoholic beverage expenditure (LB11) ÷ food expenditure (LB00) × 100 |
| `savings_annual_income_ratio` | ratio | 2024 | Capital city, 2+ person households | MIC FIES (Savings & Liabilities volume), Table 8-1 | Average savings balance per household ÷ annual income |
| `social_expenses_ratio_pct` | % | 2025 | Capital city, 2+ person households | MIC FIES (purpose classification), Table 1-1 | Monthly social/entertaining expenses ÷ monthly consumption expenditure × 100 |
| `commute_school_time_min` | min/day | 2021 | Whole prefecture, age 10+, weekly average | MIC Survey on Time Use and Leisure Activities, via SSDSE-D-2023 | Average daily commuting / school travel time (MG04) |
| `sleep_time_min` | min/day | 2021 | Whole prefecture, age 10+, weekly average | MIC Survey on Time Use and Leisure Activities, via SSDSE-D-2023 | Average daily sleep time (MG01) |
| `sports_participant_rate_pct` | % | 2021 | Whole prefecture, age 10+ | MIC Survey on Time Use and Leisure Activities, via SSDSE-D-2023 | Share of people who did any sport in the past year (MC00) |
| `hobby_entertainment_time_min` | min/day | 2021 | Whole prefecture, age 10+, weekly average | MIC Survey on Time Use and Leisure Activities, via SSDSE-D-2023 | Average daily time for hobbies and entertainment (MG15) |
| `home_ownership_rate_pct` | % | 2023 | Whole prefecture, principal households | MIC Housing and Land Survey 2023, final results appendix | Owner-occupied homes as a share of homes with a principal household |
| `seafood_meat_ratio` | ratio | 2023–2025 avg | Capital city, 2+ person households | MIC FIES, via SSDSE-C-2026 | Seafood expenditure (LB02) ÷ meat expenditure (LB03). Above 1.0 = seafood-dominant |
| `coffee_related_expenditure_jpy` | JPY/year | 2023–2025 avg | Capital city, 2+ person households | MIC FIES, via SSDSE-C-2026 | Ground/bean coffee (LB102001) + coffee drinks (LB102002) + café charges (LB121201) |
| `volunteer_participant_rate_pct` | % | 2021 | Whole prefecture, age 10+ | MIC Survey on Time Use and Leisure Activities, via SSDSE-D-2023 | Share of people who did volunteer activity in the past year (ME00) |
| `learning_self_dev_rate_pct` | % | 2021 | Whole prefecture, age 10+ | MIC Survey on Time Use and Leisure Activities, via SSDSE-D-2023 | Share of people who did self-development learning or training in the past year (MB00) |

## Notes

- No missing values: all 47 prefectures are populated for every column.
- Cleaning applied by Japan Open Data Lab: column-name normalisation, type
  alignment, capital-city labelling per prefecture, and cross-checks of the
  indicator values against the published source tables.
- One column of the internal master (passenger cars per household, sourced
  from AIRIA published statistics) is **not** included in this sample: AIRIA
  is not a government body, and its published copyright policy requires prior
  consent for reproduction, so the column cannot be treated as cleared for
  commercial redistribution. Only columns whose sources permit commercial
  use are included. See `data-quality-report-v1.md` §4.

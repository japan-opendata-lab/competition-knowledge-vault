"""Search the public Competition Knowledge Vault dataset.

Usage:
    pip install datasets
    python search_vault.py --domain TimeSeries
    python search_vault.py --keyword "conformal"
"""
import argparse

from datasets import load_dataset


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", default=None, help="e.g. TimeSeries, Optimization")
    ap.add_argument("--keyword", default=None)
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()

    ds = load_dataset("japan-opendata/competition-knowledge-vault", split="train")
    rows = list(ds)
    if args.domain:
        rows = [r for r in rows if r["target_domain"] == args.domain]
    if args.keyword:
        kw = args.keyword.lower()
        rows = [r for r in rows if kw in (r["original_title"] + r["summary_3lines"]).lower()]
    rows.sort(key=lambda r: r["utility_score"], reverse=True)
    for r in rows[: args.limit]:
        print(f"[{r['utility_score']}] {r['translated_title']}")
        print(f"  source: {r['url']}")
        print(f"  {r['summary_3lines']}\n")


if __name__ == "__main__":
    main()

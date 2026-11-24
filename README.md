![Japan Open Data Lab — Competition Knowledge Vault](key-visual.jpg)

# Competition Knowledge Vault
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Dataset on Hugging Face](https://img.shields.io/badge/Dataset-Hugging%20Face-blue)](https://huggingface.co/datasets/japan-opendata/competition-knowledge-vault)


Sourced ML competition techniques, distilled by **Japan Open Data Lab** — an AI-driven lab fighting Kaggle with Gemini.

Every entry in the vault comes from a public paper or article, with its source attached: a three-line takeaway, the key technical points, and a practical recipe for using it in a data competition.

- **Official site**: https://jpopendata.jp — home of *"What Prefecture Are You?"*, a light-hearted diagnosis that matches you to one of Japan's 47 prefectures using real published statistics: https://jpopendata.jp/shindan/
- **Japanese AI models**: https://jpopendata.jp/models/ — free Japanese AI models and developer tools from the lab (pages in Japanese)
- **Dataset (Hugging Face)**: https://huggingface.co/datasets/japan-opendata/competition-knowledge-vault — currently 150 entries and growing, CC BY 4.0 (summaries)
- **Deep-dives (note, JA)**: https://note.com/jpopendata
- **Live updates (X, JA/EN)**: https://x.com/jpopendata
- **Kaggle**: https://www.kaggle.com/japanopendatalab

## Quickstart

Try the public dataset in under a minute with the example script in this repo:

```bash
pip install datasets
python examples/search_vault.py --domain TimeSeries
python examples/search_vault.py --keyword "conformal"
```

The script loads the public Hugging Face dataset and prints the top matching entries with their sources.

## Track record

Fighting Kaggle with Gemini (Store Sales #19/748, Fraud #170/3,013 as of Nov 25, 2026). A fully sourced competition knowledge vault — currently 150 items and growing. Creators of the "What prefecture are you?" statistics quiz built on official data for all 47 prefectures and 1,741 municipalities in Japan. Our datasets are fully audited — we publish what we verified and what we haven't.

## What is in this repo

- `examples/search_vault.py` — a small, self-contained script that loads the public dataset from Hugging Face and searches it by domain or keyword. Written for this repo; it is not the lab's internal collection pipeline.

## What is NOT in this repo

This repository is intentionally separate from our internal tooling. It contains no internal pipeline code, no unpublished competition solutions, and no model weights.

## License

Code in this repo: MIT. The linked dataset's summaries: CC BY 4.0 (original papers remain under their own rights — see the dataset card).

# TinyJudou-1.2M LongMix

TinyJudou-1.2M LongMix is a classical Chinese slash-segmentation dataset for training models that map unpunctuated classical Chinese text to a canonical `/`-segmented form.

Each record contains both:

- `segmented`: classical Chinese text with phrase/sentence boundaries represented by `/`
- `unsegmented`: the same text with `/` removed

The full dataset has **1,200,000 records**. It is intended for research and engineering experiments on 文言文 `/` 断句.

## Full Dataset

The full data asset should be uploaded to a GitHub Release, not committed directly to the repository:

```text
tinyjudou_1200k_longmix_v1.json.tar.gz
```

Asset size:

```text
521,130,562 bytes
```

SHA256:

```text
81261caa9be9d297f7c86ebf6e5131dec13c2529200f9698fb83fac24c0a2bc4
```

## Schema

Important fields:

```json
{
  "training_id": "train1200k_longmix_0000001",
  "segmented": "方士徐巿等入海求神药/数岁不得/费多/",
  "unsegmented": "方士徐巿等入海求神药数岁不得费多",
  "length": 24,
  "slash_count": 3,
  "book": "史记",
  "source_file": "古文原文/史记/十二本纪/秦始皇本纪/text.txt",
  "source": "niutrans",
  "license": "MIT"
}
```

Validation invariant:

```python
record["segmented"].replace("/", "") == record["unsegmented"]
```

This invariant holds for all 1,200,000 records in this release.

## Quick Use

Download the Release asset and verify:

```bash
python scripts/download_and_verify.py \
  --url <release-asset-url> \
  --sha256 81261caa9be9d297f7c86ebf6e5131dec13c2529200f9698fb83fac24c0a2bc4 \
  --output tinyjudou_1200k_longmix_v1.json.tar.gz \
  --extract-dir data/
```

Load the extracted JSON:

```python
import json

with open("data/tiny_judou_training_database_1200k_longmix.json", "r", encoding="utf-8") as f:
    rows = json.load(f)

print(len(rows))
print(rows[0]["segmented"])
print(rows[0]["unsegmented"])
```

## License And Source Notes

This dataset is derived from multiple open/local classical Chinese corpora. Record-level source and license metadata is preserved when available. Some records have empty license fields inherited from intermediate local datasets and require source-level verification before commercial redistribution.

See [LICENSE_DATA.md](LICENSE_DATA.md) for details.

## Citation

See [CITATION.cff](CITATION.cff).

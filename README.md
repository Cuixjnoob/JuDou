
# TinyJudou-1.2M LongMix

TinyJudou-1.2M LongMix is a classical Chinese slash-segmentation dataset for training models that convert unpunctuated classical Chinese text into a canonical `/`-segmented form.

The dataset is designed for research and engineering experiments on **文言文 `/` 断句** (中国人在这里就用中文）, especially character-level or span-level segmentation models.

Each record contains two aligned text fields:

- `segmented`: classical Chinese text with phrase or sentence boundaries marked by `/`
- `unsegmented`: the same text with all `/` markers removed

The full release contains **1,200,000 records**.

---

## Dataset Asset

The full dataset should be distributed as a GitHub Release asset rather than committed directly to the repository.

Release asset:

```text
tinyjudou_1200k_longmix_v1.json.tar.gz
````

Asset size:

```text
521,130,562 bytes
```

SHA256:

```text
81261caa9be9d297f7c86ebf6e5131dec13c2529200f9698fb83fac24c0a2bc4
```

---

## Data Schema

Each record is a JSON object. Important fields include:

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

Field meanings:

* `training_id`: unique record identifier
* `segmented`: canonical slash-segmented text
* `unsegmented`: input text with all slash markers removed
* `length`: character length of `unsegmented`
* `slash_count`: number of `/` markers in `segmented`
* `book`: source book or text collection when available
* `source_file`: original source path when available
* `source`: upstream corpus or data source
* `license`: record-level license metadata when available

---

## Validation Invariant

For every record in this release, the following invariant holds:

```python
record["segmented"].replace("/", "") == record["unsegmented"]
```

This invariant has been checked for all **1,200,000** records.

---

## Quick Start

Download the GitHub Release asset and verify its checksum:

```bash
python scripts/download_and_verify.py \
  --url <release-asset-url> \
  --sha256 81261caa9be9d297f7c86ebf6e5131dec13c2529200f9698fb83fac24c0a2bc4 \
  --output tinyjudou_1200k_longmix_v1.json.tar.gz \
  --extract-dir data/
```

Load the extracted JSON file:

```python
import json

with open("data/tiny_judou_training_database_1200k_longmix.json", "r", encoding="utf-8") as f:
    rows = json.load(f)

print(len(rows))
print(rows[0]["segmented"])
print(rows[0]["unsegmented"])
```

---

## Intended Use

TinyJudou-1.2M LongMix is intended for:

* classical Chinese slash segmentation
* 文言文 `/` 断句 model training
* character-level and span-level segmentation experiments
* structured prediction models such as boundary classifiers, CRF models, Semi-CRF models, and sequence encoders
* evaluation of segmentation robustness across books, genres, and source collections

The dataset is not intended to define a universal punctuation standard. The `/` markers represent the canonical segmentation style used in this dataset release.

---

## License and Source Notes

This dataset is derived from multiple open or local classical Chinese corpora. Record-level source and license metadata is preserved when available.

Some records may have empty license fields inherited from intermediate local datasets. These records require source-level verification before commercial redistribution.

See [LICENSE_DATA.md](LICENSE_DATA.md) for detailed source and license notes.

---

## Citation

If you use this dataset, please cite it using the metadata in [CITATION.cff](CITATION.cff).


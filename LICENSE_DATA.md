# Data License And Terms

TinyJudou-1.2M LongMix is a compiled dataset derived from multiple open/local classical Chinese corpora and intermediate TinyJudou processing outputs.

This file is not legal advice. It summarizes the release posture and the license metadata currently present in the dataset.

## Record-Level License Metadata

The dataset contains a `license` field when a source license was available at the record level.

Current distribution:

```json
{
  "MIT": 544468,
  "CC0-1.0": 533300,
  "": 122208,
  "CC BY-SA or public domain, check page": 24
}
```

## Recommended Release Terms

Because this is a mixed-source dataset, do not claim that the entire dataset is newly relicensed under a single permissive license unless each source has been fully audited.

Recommended wording:

```text
The dataset is released with source and license metadata preserved where available.
Each record may be subject to the terms of its original source.
Users are responsible for checking source/license fields before redistribution or commercial use.
Code and metadata files in this repository may be used under MIT unless otherwise noted.
```

## Source Notes

Known/expected source families include:

- NiuTrans/Classical-Modern derived classical text, commonly MIT in the source repository.
- gujilab/chinese-classical-corpus `punctuate`, recorded here as `CC0-1.0`.
- Scagin/CCTC derived records, recorded here as `MIT` where normalized.
- Small Wikisource-derived supplements, recorded as `CC BY-SA or public domain, check page`.
- Intermediate TinyJudou generated pools with incomplete top-level license fields. These retain `source_refs`, `primary_source_name`, `primary_path`, `book`, and `source_file` for audit.

## Practical Guidance

For research use:

- The full dataset is suitable as a broad training pool.
- Cite this dataset and inspect the original sources where needed.

For commercial use:

- Filter or audit by `license`.
- Prefer records with explicit permissive license metadata.
- Re-check source pages for Wikisource and empty-license records.

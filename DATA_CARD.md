# TinyJudou-1.2M LongMix Data Card

## Dataset Summary

TinyJudou-1.2M LongMix is a 1,200,000-record classical Chinese `/` segmentation dataset. The task is:

```text
input:  unsegmented classical Chinese character stream
target: the same text with / inserted at segmentation boundaries
```

Example:

```json
{
  "segmented": "非蛇鳝之穴/无可寄托者/",
  "unsegmented": "非蛇鳝之穴无可寄托者"
}
```

## Intended Uses

- Training classical Chinese slash-segmentation models.
- Pretraining or continued pretraining for classical Chinese encoders.
- Data analysis of 文言句读 structure.
- Benchmark construction after users create their own clean holdout splits.

## Not Intended Uses

- Treating this full mixed dataset as a clean evaluation benchmark.
- Recovering modern punctuation such as `，。！？`.
- Legal or authoritative scholarly editions of classical texts.
- Commercial redistribution without checking source-level license metadata.

## Size

```json
{
  "records": 1200000,
  "compressed_asset": "tinyjudou_1200k_longmix_v1.json.tar.gz",
  "compressed_size_bytes": 521130562,
  "uncompressed_json_size_bytes": 2704402637
}
```

## Text Fields

- `segmented`: text with `/` as the only segmentation marker.
- `unsegmented`: `segmented` with `/` removed.

All records satisfy:

```python
segmented.replace("/", "") == unsegmented
```

## Metadata Fields

Common metadata fields include:

- `training_id`
- `length`
- `slash_count`
- `avg_segment_len`
- `book`
- `group`
- `source`
- `license`
- `source_file`
- `primary_source_name`
- `primary_tier`
- `primary_path`
- `source_refs`
- `usable_for_training`
- `usable_for_semantic_pretraining`
- `usable_for_slash_training_strict`

## Source Distribution

Top-level `source` distribution:

```json
{
  "niutrans": 533835,
  "gujilab_punctuate": 533300,
  "": 122208,
  "cctc": 10633,
  "wikisource": 24
}
```

Record-level license distribution:

```json
{
  "MIT": 544468,
  "CC0-1.0": 533300,
  "": 122208,
  "CC BY-SA or public domain, check page": 24
}
```

The empty-license rows come from intermediate local training pools where the original source/license was not always normalized into the top-level field. Use `source_refs`, `primary_path`, `book`, and `source_file` to audit them before sensitive redistribution.

## Quality Notes

The dataset is "LongMix": it combines base classical prose samples, long 100-200 character windows, 500-1000 character long article windows, and curated/hard examples. It is useful as a broad training pool, not as a pristine canonical edition.

Relevant validation counts:

```json
{
  "rows": 1200000,
  "has_slash_in_segmented": 1200000,
  "segmented_unsegmented_match": 1200000,
  "usable_for_semantic_pretraining": 1200000,
  "usable_for_slash_training_strict": 450000
}
```

The `usable_for_slash_training_strict` flag is retained for users who want a stricter subset, but the full release intentionally includes all 1.2M records.

## Known Limitations

- The dataset is compiled from multiple sources and processing rounds, so segmentation conventions may vary.
- Some source/license fields are incomplete.
- It includes training-development material and should not be used as a hidden test set.
- It uses `/` labels only; original punctuation type is not preserved as the target.

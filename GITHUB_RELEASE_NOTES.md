# GitHub Release Draft: TinyJudou-1.2M LongMix v1.0.0

## Title

TinyJudou-1.2M LongMix v1.0.0

## Description

This release provides the full TinyJudou-1.2M LongMix dataset for classical Chinese `/` segmentation.

Each record contains:

- `segmented`: classical Chinese text with `/` segmentation boundaries
- `unsegmented`: the same text without `/`
- source/book/license metadata where available

Validation summary:

```json
{
  "records": 1200000,
  "has_slash_in_segmented": 1200000,
  "segmented_unsegmented_match": 1200000
}
```

## Assets

Upload this file as the release asset:

```text
tinyjudou_1200k_longmix_v1.json.tar.gz
```

Size:

```text
521,130,562 bytes
```

SHA256:

```text
81261caa9be9d297f7c86ebf6e5131dec13c2529200f9698fb83fac24c0a2bc4
```

## Notes

This is a mixed-source training dataset, not a clean hidden evaluation benchmark. Source and license metadata is preserved where available. Some records have incomplete top-level license metadata and should be audited before sensitive redistribution or commercial use.

Recommended use:

```text
training / pretraining / data research
```

Not recommended as:

```text
authoritative scholarly text edition / punctuation restoration benchmark / legal source package
```

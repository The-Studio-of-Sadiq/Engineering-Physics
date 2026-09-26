# Reference.md — moved

The chapter-by-chapter source tracing for this book now lives at the repository
root:

**→ [`../REFERENCES.md`](../REFERENCES.md)**

## Why it moved

`REFERENCES.md` is referenced by the README, by `00 Map.md`, and by any reader
looking for provenance. A reference list buried under `METADATA/` reads as
internal apparatus; at the root it reads as what it is — a first-class part of
the argument. This file existed only to hold the content, and leaving it in
place would have produced two reference files that could drift apart.

## What is there now

`REFERENCES.md` contains everything this file did, plus:

- a **numbered citation key** (`[R1]`–`[R50]`) indexing every source with the
  chapters it serves, so a reader can go from a claim to its full bibliographic
  entry in one step. Chapter prose keeps citing by author and year — the `[R#]`
  labels are an index into the file, not a marker the text must carry
- a **numbered textbook key** (`[T#]`) covering all four engineering branches,
  which the previous version lacked for fluids, structures, chemical
  engineering, and control
- a **three-tier evidence classification** ([MEASURED] / [DERIVED / TEXTBOOK] /
  [SYNTHESIS]) applied consistently, with [SYNTHESIS] used explicitly for the
  book's own three load-bearing claims rather than attaching decorative
  citations to them
- an expanded **Gaps and flags** section recording what is not yet sourced

No citation was dropped in the move.

---

*Do not add new references here. Add them to [`../REFERENCES.md`](../REFERENCES.md).*

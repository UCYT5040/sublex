# Sublex

## Quickstart

```bash
pip install uv
uv run --module sublex
```

uv will automatically create a virtual environment and install all dependencies  (and do it blazing fast!)

A poetry SBX is included in the repository. Use the `query` or `author` filters with the `poetry` tag to search for poems.

## Writing SBXs (search confuigurations)

Sublex uses Starlark for SBX parsing.

See `sbx/poetry.sbx` for an example and `SBX.md` for an in-depth guide.

## Coming Soon:

- Discover and download SBX files through the InterPlanetary File System (IPFS).
- More SBX examples.
- Improved interface & documentation.
- Async search operations (and multiple operations)

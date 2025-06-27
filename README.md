# Sublex

Sublex is a tool to help perform searches (typically network searches) with multiple search configurations.

## Quickstart

```bash
pip install uv
uv run --module sublex
```

uv will automatically create a virtual environment and install all dependencies  (and do it blazing fast!)

### Filters / Tags

Each search operation has filters, and optionally has tags.

Tags specify what to search for. If a search configuration doesn't match the tags you listed, it wont be executed.

Filters are information sent to search configurations. The most common filter you'll see is `query`, but I recommend configurations also include filters like `author`, `genre`, `year`, etc.

### SBXs

`sbx` files are search configurations. Essentially, telling Sublex where to search and how to process those results.

A poetry (form of literature) SBX is included in the repository. With this, you can search for poems.

Use the `query` or `author` filters with the `poetry` tag to search for poems.

## Writing SBXs (search confuigurations)

Sublex uses Starlark for SBX parsing.

See `sbx/poetry.sbx` for an example and `SBX.md` for an in-depth guide.

## Coming Soon:

- Discover and download SBX files through the InterPlanetary File System (IPFS).
- More SBX examples.
- Improved interface & documentation.
- Async search operations (and multiple operations)

from .config.sbx import initialize

initialize()

from .sbx.loader import load

load()

from .search import execute_search
from .display_results import display_results

tags = input("Comma-separeted tags (or empty): ").split(",")
if tags == [""]:
    tags = None
filters = {}
print("HINT: Most SBXs accept the 'query' filter key")
while True:
    key = input("Filter key (or empty to finish): ")
    if not key:
        break
    value = input(f"Filter value for '{key}': ")
    filters[key] = value

display_results(execute_search(filters, tags))

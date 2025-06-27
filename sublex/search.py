from .sbx import registry
from .sbx.execute import execute_sbx


def execute_search(filters: dict[str, str], tags: list[str] | None = None) -> list[str]:
    results = []
    for sbx in registry.get_all():
        if tags and not set(tags).intersection(set(sbx.get("tags", []))):
            print(f"Skipping {sbx.get('name')} due to tags: {sbx.get('tags')}")
            continue
        one_filter_exists = False
        dealiased_filters = {}
        for key, value in sbx.get("supported_filters", {}).items():
            if key in filters:
                one_filter_exists = True
                dealiased_filters[key] = filters[key]
            else:
                for alias in value:
                    if alias in filters:
                        one_filter_exists = True
                        dealiased_filters[key] = filters[alias]
                        break
        if not one_filter_exists:
            print(f"Skipping {sbx.get('name')} due to filters: {sbx.get('filters')}")
            continue

        filters_table = sbx["lua"].table_from(filters)

        for result in execute_sbx(sbx, filters_table):
            result["sbx"] = sbx.get("name", "Unknown")
            results.append(result)

    results.reverse()
    return results

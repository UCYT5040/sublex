def display_results(results):
    for result in results:
        print("-" * 10)
        print(f": {result.get('title', 'N/A')}")
        print(f"  URL: {result.get('url', 'N/A')}")
        for other in result.get("other", {}).values():
            print(f"  *: {other.get('name', 'N/A')}: {other.get('value', 'N/A')}")
        action = input("Press Enter to continue or 'q' to quit: ")
        if action.lower() == "q":
            break
    print("-" * 10)
    print("End of results")

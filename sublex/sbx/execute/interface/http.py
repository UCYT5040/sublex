# HTTP functions for use within Lua
import requests


class HTTP:
    def __init__(self, sbx):
        self.sbx = sbx

    def get(self, url: str) -> dict:
        """
        Perform a GET request to the specified URL and return the response data.

        Args:
            url (str): The URL to fetch.

        Returns:
            dict: A dictionary containing the status code, headers, and body of the response.
        """
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        json_table = self.sbx['lua'].table_from(response.json()) if response.headers.get('Content-Type') == 'application/json' else None

        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.text,
            "json": json_table
        }

    # TODO: Implement POST, PUT, DELETE methods

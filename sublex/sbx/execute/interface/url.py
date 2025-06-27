# Util file for URL encoding

from urllib.parse import quote, unquote

class URL:
    @staticmethod
    def encode(url: str) -> str:
        """
        Encode a URL by replacing special characters with percent-encoded characters.

        Args:
            url (str): The URL to encode.

        Returns:
            str: The encoded URL.
        """
        return quote(url, safe='')

    @staticmethod
    def decode(encoded_url: str) -> str:
        """
        Decode a percent-encoded URL back to its original form.

        Args:
            encoded_url (str): The encoded URL to decode.

        Returns:
            str: The decoded URL.
        """
        return unquote(encoded_url)
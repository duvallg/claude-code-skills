# date_parser.py
# This module contains date parsing utilities for the application.
# Created: 2026-01-01
# Author: engineering team
# Last modified: 2026-05-16
# Version: 1.0.0

from datetime import datetime, timezone


def parse_iso8601_date(date_string: str) -> datetime:
    """
    Parse a date string in ISO 8601 format.

    This function accepts a string representing a date or datetime in ISO 8601
    format and returns a Python datetime object. ISO 8601 is an international
    standard covering the exchange of date- and time-related data. It was
    issued by the International Organization for Standardization (ISO).

    Parameters
    ----------
    date_string : str
        A string representing a date or datetime in ISO 8601 format.
        Examples: "2026-01-01", "2026-01-01T12:00:00", "2026-01-01T12:00:00Z"

    Returns
    -------
    datetime
        A Python datetime object representing the parsed date/time.

    Raises
    ------
    ValueError
        If the date_string cannot be parsed as a valid ISO 8601 date.

    Examples
    --------
    >>> parse_iso8601_date("2026-01-01")
    datetime.datetime(2026, 1, 1, 0, 0)

    Notes
    -----
    This function uses Python's datetime module for parsing.
    See also: https://en.wikipedia.org/wiki/ISO_8601
    """
    # Use datetime.fromisoformat to parse the string
    # This is the standard Python approach for ISO 8601 parsing
    try:
        # Try to parse the date string
        result = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        # Convert to UTC
        if result.tzinfo is not None:
            result = result.astimezone(timezone.utc).replace(tzinfo=None)
        # Return the result
        return result
    except ValueError:
        # Raise ValueError if parsing fails
        raise ValueError(f"Cannot parse '{date_string}' as ISO 8601")

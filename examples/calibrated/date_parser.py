from datetime import datetime, timezone


def parse_iso8601_date(date_string: str) -> datetime:
    """Returns a naive UTC datetime. Timezone-aware inputs are converted then stripped."""
    try:
        result = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        if result.tzinfo is not None:
            result = result.astimezone(timezone.utc).replace(tzinfo=None)
        return result
    except ValueError:
        raise ValueError(f"Cannot parse '{date_string}' as ISO 8601")

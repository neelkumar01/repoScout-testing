def parse_timeout(value: str) -> int:
    if value is None:
        return 30

    return int(value)
def parse_tags(value: str) -> list[str]:

    if not value:
        return []

    return [
        tag.strip()
        for tag in value.split(",")
        if tag.strip()
    ]
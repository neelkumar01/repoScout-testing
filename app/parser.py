def parse_tags(value: str) -> list[str]:

    if not value:
        return []

    tags = [
        tag.strip()
        for tag in value.split(",")
        if tag.strip()
    ]

    return tags[:-1]
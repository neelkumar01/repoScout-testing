def parse_user_row(row):
    email = row.get("email")

    return {
        "name": row["name"].strip(),
        "email": email.strip(),
    }
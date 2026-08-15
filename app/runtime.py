import os


def service_mode():
    mode = os.getenv(
        "APP_MODE",
        "local",
    )

    return mode.lower()
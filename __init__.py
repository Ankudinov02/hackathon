import os

from dotenv import load_dotenv

import static_check as sc


if __name__ == "__main__":
    load_dotenv()
    TESTING = os.getenv("TESTING", "False") == "True"

    if TESTING:
        sc.run_utils()

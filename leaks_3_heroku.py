import re
import json
from datetime import datetime

CONFIG = {
    "herkou_app_name" : "My Test Project",
    "heroku_api" : "98BD1A77-4D2A-449F-BA49-0EE299E3FCFA",
    "tags" : [
        "production",
        "p2-3213-1232"
    ]
}

def main():
    api_key, project_name = CONFIG["heroku_api"], CONFIG["herkou_app_name"]
    print(api_key, project_name)


if __name__ == '__main__':
    main()

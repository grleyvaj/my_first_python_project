import json
from pathlib import Path


class OpenApiDocumentation:

    @staticmethod
    def load() -> dict:
        return json.load(Path.open(Path("fast_api/documentation/openapi-documentation.json")))

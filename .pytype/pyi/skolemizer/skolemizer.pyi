# (generated with --quick)

os: module
uuid: module

class Skolemizer:
    __doc__: str
    baseurl_default_value: str
    baseurl_key: str
    skolemizations: set
    @staticmethod
    def _is_valid_uri(uri: str) -> bool: ...
    @staticmethod
    def add_skolemization() -> str: ...
    @staticmethod
    def get_baseurl() -> str: ...
    @staticmethod
    def has_skolemization_morfologi(skolemization: str) -> bool: ...
    @staticmethod
    def is_exact_skolemization(skolemization: str) -> bool: ...

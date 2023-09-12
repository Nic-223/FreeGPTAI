class CompletionError(Exception):
    """Completion error base class."""

class APIClientError(CompletionError):
    """Exception in the API client code."""

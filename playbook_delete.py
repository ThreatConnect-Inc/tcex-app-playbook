"""Playbook delete."""
# standard library
import logging

from ..app.key_value_store import KeyValueRedis  # type: ignore # pylint: disable=import-error
from ..app.key_value_store.key_value_store import (  # type: ignore # pylint: disable=import-error
    KeyValueStore,
)

# get tcex logger
_logger = logging.getLogger(__name__.split('.', maxsplit=1)[0])


class PlaybookDelete:
    """Playbook Write ABC"""

    def __init__(self, context: str, key_value_store: KeyValueStore):
        """Initialize the class properties."""
        self.context = context
        self.key_value_store = key_value_store

        # properties
        self.log = _logger

    def variable(self, key: str | None) -> int | None:
        """Delete method of CRUD operation for all data types.

        Only supported when using the Redis KV store.
        """
        if key is None:
            return None

        if not isinstance(self.key_value_store.client, KeyValueRedis):
            return None

        return self.key_value_store.client.delete(self.context, key.strip())

from typing import Any, Dict

_cache: Dict[str, Any] = {}


def get_cache(key: str) -> Any:
    return _cache.get(key)


def set_cache(key: str, value: Any) -> None:
    _cache[key] = value


def clear_cache() -> None:
    _cache.clear()



# simple in-memory cache, get_cache, set_cache, clear_cache, cache expiration, cache invalidation, cache keys, cache values, cache size limit, cache statistics, cache persistence 
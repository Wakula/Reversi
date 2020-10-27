from model.constants import Player

class Cache:
    _instance = None
    _cache = {}

    @staticmethod
    def get_instance():
        if Cache._instance is None:
            Cache._instance = Cache()

        return Cache._instance

    def save_state(self, field, player, available_moves):
        self._cache[self._get_key(field, player)] = available_moves

    def try_get_moves(self, field, player):
        key = self._get_key(field, player)
        if key in self._cache:
            return self._cache[key]
        return None

    def reset_cache(self):
        _cache = {}

    def _get_key(self, field, player):
        return str(player) + ''.join([str(row) for row in field])

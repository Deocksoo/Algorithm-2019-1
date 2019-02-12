class LRUCache:
    def __init__(self, size):
        self.size = size
        self.cache_memory = [""] * size
        self.last_used_index = 0

    def update(self, new_city):
        """
        :type new_city: string
        :rtype: None
        """
        if new_city in self.cache_memory:
            self.cache_memory.remove(new_city)
            self.cache_memory.insert(0, new_city)
        else:
            self.cache_memory.insert(0, new_city)
            self.cache_memory.pop(self.size)

    def find(self, city):
        """
        :type city: string
        :rtype: string
        LRU의 특징을 가지고 있음
        """
        if city in self.cache_memory:
            self.update(city)
            return "hit"
        else:
            self.update(city)
            return "miss"

def solution(cacheSize, cities):
    city_cache = LRUCache(cacheSize)
    executed_time = 0

    for city in cities:
        if city_cache.find(city.lower()) == "hit":
            executed_time += 1
        else:
            executed_time += 5
    
    return executed_time

if __name__ == "__main__":
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
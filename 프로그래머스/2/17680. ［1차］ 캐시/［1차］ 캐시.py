def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        city = city.lower()

        if city in cache:
            cache.append(city)
            cache.remove(city)
            answer += 1
        else:
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
            answer += 5

    return answer
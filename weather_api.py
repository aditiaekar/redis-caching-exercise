import json
import time
import redis


CACHE_TTL_SECONDS = 300

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)


def make_cache_key(city):
    return f"weather:{city.strip().lower()}"


def fetch_weather_from_api(city):
    time.sleep(2)

    return {
        "city": city,
        "temperature": 30,
        "condition": "Cerah",
        "message": "Data ini berasal dari simulasi API lambat"
    }


def get_weather(city):
    cache_key = make_cache_key(city)

    # 1. Cek data cuaca di Redis
    cached_weather = redis_client.get(cache_key)

    # 2. Jika cache tersedia, kembalikan data dari Redis
    if cached_weather:
        print("Cache HIT - data diambil dari Redis")
        return json.loads(cached_weather)

    # 3. Jika cache tidak tersedia, ambil data dari API lambat
    print("Cache MISS - data diambil dari API lambat")
    weather_data = fetch_weather_from_api(city)

    # 4. Simpan data ke Redis
    redis_client.set(cache_key, json.dumps(weather_data))

    # 5. Atur masa berlaku cache selama 300 detik
    redis_client.expire(cache_key, CACHE_TTL_SECONDS)

    return weather_data

def clear_weather_cache(city):
    cache_key = make_cache_key(city)
    redis_client.delete(cache_key)
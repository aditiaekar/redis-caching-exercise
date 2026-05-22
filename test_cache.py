import time
from weather_api import get_weather, clear_weather_cache


city = "Jakarta"

# Menghapus cache terlebih dahulu agar first call benar-benar lambat
clear_weather_cache(city)

# First call - should be slow because data is not cached yet
start = time.time()
result1 = get_weather(city)
time1 = time.time() - start

print(f"First call: {time1:.2f}s")
print(result1)
print("-" * 50)

# Second call - should be fast because data is already cached in Redis
start = time.time()
result2 = get_weather(city)
time2 = time.time() - start

print(f"Second call (cached): {time2:.2f}s")
print(result2)
print("-" * 50)

# Third call after 5 minutes:
# Setelah 300 detik, cache akan expired.
# Jika fungsi dipanggil lagi setelah cache expired, maka proses akan lambat kembali
# karena data harus diambil ulang dari API.
print("Third call after 5 minutes should be slow again because cache has expired.")
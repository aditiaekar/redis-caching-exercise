# Redis Caching Exercise

Project ini merupakan latihan implementasi Redis caching pada fungsi pengambilan data cuaca menggunakan Python dan Redis.

## Deskripsi

Pada kode awal, setiap pemanggilan fungsi `get_weather(city)` membutuhkan waktu sekitar 2 detik karena terdapat simulasi API lambat menggunakan `time.sleep(2)`.

Dengan Redis caching, hasil pemanggilan pertama akan disimpan ke Redis selama 5 menit atau 300 detik. Jika fungsi dipanggil kembali dengan kota yang sama sebelum cache expired, maka data akan langsung diambil dari Redis sehingga response time menjadi lebih cepat.

## Teknologi yang Digunakan

- Python
- Redis
- Docker
- Docker Compose

## Struktur Project

```text
redis-caching-exercise/
├── screenshot/
│   ├── run.png
│   └── testing.png
├── cache_report.md
├── docker-compose.yml
├── README.md
├── requirements.txt
├── test_cache.py
└── weather_api.py
```

## Cara Menjalankan Project

### 1. Jalankan Redis menggunakan Docker

```bash
docker compose up -d
```

### 2. Install dependency Python

```bash
pip install -r requirements.txt
```

### 3. Jalankan testing

```bash
python test_cache.py
```

## Contoh Hasil Testing

```bash
Cache MISS - data diambil dari API lambat
First call: 2.01s
{'city': 'Jakarta', 'temperature': 30, 'condition': 'Cerah', 'message': 'Data ini berasal dari simulasi API lambat'}
--------------------------------------------------
Cache HIT - data diambil dari Redis
Second call (cached): 0.00s
{'city': 'Jakarta', 'temperature': 30, 'condition': 'Cerah', 'message': 'Data ini berasal dari simulasi API lambat'}
--------------------------------------------------
Third call after 5 minutes should be slow again because cache has expired.
```

## Redis Commands

Beberapa command Redis yang digunakan dalam project ini:

```bash
GET weather:jakarta
SET weather:jakarta '{"city": "Jakarta", "temperature": 30, "condition": "Cerah"}'
EXPIRE weather:jakarta 300
TTL weather:jakarta
```

## Penjelasan Singkat

Pada pemanggilan pertama, data belum tersedia di Redis cache sehingga sistem menjalankan simulasi API lambat selama sekitar 2 detik.

Pada pemanggilan kedua, data sudah tersedia di Redis cache sehingga sistem tidak perlu menjalankan simulasi API lagi. Hasilnya, response time menjadi jauh lebih cepat.

## Dokumentasi

Penjelasan lengkap mengenai implementasi caching, hasil testing, screenshot, dan jawaban pertanyaan tersedia pada file:

```text
cache_report.md
```

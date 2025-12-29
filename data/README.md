# Данные USGS MRDS

## Загрузка данных

Данные не включены в репозиторий из-за большого размера (107 MB для GeoJSON).

### Автоматическая загрузка и конвертация

```bash
# Скачать данные USGS MRDS
curl -L -o data/mrds-csv.zip https://mrdata.usgs.gov/mrds/mrds-csv.zip

# Распаковать
unzip data/mrds-csv.zip -d data/

# Конвертировать в GeoJSON
python3 data/convert_to_geojson.py
```

### Ручная загрузка

1. Перейти на https://mrdata.usgs.gov/mrds/
2. Скачать файл `mrds-csv.zip` (23 MB)
3. Распаковать в папку `data/`
4. Запустить скрипт конвертации:

```bash
python3 data/convert_to_geojson.py
```

## Структура данных

После загрузки и конвертации в папке `data/` должны быть:

- `mrds.csv` - Исходные данные в CSV (131 MB)
- `mrds.geojson` - Конвертированные данные в GeoJSON (107 MB)
- `mrds.met` - Метаданные USGS
- `convert_to_geojson.py` - Скрипт конвертации
- `analyze_mrds.py` - Скрипт анализа данных

## Формат данных

### CSV поля

- `dep_id` - ID месторождения
- `site_name` - Название месторождения
- `latitude`, `longitude` - Координаты
- `country`, `state`, `county` - Локация
- `commod1`, `commod2`, `commod3` - Основные ресурсы
- `dev_stat` - Статус разработки
- `url` - Ссылка на детали USGS

### GeoJSON структура

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [longitude, latitude]
      },
      "properties": {
        "id": "...",
        "name": "...",
        "commodity": "...",
        "country": "...",
        "state": "...",
        "dev_status": "...",
        "url": "..."
      }
    }
  ]
}
```

## Статистика

- Всего записей: 304,632
- Записей с валидными координатами: 304,613
- Размер CSV: 131 MB
- Размер GeoJSON: 107 MB

## Источник

**USGS Mineral Resources Data System (MRDS)**
- URL: https://mrdata.usgs.gov/mrds/
- Лицензия: Public Domain
- Версия данных: 2016-03-15

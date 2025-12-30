import csv
import json
import os

print("Converting MRDS CSV to GeoJSON...")

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

features = []
processed = 0
invalid = 0

input_path = os.path.join(script_dir, 'mrds.csv')
print(f"Reading from: {input_path}")

with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        processed += 1
        
        # Only include records with valid coordinates
        if row.get('latitude') and row.get('longitude'):
            try:
                lat = float(row['latitude'])
                lon = float(row['longitude'])
                
                # Validate coordinate ranges
                if -90 <= lat <= 90 and -180 <= lon <= 180:
                    # Create GeoJSON feature
                    feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [lon, lat]
                        },
                        "properties": {
                            "id": row.get('dep_id', ''),
                            "name": row.get('site_name', 'Unknown'),
                            "commodity": row.get('commod1', ''),
                            "commodity2": row.get('commod2', ''),
                            "commodity3": row.get('commod3', ''),
                            "country": row.get('country', ''),
                            "state": row.get('state', ''),
                            "dev_status": row.get('dev_stat', ''),
                            "url": row.get('url', '')
                        }
                    }
                    features.append(feature)
                else:
                    invalid += 1
            except (ValueError, TypeError):
                invalid += 1
        else:
            invalid += 1
        
        # Progress indicator
        if processed % 50000 == 0:
            print(f"Processed {processed} records, valid: {len(features)}, invalid: {invalid}")

# Create GeoJSON FeatureCollection
geojson = {
    "type": "FeatureCollection",
    "features": features
}

# Save to file
output_path = os.path.join(script_dir, 'mrds.geojson')
print(f"Writing to: {output_path}")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(geojson, f)

print(f"\nConversion complete!")
print(f"Total records processed: {processed}")
print(f"Valid features: {len(features)}")
print(f"Invalid records: {invalid}")
print(f"Output file: {output_path}")
print(f"File size: {round(os.path.getsize(output_path) / 1024 / 1024, 2)} MB")

import csv
import json
from collections import Counter

# Read and analyze MRDS CSV
with open('/tmp/gh-issue-solver-1767036443116/data/mrds.csv', 'r', encoding='utf-8', errors='replace') as f:
    reader = csv.DictReader(f)
    
    total_count = 0
    valid_coords = 0
    commodities = Counter()
    countries = Counter()
    sample_records = []
    
    for i, row in enumerate(reader):
        total_count += 1
        
        # Check for valid coordinates
        if row.get('latitude') and row.get('longitude'):
            try:
                lat = float(row['latitude'])
                lon = float(row['longitude'])
                if -90 <= lat <= 90 and -180 <= lon <= 180:
                    valid_coords += 1
                    
                    # Count commodities
                    if row.get('commod1'):
                        commodities[row['commod1']] += 1
                    
                    # Count countries
                    if row.get('country'):
                        countries[row['country']] += 1
                    
                    # Collect first 5 valid samples
                    if len(sample_records) < 5:
                        sample_records.append({
                            'site_name': row.get('site_name'),
                            'latitude': lat,
                            'longitude': lon,
                            'country': row.get('country'),
                            'commodity': row.get('commod1'),
                            'dev_stat': row.get('dev_stat')
                        })
            except:
                pass
        
        # Process first 50000 for quick analysis
        if total_count >= 50000:
            break

print(f"Total records analyzed: {total_count}")
print(f"Records with valid coordinates: {valid_coords}")
print(f"\nTop 10 commodities:")
for comm, count in commodities.most_common(10):
    print(f"  {comm}: {count}")
print(f"\nTop 10 countries:")
for country, count in countries.most_common(10):
    print(f"  {country}: {count}")
print(f"\nSample records:")
print(json.dumps(sample_records, indent=2))

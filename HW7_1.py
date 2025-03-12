import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)  # Synthetic daily rainfall data

rainfall[np.random.choice(365, 100, replace=False)] = 0  # 100 dry days

#1. Boolean Arrays & Masks
print(f'Using Boolean arrays & Masks:'   )
print()
print(f'Rainy and dry day count:')
print()
rainfall[np.random.choice(365, 100, replace=False)] = 0

rainy_days = rainfall > 0
num_rainy_days = np.sum(rainy_days)

print(f'Number of rainy days: {num_rainy_days}')
#Heavy Rain
heavy_rain_days = rainfall > 5
percentage_heavy_rain_days = np.sum(heavy_rain_days) / len(rainfall) * 100

print(f'Percentage of days with heavy rain: {percentage_heavy_rain_days:.2f}%')

#Dry Spells
dry_days = rainfall == 0
dry_spells = np.diff(np.where(np.concatenate(([False], dry_days, [False])))[0])[::2].max()

print(f'Longest dry spell: {dry_spells} days')
print()
print(f'Fancy Indexing:')
#Top Rainfall Days
# Top 10 wettest days using fancy indexing
top_rainfall_days_indices = np.argsort(rainfall)[-10:]
top_rainfall_days = rainfall[top_rainfall_days_indices]

print('Top 10 wettest days (rainfall values):', top_rainfall_days)
# Monthly averages using fancy indexing
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_indices = np.arange(365)

start = 0
monthly_averages = []

for days in days_per_month:
    month_indices = day_indices[start:start+days]
    monthly_average = float(np.mean(rainfall[month_indices]))
    # Round the average to 2 decimal places for readability
    monthly_averages.append(round(monthly_average, 2))
    start += days

print('Monthly rainfall averages:', monthly_averages)

print(f'Sorting:')
# Sort the rainfall data in ascending order
sorted_rainfall = np.sort(rainfall)

# Find the median rainfall value
median_rainfall = np.median(rainfall)

print(f'Sorted Rainfall Data (in mm): {sorted_rainfall}')
print(f'Median Rainfall Value (in mm): {median_rainfall}')
# Find the 90th percentile of rainfall
percentile_90th = np.percentile(rainfall, 90)

print(f'90th percentile of rainfall (in mm): {percentile_90th:.2f}')

#Structured Data
print(f'Structured Data:')
# Creating a structured array
structured_rainfall = np.zeros(rainfall.size, dtype=[('day', 'i4'), ('rainfall', 'f4'), ('is_rainy', '?')])
structured_rainfall['day'] = np.arange(1, 366)
structured_rainfall['rainfall'] = rainfall
structured_rainfall['is_rainy'] = rainfall > 0  # Ensuring the Boolean value is True if rainfall > 0

# Display first 10 entries with explanation
print('First 10 entries of the structured data (day, rainfall, is_rainy):')
for entry in structured_rainfall[:10]:
    print(f'Day: {entry["day"]}, Rainfall: {entry["rainfall"]:.2f} mm, Is Rainy: {entry["is_rainy"]}')

# Extracting all rainy days
rainy_days_structured = structured_rainfall[structured_rainfall['is_rainy']]
average_rainfall_rainy_days = np.mean(rainy_days_structured['rainfall'])

print(f'Average rainfall on rainy days (in mm): {average_rainfall_rainy_days:.2f}')

# Sorting the structured array by rainfall
sorted_structured_rainfall = np.sort(structured_rainfall, order='rainfall')

# Printing the top 5 rainiest days with explanation
print('Top 5 rainiest days (day, rainfall, is_rainy):')
for entry in sorted_structured_rainfall[-5:]:
    print(f'Day: {entry["day"]}, Rainfall: {entry["rainfall"]:.2f} mm, Is Rainy: {entry["is_rainy"]}')

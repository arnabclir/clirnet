import pandas as pd

# Read content_data.csv normally
content_data = pd.read_csv('content_data.csv')

# Read views_reads.csv with only the first 4 columns (header says 4 cols but has more)
views_reads = pd.read_csv('data_content_views_reads.csv', usecols=['type_id', 'views', 'reads', 'date_Data'])

# Rename type_id to content_old_id for joining
views_reads = views_reads.rename(columns={'type_id': 'content_old_id'})

# Perform a full outer join on content_old_id (type_id maps to content_old_id)
joined = pd.merge(
    content_data,
    views_reads,
    on='content_old_id',
    how='outer'
)

# Sort by content_old_id for better readability
joined = joined.sort_values('content_old_id', na_position='last')

# Save the joined file
output_path = 'content_data_joined.csv'
joined.to_csv(output_path, index=False, encoding='utf-8')

print(f"Join completed successfully")
print(f"Rows in content_data.csv: {len(content_data)}")
print(f"Rows in data_content_views_reads.csv: {len(views_reads)}")
print(f"Rows in joined file: {len(joined)}")
print(f"Matching records: {len(joined[joined['views'].notna()])}")
print(f"Output file: {output_path}")

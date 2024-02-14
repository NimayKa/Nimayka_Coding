import pandas as pd

# Assuming your DataFrame is named df
data = {'listed_in': ['Documentaries', 'Crime TV Shows, International TV Shows, TV Action & Adventure',
                      'TV Dramas, TV Horror, TV Mysteries', 'Children & Family Movies, International TV Shows, Comedies']}
df = pd.DataFrame(data)

# Function to filter DataFrame based on a keyword and count the top 5 categories
def count_top_categories(keyword):
    filtered_df = df[df['listed_in'].str.contains(keyword, case=False)]
    if len(filtered_df) == 0:
        return "No matches found"
    categories = filtered_df['listed_in'].str.split(', ')
    flattened_categories = [category for sublist in categories for category in sublist]
    category_counts = pd.Series(flattened_categories).value_counts()
    return category_counts.head(5)

# Example usage:
keyword = "TV"
top_categories = count_top_categories(keyword)
print("Top 5 categories:")
print(top_categories)
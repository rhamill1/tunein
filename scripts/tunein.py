
import pandas as pd

input_df = pd.read_csv('data/sf_business_dataset.csv')
input_df.rename(columns={'Neighborhoods - Analysis Boundaries':'neighborhood',
                          'Business Corridor':'business_corridor',
                          'Business Location': 'business_location'}, inplace=True)


def explore_data(data_frame):
    print(input_df.shape)
    print(input_df.head())
    print(input_df.columns)

# explore_data(input_df)


# QUESTION 1. Identify pockets in San Francisco with high pockets of active businesses

active_businesses_df = input_df[input_df['Business End Date'].isnull()]
active_businesses_df = active_businesses_df.dropna(subset=['neighborhood'])


print(active_businesses_df.shape)

counter = active_businesses_df.groupby('neighborhood').neighborhood.count()
sorted_count = counter.sort_values(ascending=False)
print(sorted_count)
print(sorted_count.shape)

print(sorted_count.sum())


import pandas as pd

input_df = pd.read_csv('data/sf_business_dataset.csv')
input_df.rename(columns={'Neighborhoods - Analysis Boundaries':'neighborhood',
                          'Business Corridor':'business_corridor',
                          'Business Location': 'business_location',
                          'NAICS Code' : 'naics_code',
                          'NAICS Code Description': 'naics_description',
                          'Business Start Date': 'business_start_date'}, inplace=True)


def explore_data(data_frame):
    print(input_df.shape)
    print(input_df.head(n=20))
    print(input_df.columns)

# explore_data(input_df)




# QUESTION 1. Identify pockets in San Francisco with high pockets of active businesses
def high_pockets_active_business(input_df):
    active_businesses_df = input_df[input_df['Business End Date'].isnull()]
    active_businesses_df = active_businesses_df.dropna(subset=['neighborhood'])
    print(active_businesses_df.shape)

    counter = active_businesses_df.groupby('neighborhood').neighborhood.count()
    sorted_count = counter.sort_values(ascending=False)
    print(sorted_count)

    # sanity check that counts make sense
    print(sorted_count.shape)
    print(sorted_count.sum())

 # high_pockets_active_business(input_df)




# QUESTION 2. Identify the NAICS code and description for less popular industries.
def less_popular_industries(input_df):
    naics_df = input_df[['naics_code', 'naics_description']]
    naics_df = naics_df.dropna(subset=['naics_description'])
    print(naics_df.shape)

    naics_df['counter'] = 1
    naics_counted_df = naics_df.groupby(['naics_code', 'naics_description'])['counter'].count()
    sorted_count = naics_counted_df.sort_values(ascending=True)
    print(sorted_count)

    # sanity check that counts make sense
    print(sorted_count.shape)
    print(sorted_count.sum())

# less_popular_industries(input_df)




# QUESTION 3. What are the different industry types that have emerged in San Francsico over the years? Are there any trends?
def business_started_by_industry_year(input_df):
    industry_year_df = input_df[['naics_code', 'naics_description', 'business_start_date']]
    industry_year_df['start_year'] = industry_year_df['business_start_date'].str[-4:]
    industry_year_df = industry_year_df[['naics_code', 'naics_description', 'start_year']]

    industry_year_df = industry_year_df.dropna(subset=['naics_description', 'start_year'])

    industry_year_df['counter'] = 1
    industry_year_counted_df = industry_year_df.groupby(['naics_code', 'naics_description', 'start_year'])['counter'].count()

    print(industry_year_counted_df.shape)

    print(industry_year_counted_df.head(n=30))

# business_started_by_industry_year(input_df)

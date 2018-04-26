
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

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

    sorted_count.plot.bar()
    plot.show()


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

    sorted_count.plot.barh()
    plot.show()

# less_popular_industries(input_df)




# QUESTION 3. What are the different industry types that have emerged in San Francsico over the years? Are there any trends?
def business_started_by_industry_year(input_df):
    industry_year_df = input_df[['naics_code', 'naics_description', 'business_start_date']]
    industry_year_df['start_year'] = industry_year_df['business_start_date'].str[-4:]
    industry_year_df = industry_year_df[['naics_code', 'naics_description', 'start_year']]

    # print(len(industry_year_df))
    industry_year_df['start_year'] = pd.to_numeric(industry_year_df.start_year, errors='coerce')
    industry_year_df = industry_year_df.where(industry_year_df['start_year'] <= 2018).dropna()

    # print(len(industry_year_df))
        # remove and check for years > 2018

    industry_year_df = industry_year_df.dropna(subset=['naics_description', 'start_year'])

    industry_year_df['counter'] = 1
    industry_year_counted_df = industry_year_df.groupby(['naics_code', 'naics_description', 'start_year'])['counter'].count()
    industry_year_counted_df = industry_year_counted_df.to_frame()

    # print(industry_year_counted_df.shape)
    # print(industry_year_counted_df.head())

    # print(industry_year_df.sort_values(by=['start_year'], axis=0, ascending=False))
        # there are records > 2018
    max_year = industry_year_df[['start_year']].max(axis=0)
    min_year = industry_year_df[['start_year']].min(axis=0)
    distinct_years = [i for i in range(min_year,max_year + 1)]

    distinct_naics = industry_year_df[['naics_code', 'naics_description']].drop_duplicates().reset_index(drop=True)
    distinct_naics = distinct_naics.values.tolist()

    complete_industry_years = [[naics_info[0], naics_info[1], year, 0] for naics_info in distinct_naics for year in distinct_years]


    new_columns = ['naics_code', 'naics_description', 'start_year','counter2']
    zeros_df = pd.DataFrame(complete_industry_years, columns=new_columns)
    zeros_df = zeros_df.set_index(['naics_code', 'naics_description', 'start_year'])

    stage_df = pd.merge(zeros_df, industry_year_counted_df, how='left', left_index=True, right_index=True)
    stage_df['new_companies'] = stage_df.counter.combine_first(stage_df.counter2)
    stage_df = stage_df.reset_index(['naics_code', 'naics_description','start_year'])
    pivoted_df = stage_df.pivot_table(values='new_companies', index=['naics_code', 'naics_description'], columns='start_year')

    print(pivoted_df)
    print(stage_df)
    print(stage_df.shape)




    year = [1960, 1970, 1980, 1990, 2000, 2010]
    pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
    pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]
    plot.plot(year, pop_pakistan, color='g')
    plot.plot(year, pop_india, color='orange')
    plot.xlabel('Countries')
    plot.ylabel('Population in million')
    plot.title('Pakistan India Population till 2010')
    # plot.show()



business_started_by_industry_year(input_df)

import pandas as pd


def get_percent_count(country, count_type, covid_json, world_pop_df):
    """Returns the percentage count of given country and type

    :param country: country for which covid data is needed
    :param count_type: type of covid count ['confirmed', 'deaths', 'recovered']
    :param covid_json: covid data json
    :world_pop_df: pandas dataframe with world population details
    :return: percentage of covid count for the given country and type
    """

    covid_value = covid_json[country][-1][count_type]
    population_value = world_pop_df[
                        world_pop_df['Country'] == country].Pop.mean()
    percent_count = covid_value / population_value * 100

    return round(percent_count, 5)

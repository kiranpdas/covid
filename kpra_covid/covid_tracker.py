from typing import Dict
import pandas as pd
from datetime import datetime


def get_percent_count(country: str, count_type: str, covid_json: Dict, world_pop_df: pd.DataFrame) -> float:
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
    percent_count = round(covid_value / population_value * 100, 5)

    return percent_count


def get_current_count(country: str, count_type: str, covid_json: Dict) -> int:
    """Returns the actual count of given country and type

    :param country: country for which covid data is needed
    :param count_type: type of covid count ['confirmed', 'deaths', 'recovered']
    :param covid_json: covid data json
    :return: covid count for the given country and type
    """

    covid_value = covid_json[country][-1][count_type]
    return covid_value


def get_covid_date(country: str, covid_json: Dict) -> datetime:
    """Returns the latest date of covid data

    :param country: country for which covid data is needed
    :param covid_json: covid data json
    :return: latest date of the covid data as date object
    """

    covid_date = datetime.strptime(
        covid_json[country][-1]['date'], '%Y-%m-%d')
    return covid_date

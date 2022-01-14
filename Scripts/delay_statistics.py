from typing import Iterable
import pandas as pd


def _get_delay_statistic(feature_observations: pd.Series,
                         delay_observations: pd.Series,
                         statistic: str,
                         ) -> tuple[pd.Series, dict]:
    """
    Converts a categorical feature into a statistical estimate of a numeric feature by leveraging pandas `groupby` and `transform`
    methods. Because this is a wrapper function, limitations stem from those of its subcomponents. This function is intended for 
    internal use by `get_delay_statistics`.

    Parameters:

        `feature_observations`: pd.Series - The categorical feature column.

        `delay_observations`: pd.Series - The numeric column to use for extracting statistics.

        `statistic`: str - the statistic to be extracted from `delay_observations` using`feature_observations`.

    Returns:

        tuple[pd.Series, dict] - A tuple with the transformed series and a dictionary containing the mappings to be applied
            on the test data.

    """

    _df = pd.concat([feature_observations, delay_observations], axis=1)
    feature_name, delay_name = _df.columns

    stat_series = _df.groupby(feature_name)[
        delay_name].transform(statistic)

    _mapping = _df.groupby(feature_name)[
        delay_name].agg(statistic)

    stat_mapping = {index: rank for index,
                    rank in zip(_mapping.index, _mapping)}

    return stat_series, stat_mapping


def get_delay_statistics(df: pd.DataFrame,
                         features: Iterable,
                         delay_observations: pd.Series,
                         statistics: Iterable = ['mean', 'median'],
                         ) -> tuple[pd.DataFrame, dict[dict]]:
    """
    Applies `_get_delay_statistic` on a list of categorical features (expected subset of `df`.columns) to generate a pandas
    DataFrame of ranked columns as well as a dict of their mappings.

    Parameters:

        `df`: pd.DataFrame - Input DataFrame that is expected to contain the categorical `features` for which to extract statistics from the
            `delay_observations`.

        `features`: Iterable - An iterable of categorical column names present in the input `df` to be ranked. Expected to be columns in the
            input DataFrame (`df`).

        `delay_observations`: pd.Series - The numeric delay feature Series from which to extract statistics for the categorical `features`. Must 
            be a column in the input DataFrame (`df`).

        `statistics`: Iterable = ['mean', 'median'] - the statistics to be extracted from the `delay_observations` using the `features`.

    Returns:

        tuple[pd.DataFrame, dict[dict]] - A tuple containing both the transformed DataFrame and a dictionary with mappings corresponding to
            the specified statistics to be applied on the test data.

    """
    delay_statistics = {}
    mappings = {}

    for feature in features:
        for statistic in statistics:
            (delay_statistics[f'{feature}_{statistic}'],
             mappings[f'{feature}_{statistic}']) = _get_delay_statistic(df[feature],
                                                                        delay_observations,
                                                                        statistic,
                                                                        )

    return pd.DataFrame(delay_statistics), mappings


def main():
    # NOTE: Add any code to be executed when this script is ran in this function.
    pass


if __name__ == '__main__':
    main()

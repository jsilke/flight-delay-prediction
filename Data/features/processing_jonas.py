import pandas as pd


def rank_column_by_mean(df: pd.DataFrame,
                        to_rank_name: str,
                        rank_by_name: str,
                        method: str = 'dense',
                        ) -> tuple[pd.Series, dict]:
    """
    Converts categorical columns into ordinal columns using the pandas `groupby`, `rank` and `transform` categorical methods.
    Because this is a wrapper function, limitations stem from those of its subcomponents.

    Parameters:

        `df`: pd.DataFrame - Input DataFrame that is expected to contain both the categorical column (`to_rank_name`) to be 
            ranked as well as the numeric column (`rank_by_name`) to use for ranking values.

        `to_rank_name`: str - The name of the categorical column to be ranked as a string. Must be a column in the
            input DataFrame (`df`).

        `rank_by_name`: str - The name of the numeric column to be used for ranking the categorical column. Must be 
            a column in the input DataFrame (`df`).

        `method`: str = 'dense' - the method to be used by the pandas `rank` method to determine ranking. Our default of 
            'dense' is sensible, but {'average', 'min', 'max', 'first', 'dense'} are all accepted here.

    Returns:

        tuple[pd.Series, dict] - A tuple with the transformed series and a dictionary containing the mappings to be applied
            on the test data.

    """
    _metric_series = df.groupby(to_rank_name)[rank_by_name].transform('mean')
    ranked_series = _metric_series.rank(method=method)

    _mapping = df.groupby(to_rank_name)[rank_by_name].mean().rank()
    rank_mapping = {index: rank for index,
                    rank in zip(_mapping.index, _mapping)}

    return ranked_series, rank_mapping


def rank_features_by_mean(df: pd.DataFrame,
                          to_rank_names: list,
                          rank_by_name: str,
                          method: str = 'dense',
                          ) -> tuple[pd.DataFrame, dict[dict]]:
    """
    Applies `rank_column_by_mean` on a list of categorical features (expected subset of `df`.columns) to generate a pandas
    DataFrame of ranked columns as well as a dict of their mappings.

    Parameters:

        `df`: pd.DataFrame - Input DataFrame that is expected to contain both the categorical column (`to_rank_name`) to be 
            ranked as well as the numeric column (`rank_by_name`) to use for ranking values.

        `to_rank_names`: list - The list of names of the categorical columns to be ranked. Expected be columns in the
            input DataFrame (`df`).

        `rank_by_name`: str - The name of the numeric column to be used for ranking the categorical column. Must be 
            a column in the input DataFrame (`df`).

        `method`: str = 'dense' - the method to be used by the pandas `rank` method to determine ranking. Our default of 
            'dense' is sensible, but {'average', 'min', 'max', 'first', 'dense'} are all accepted here.

    Returns:

        tuple[pd.DataFrame, dict[dict]] - A tuple with the transformed DataFrame and a dictionary containing the mappings 
            to be applied on the test data.

    """
    ranked_features = {}
    mappings = {}

    for to_rank_name in to_rank_names:
        ranked_features[f'{to_rank_name}_ranked'], mappings[to_rank_name] = rank_column_by_mean(df,
                                                                                                to_rank_name,
                                                                                                rank_by_name,
                                                                                                method)

    return pd.DataFrame(ranked_features), mappings


def main():
    # NOTE: Add any code to be executed when this script is ran in this function.
    pass


if __name__ == '__main__':
    main()

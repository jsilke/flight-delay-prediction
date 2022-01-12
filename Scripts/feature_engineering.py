import pandas as pd


def rank_column_by_metric(df_with_rank_by_and_to_rank: pd.DataFrame,
                          column_to_rank: str,
                          rank_by_column: str,
                          method: str = 'dense',
                          ) -> tuple[pd.Series, dict]:
    """
    Converts categorical columns into ordinal columns using the pandas groupby and transform categorical methods.
    Because this is a wrapper function, limitations stem from those of its subcomponents.

    Parameters:

        `df_with_rank_by_and_to_rank`: pd.DataFrame - Input DataFrame that is expected to contain both the column
            to be ranked as well as the column to use for ranking values.

        `column_to_rank`: str - The name of the categorical column to be ranked as a string. Must be a column in the
            input DataFrame.

        `rank_by_column`: str - The name of the numeric column to be used for ranking the categorical column. Must be 
            a column in the input DataFrame.

        `metric`: str = 'mean' - The metric (function name) to be broadcasted over the numeric column to establish rankings 
            by the pandas `transform` method. Defaults to 'mean'.

        `method`: str = 'dense' - the method to be used by the pandas rank method to determine ranking. Our default of 
            'dense' is sensible, but {‘average’, ‘min’, ‘max’, ‘first’, ‘dense’} are all accepted here.

    Returns:
        tuple[pd.Series, dict] - A tuple with the transformed series and a dictionary containing the mappings to be applied
            on the test data.
    """
    _metric_series = df_with_rank_by_and_to_rank.groupby(
        column_to_rank)[rank_by_column].transform('mean')
    ranked_series = _metric_series.rank(method=method)

    _mapping = df_with_rank_by_and_to_rank.groupby(
        column_to_rank)[rank_by_column].mean().rank()
    rank_mapping = {index: rank for index,
                    rank in zip(_mapping.index, _mapping)}

    return ranked_series, rank_mapping


def main():
    # NOTE: Add any code to be executed when this script is ran in this function.
    pass


if __name__ == '__main__':
    main()

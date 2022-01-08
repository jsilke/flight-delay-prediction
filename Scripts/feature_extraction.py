#!/usr/bin/env python3
import os
import re

RELATIVE_PATH = "flight-delay-prediction/Data"


def get_features_from_description(
    data_description_path: str,
    output_path: str = None,
    output_delimiter: str = "\n",
    feature_locator: str = "-",
    description_delimiter: str = "**",
):
    """
    Takes in a file describing a table and its features and uses the provided delimiters to parse them and write the outputs to seperate
    feature files for each table so they can be used as headings. This function assumes that the table name is listed on the first line
    of the file and that it is flanked by the `delimiter`. Another assumption is that the first occurrence of the `delimiter` on each
    relevant line is the target string to be extracted (i.e. table name or feature).

    Parameters:
        `data_description_path`: str - path (including file name) to the data descriptions to be parsed.

        `output_path`: str - desired output directory location to store the feature files. This will be created if it does not exist.
            Default will use the current working directory.

        `output_delimiter`: str = '\n' - allows the default output delimiter to be swapped from the default of '\n' to facilitate insertion as
            a header row.

        `feature_locator`: str = "-" - a character present at the beginning of each feature-containing line that is used to parse them.
            Default values are specific to this project and assumes that all feature lines, and ONLY feature lines, begin with this character.

        `description_delimiter`: str = "**" - string used to split the table and feature names from the rest of the information on the line. This
            implementation assumes the same delimiter for both table names and features. The default value is specific to this project.

    Output:
        A text file (.txt) names after the associated table containing a line-delimited (i.e. '\n') feature list in the specified output_path/ directory.
    """
    if output_path is None:  # Explicit is better than implicit.
        output_path = os.getcwd()

    with open(data_description_path, "r") as description_file:
        # split the first line using the delimiter and collect the first occurring internal element resulting from the split.
        table_name = description_file.readline().split(description_delimiter)[1]
        # makes a list of features from lines that begin with the feature locator.
        features = [
            line.split(description_delimiter)[1]
            for line in description_file
            if re.search(fr"^{feature_locator}", line)
        ]

    features_string = output_delimiter.join(features)

    with open(f"{output_path}/{table_name}.txt", "w") as feature_file:
        feature_file.write(features_string)


def get_descriptions(
    directory_path: str = f"{RELATIVE_PATH}/descriptions",
    output_path: str = f"{RELATIVE_PATH}/features",
    output_delimiter: str = "\n",
):
    """
    Takes in a directory of description files (expects markdown [.md] files) and iterates through each file to generate feature files.
    This function assumes all .md files in the directory are data descriptions that should be used to produce feature files.

    Parameters:
        `directory_path`: str = f"{RELATIVE_PATH}/descriptions" - directory containing description files to be used to generate feature files.
            The default value is project-specific.

        `output_path`: str = f"{RELATIVE_PATH}/features" - path for the directory that feature files should be generated in. The default value
            is project-specific.

        `output_delimiter`: str = '\n' - allows the default output delimiter to be swapped from the default of '\n' to facilitate insertion as
            a header row.

    Output:
        A separate text file (.txt) of features for each table in the specified output_path/ directory.
    """

    # check if the desired output director exists and create it if not.
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    directory = os.fsencode(directory_path)

    for file in os.listdir(directory):
        description_file = os.fsdecode(file)
        if description_file.endswith(".md"):
            get_features_from_description(
                f"{directory_path}/{description_file}", output_path, output_delimiter
            )
        else:
            continue


def main():
    get_descriptions()


if __name__ == "__main__":
    main()

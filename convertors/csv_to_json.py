import argparse
import pandas as pd


def main(file_path, output_path):
    df = pd.read_csv(file_path)
    df.to_json(orient="records", path_or_buf=output_path, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add scripts options
    parser.add_argument("-f", "--file", help="Csv file path",
                        type=str, required=True)
    parser.add_argument("-o", "--output", help="Json file path",
                        type=str, required=True)

    args = parser.parse_args()

    main(args.file, args.output)
    print(f"Json file outputed : {args.output}")

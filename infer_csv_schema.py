# infer_csv_schema.py
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["pandas","pandera"]
# ///

import pandas as pd
import pandera as pa
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: uv run infer_csv_schema.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    df = pd.read_csv(csv_file)
    schema = pa.infer_schema(df)
    print(schema)


if __name__ == "__main__":
    main()

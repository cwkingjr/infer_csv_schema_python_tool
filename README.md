# Infer CSV Pantera Schema

Quick little tool to run with uv to infer a csv schema with pandas and pandera. The output is a Pandera Inferred Schema.

## Usage

```
uv run infer_csv_schema.py <csv_file>
```

## Example output

```
uv run infer_csv_schema.py ./fake-data-3000-rows.csv

<Schema DataFrameSchema(
    columns={
        'Rank': <Schema Column(name=Rank, type=DataType(int64))>
        'Severity': <Schema Column(name=Severity, type=DataType(int64))>
        'ShortId': <Schema Column(name=ShortId, type=DataType(object))>
        'Title': <Schema Column(name=Title, type=DataType(object))>
        'Status': <Schema Column(name=Status, type=DataType(object))>
        'NextStepAction': <Schema Column(name=NextStepAction, type=DataType(object))>
        'CreateDate': <Schema Column(name=CreateDate, type=DataType(object))>
        'LastUpdatedDate': <Schema Column(name=LastUpdatedDate, type=DataType(object))>
        'AssignedFolderLabel': <Schema Column(name=AssignedFolderLabel, type=DataType(object))>
        'Labels': <Schema Column(name=Labels, type=DataType(object))>
        'Description': <Schema Column(name=Description, type=DataType(object))>
        'RootCauses': <Schema Column(name=RootCauses, type=DataType(object))>
        'Priority': <Schema Column(name=Priority, type=DataType(object))>
        'Tags': <Schema Column(name=Tags, type=DataType(object))>
        'AssigneeIdentity': <Schema Column(name=AssigneeIdentity, type=DataType(object))>
        'ResolvedByIdentity': <Schema Column(name=ResolvedByIdentity, type=DataType(object))>
        'SubmitterIdentity': <Schema Column(name=SubmitterIdentity, type=DataType(object))>
        'RequesterIdentity': <Schema Column(name=RequesterIdentity, type=DataType(object))>
        'tpa_from (string)': <Schema Column(name=tpa_from (string), type=DataType(object))>
    },
    checks=[],
    parsers=[],
    coerce=True,
    dtype=None,
    index=<Schema Index(name=None, type=DataType(int64))>,
    strict=False,
    name=None,
    ordered=False,
    unique_column_names=False,
    metadata=None,
    add_missing_columns=False
)>
```

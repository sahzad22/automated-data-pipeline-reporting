# Operations Runbook

## Normal Run

```bash
python -m src.pipeline
```

## Expected outcome

- API responds successfully
- Required fields are present
- Data passes validation
- SQL table is refreshed
- Pipeline audit receives a SUCCESS row
- Power BI refresh can be enabled through environment settings

## Failure handling

API failures are retried. Validation failures stop the load before SQL is changed. SQL errors are logged and recorded as failed runs when possible.

## Production scheduling

For enterprise deployments, schedule with Airflow, Azure Data Factory, Microsoft Fabric Data Factory or GitHub Actions.

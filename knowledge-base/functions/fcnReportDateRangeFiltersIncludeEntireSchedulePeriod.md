# fcnReportDateRangeFiltersIncludeEntireSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnReportDateRangeFiltersIncludeEntireSchedulePeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| reportDateRangeStart | DateTime | |
| reportDateRangeEnd | DateTime | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is a boolean initially true.if (reportDateRangeStart <> null and reportDateRangeEnd <> null and aSchedulePeriodPay <> null) then{if (reportDateRangeStart.toLocalDate().isAfter(aSchedulePeriodPay.schedulePeriodStart.toLocalDate()) or              reportDateRangeEnd.toLocalDate().isBefore(aSchedulePeriodPay.schedulePeriodEnd.toLocalDate())) then{retVal = false.}}return retVal.
```

## Llamado por

- [fcnBuildUnutilizedReserveList](fcnBuildUnutilizedReserveList.md)


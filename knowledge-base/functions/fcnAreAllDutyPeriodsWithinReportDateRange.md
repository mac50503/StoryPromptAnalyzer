# fcnAreAllDutyPeriodsWithinReportDateRange

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAreAllDutyPeriodsWithinReportDateRange`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
retVal is a boolean initially true.if (reportFilterStart <> null and reportFilterStart <> null and     aTripPay <> null and aTripPay.dutyPeriodPayList.size() > 0) then{                                                           for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (retVal = true and fcnIsDateTimeWithinReportFilterRange(it.reportDateTime, reportFilterStart, reportFilterEnd) = false) thenretVal = false.}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)

## Llamado por

- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)


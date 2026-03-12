# fcnGetEventDateForExperiencePay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetEventDateForExperiencePay`

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
retVal is some DateTime initially null.if (reportFilterStart <> null and reportFilterStart <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (fcnIsDateTimeWithinReportFilterRange(it.releaseDateTime, reportFilterStart, reportFilterEnd)) thenretVal = it.releaseDateTime.}}//fcnShow("===>>> returning from function fcnGetEventDateForExperiencePay ... trip = " aTripPay.tripNameAndDate " ...reportFilterStart = " reportFilterStart " ...reportFilterEnd = " reportFilterEnd " ...return value = " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateExperiencePayBucket](fcnCalculateExperiencePayBucket.md)


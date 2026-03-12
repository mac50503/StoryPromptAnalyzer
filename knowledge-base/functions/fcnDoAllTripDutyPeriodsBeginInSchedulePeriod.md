# fcnDoAllTripDutyPeriodsBeginInSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoAllTripDutyPeriodsBeginInSchedulePeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
retVal is a boolean initially true.if (aTripPay <> null and aTripPay.dutyPeriodPayList.size() > 0 and aSchedulePeriodPay <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (retVal = true)thenretVal = fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(it, aSchedulePeriodPay).}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)

## Llamado por

- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)


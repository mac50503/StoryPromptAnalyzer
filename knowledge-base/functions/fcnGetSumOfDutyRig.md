# fcnGetSumOfDutyRig

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetSumOfDutyRig`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aTripPay <> null) then {for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do retVal += it.dutyPeriodRig.}return retVal.
```

## Llamado por

- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)


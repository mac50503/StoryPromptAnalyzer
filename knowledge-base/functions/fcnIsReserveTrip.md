# fcnIsReserveTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsReserveTrip`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayTrip <> null) then{if (aPayTrip.payTripInflight <> null and aPayTrip.payTripInflight.isReserveTrip) thenretVal =  true.else if (aPayTrip.assignmentLabel =(ignoring case) "R") thenretVal = true.}return retVal.
```

## Llamado por

- [fcnCalculateDutyPeriodContributionForProductivityPay](fcnCalculateDutyPeriodContributionForProductivityPay.md)
- [fcnCalculateForcedPremiumTripsPayValue](fcnCalculateForcedPremiumTripsPayValue.md)
- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnShowTripPaySummary](fcnShowTripPaySummary.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
05/06/2015 - Tim A. refactored to check labels for FO but check isReserve property for IF
09/30/2024 - Removed S label check
```


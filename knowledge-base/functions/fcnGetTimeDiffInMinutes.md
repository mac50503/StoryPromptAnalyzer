# fcnGetTimeDiffInMinutes

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetTimeDiffInMinutes`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateTime1 | DateTime | |
| dateTime2 | DateTime | |

## Lógica de negocio

```blaze
if (dateTime1 <> null and dateTime2 <> null) then{return Duration.newInstance(dateTime1, dateTime2).standardMinutes.}elsereturn 0.
```

## Llamado por

- [fcnCalculateActualDutyDuration](fcnCalculateActualDutyDuration.md)
- [fcnCalculateCrewMealPerdiumDomesticLegs](fcnCalculateCrewMealPerdiumDomesticLegs.md)
- [fcnCalculateCrewMealPerdiumInternationalLegs](fcnCalculateCrewMealPerdiumInternationalLegs.md)
- [fcnCalculateDHR](fcnCalculateDHR.md)
- [fcnCalculateDutyDurationAtLegBlockIn](fcnCalculateDutyDurationAtLegBlockIn.md)
- [fcnCalculateFaaCompRestUnderReserve](fcnCalculateFaaCompRestUnderReserve.md)
- [fcnCalculateFaaRest](fcnCalculateFaaRest.md)
- [fcnCalculateFaaRestForWindowUnderReserve](fcnCalculateFaaRestForWindowUnderReserve.md)
- [fcnCalculateFaaRestPreferLRR](fcnCalculateFaaRestPreferLRR.md)
- [fcnCalculateFaaRestUnderReserve](fcnCalculateFaaRestUnderReserve.md)
- [fcnCalculateLegDutyHours](fcnCalculateLegDutyHours.md)
- [fcnCalculateLimoLegPay](fcnCalculateLimoLegPay.md)
- [fcnCalculateStartOfRestForPay](fcnCalculateStartOfRestForPay.md)
- [fcnCalculateThrAndAdgAndDhr](fcnCalculateThrAndAdgAndDhr.md)
- [fcnCalculateTripDutyHours](fcnCalculateTripDutyHours.md)
- [fcnCalculateTripHourlyRatio](fcnCalculateTripHourlyRatio.md)
- [fcnDetermineCombinedDutyDurationForDutyPeriod](fcnDetermineCombinedDutyDurationForDutyPeriod.md)
- [fcnDetermineCombinedDutyDurationForTrip](fcnDetermineCombinedDutyDurationForTrip.md)
- [fcnDetermineDutyPeriodRest](fcnDetermineDutyPeriodRest.md)
- [fcnDetermineDutyPeriodTransientTerms](fcnDetermineDutyPeriodTransientTerms.md)
- [fcnDetermineLimoOfZeroDuration](fcnDetermineLimoOfZeroDuration.md)
- [fcnDetermineNonflyTripRest](fcnDetermineNonflyTripRest.md)
- [fcnDeterminePlanningDutyPeriodTransientTerms](fcnDeterminePlanningDutyPeriodTransientTerms.md)
- [fcnDeterminePlanningTripTransientTerms](fcnDeterminePlanningTripTransientTerms.md)
- [fcnDetermineTripTransientTerms](fcnDetermineTripTransientTerms.md)
- [fcnGetDHREndDateTime](fcnGetDHREndDateTime.md)
- [fcnGetNextTripsWithinHours](fcnGetNextTripsWithinHours.md)
- [fcnGetTimeDiffInHours](fcnGetTimeDiffInHours.md)
- [fcnIsNonPaidLimoLeg](fcnIsNonPaidLimoLeg.md)
- [fcnMaxFaaRestInWindow](fcnMaxFaaRestInWindow.md)
- [fcnSetCombinedDutyDurationStart](fcnSetCombinedDutyDurationStart.md)
- [fcnSetPayDutyPeriodTransientTerms](fcnSetPayDutyPeriodTransientTerms.md)
- [fcnSetReserveBlockDutyPeriodDutyAmount](fcnSetReserveBlockDutyPeriodDutyAmount.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```


# fcnDistributeToLateReturnBuckets

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDistributeToLateReturnBuckets`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |
| thePayTrip | PayTrip | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
if2025PayLROFixEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theTripPay.beginDateTime, "IF_2025_LRO_PAY_FIX_BLAZE_EFFECTIVE_DATETIME").if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.thePayLeg is some PayLeg initially fcnGetFirstLegOfDutyPeriod(thePayTrip.lastDutyPeriod).if(thePayTrip <> null and thePayTrip.lastDutyPeriod <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theTripPay.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if(fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(theTripPay.beginDateTime, "IF_2024_LRO_EFFECTIVE_DATE") and theTripPay.tripPayInflight <> nulland theTripPay.tripPayInflight <> unknown  and thePayTrip.payTripOverrideValues <> nulland thePayTrip.payTripOverrideValues <> unknown and theSchedulePeriodPay <> nulland theSchedulePeriodPay <> unknownand thePayTrip.payTripOverrideValues.isLateReturnOverride = true and ((theTripPay.endSchedulePeriodPay = theSchedulePeriodPay and not if2025PayLROFixEffectiveDateActiveFlag) or (thePayLeg is not null and fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay(thePayTrip.lastDutyPeriod.dutyPeriodPay,theSchedulePeriodPay ) and if2025PayLROFixEffectiveDateActiveFlag)) and thePayTrip.lastDutyPeriod <> null and thePayTrip.lastDutyPeriod <> unknown and thePayTrip.lastDutyPeriod.lastLeg <> null and thePayTrip.lastDutyPeriod.lastLeg <> unknownand thePayTrip.lastDutyPeriod.lastLeg.payLegInflight <> null and thePayTrip.lastDutyPeriod.lastLeg.payLegInflight <> unknown) then {if(if2025PayLROFixEffectiveDateActiveFlag and not if2025NewDomicileDayPayEffectiveDateActiveFlag) then {if( theTripPay.tripPayInflight.positionA = true or thePayTrip.lastDutyPeriod.lastLeg.payLegInflight.crewPosition = "FAA") then{fcnDistributeToPayBucket(theSchedulePeriodPay, "LROABUCKET",  1.0, 1.0,  thePayLeg.scheduledDepartureDateTime, reportFilterStart, reportFilterEnd, thePayTrip.tripPay).} else{fcnDistributeToPayBucket(theSchedulePeriodPay, "LROBUCKET",  1.0, 1.0,  thePayLeg.scheduledDepartureDateTime, reportFilterStart, reportFilterEnd, thePayTrip.tripPay).}} else {if( theTripPay.tripPayInflight.positionA = true or thePayTrip.lastDutyPeriod.lastLeg.payLegInflight.crewPosition = "FAA") then{fcnDistributeToPayBucket(theSchedulePeriodPay, "LROABUCKET",  1.0, 1.0,  thePayTrip.lastDutyPeriod.reportDateTime, reportFilterStart, reportFilterEnd, thePayTrip.tripPay).} else{fcnDistributeToPayBucket(theSchedulePeriodPay, "LROBUCKET",  1.0, 1.0,  thePayTrip.lastDutyPeriod.reportDateTime, reportFilterStart, reportFilterEnd, thePayTrip.tripPay).}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDistributeToPayBucket](fcnDistributeToPayBucket.md)
- [fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay](fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay.md)
- [fcnGetFirstLegOfDutyPeriod](fcnGetFirstLegOfDutyPeriod.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)


# fcnDoesDutyPeriodPayBeginInSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoesDutyPeriodPayBeginInSchedulePeriodPay`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(aDutyPeriodPay <> null and aDutyPeriodPay.tripPay <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aDutyPeriodPay.tripPay.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if (aSchedulePeriodPay <>null and aDutyPeriodPay <> null) then{if (aDutyPeriodPay.payDutyPeriod.payDutyPeriodInflight <> null) then{ if (aDutyPeriodPay <> null and aSchedulePeriodPay <> null and     aSchedulePeriodPay.schedulePeriodStart <> null and aSchedulePeriodPay.schedulePeriodEnd <> null and      if2025NewDomicileDayPayEffectiveDateActiveFlag and fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriodPay.payDutyPeriod) <> null and          fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriodPay.payDutyPeriod) <> null and         fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriodPay.payDutyPeriod).toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and     fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriodPay.payDutyPeriod).toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) thenreturn true.else if (aDutyPeriodPay <> null and aSchedulePeriodPay <> null and     aSchedulePeriodPay.schedulePeriodStart <> null and aSchedulePeriodPay.schedulePeriodEnd <> null and     if2025NewDomicileDayPayEffectiveDateActiveFlag = false and         fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriodPay.payDutyPeriod).isBefore(aSchedulePeriodPay.schedulePeriodStart) is equal to false and     fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriodPay.payDutyPeriod).isAfter(aSchedulePeriodPay.schedulePeriodEnd) is equal to false) thenreturn true.elsereturn false.}else{if (aDutyPeriodPay <> null and aSchedulePeriodPay <> null      and aDutyPeriodPay.reportDateTime is not null and aSchedulePeriodPay.schedulePeriodStart is not null and      if2025NewDomicileDayPayEffectiveDateActiveFlag and         aSchedulePeriodPay.schedulePeriodEnd is not null and          aDutyPeriodPay.reportDateTime.toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and         aDutyPeriodPay.reportDateTime.toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) thenreturn true.if (aDutyPeriodPay <> null and aSchedulePeriodPay <> null and      if2025NewDomicileDayPayEffectiveDateActiveFlag = false and         aDutyPeriodPay.reportDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) is equal to false and         aDutyPeriodPay.reportDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) is equal to false) thenreturn true.elsereturn false.}}return false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFirstFlyingLeg](fcnGetFirstFlyingLeg.md)
- [fcnGetFirstFlyingLegScheduledDepartureDateTime](fcnGetFirstFlyingLegScheduledDepartureDateTime.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnAllDutiesInTripThisMonthHaveRapAssociations](fcnAllDutiesInTripThisMonthHaveRapAssociations.md)
- [fcnCalculateExperiencePayBucket](fcnCalculateExperiencePayBucket.md)
- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnDetermineDutyTripExcess](fcnDetermineDutyTripExcess.md)
- [fcnDoAllTripDutyPeriodsBeginInSchedulePeriod](fcnDoAllTripDutyPeriodsBeginInSchedulePeriod.md)
- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)
- [fcnGetNonRONpremium](fcnGetNonRONpremium.md)
- [fcnGetReserveBlockDutiesReportingInSchedulePeriodPay](fcnGetReserveBlockDutiesReportingInSchedulePeriodPay.md)
- [fcnGetSumOfThisMonthLegDistributedPayForTrip](fcnGetSumOfThisMonthLegDistributedPayForTrip.md)
- [fcnGetSumOfThisMonthLegPremiumForTrip](fcnGetSumOfThisMonthLegPremiumForTrip.md)
- [fcnGetThisMonthDutyPeriodPay](fcnGetThisMonthDutyPeriodPay.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
6/16/2015 - Ben Lang - DE6669 - Added logic to use the first leg's scheduleDepartureDateTime for Inflight
```


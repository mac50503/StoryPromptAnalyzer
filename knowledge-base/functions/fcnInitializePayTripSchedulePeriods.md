# fcnInitializePayTripSchedulePeriods

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnInitializePayTripSchedulePeriods`

## Propósito
US18085 - Melissa S - 7/29/2014 - Refactored for performance

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |
| theSchedulPeriodList | List<SchedulePeriod> | |

## Lógica de negocio

```blaze
if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(thePayTrip.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").if (thePayTrip is not equal to null and     theSchedulPeriodList is not equal to null and     theSchedulPeriodList.size() > 0) then{if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {aNewStartSPName is a string initially fcnFindSchedulePeriodName(thePayTrip.beginDateTime, theSchedulPeriodList).aNewEndSPName is a string initially fcnFindSchedulePeriodName(thePayTrip.endDateTime, theSchedulPeriodList).if(aNewStartSPName <> null and aNewStartSPName <> unknown) then {thePayTrip.startsInSchedulePeriod = aNewStartSPName.}if(aNewEndSPName <> null and aNewStartSPName <> unknown) then {thePayTrip.endsInSchedulePeriod = aNewEndSPName.}}thePayTrip.tripStartSchedulePeriod = fcnFindSchedulePeriod(thePayTrip.startsInSchedulePeriod, theSchedulPeriodList).if (thePayTrip.tripStartSchedulePeriod <> null) then{fcnXrefSchedulePeriodToSchedulePeriodPay(thePayTrip.tripStartSchedulePeriod, a SchedulePeriodPay).fcnShow("===>>> fcnInitializePayTripSchedulePeriods with trip " thePayTrip.tripName " ...startsInSchedulePeriod - " thePayTrip.startsInSchedulePeriod " ...start SP = " thePayTrip.tripStartSchedulePeriod.schedulePeriodName " ...SP Pay = " thePayTrip.tripStartSchedulePeriod.schedulePeriodPay.schedulePeriodName).}// If the PayTrip starts and ends in the same schedule period, don't need to loop through the list again, just use the same SchedulePeriodif (thePayTrip.startsInSchedulePeriod = thePayTrip.endsInSchedulePeriod) then {thePayTrip.tripEndSchedulePeriod = thePayTrip.tripStartSchedulePeriod.} else {thePayTrip.tripEndSchedulePeriod = fcnFindSchedulePeriod(thePayTrip.endsInSchedulePeriod, theSchedulPeriodList).if (thePayTrip.tripEndSchedulePeriod <> null) then{fcnXrefSchedulePeriodToSchedulePeriodPay(thePayTrip.tripEndSchedulePeriod, a SchedulePeriodPay).fcnShow("===>>> fcnInitializePayTripSchedulePeriods with trip " thePayTrip.tripName " ...endsInSchedulePeriod - " thePayTrip.endsInSchedulePeriod " ...end SP = " thePayTrip.tripEndSchedulePeriod.schedulePeriodName " ...SP Pay = " thePayTrip.tripEndSchedulePeriod.schedulePeriodPay.schedulePeriodName).}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindSchedulePeriod](fcnFindSchedulePeriod.md)
- [fcnFindSchedulePeriodName](fcnFindSchedulePeriodName.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`
- [fcnXrefSchedulePeriodToSchedulePeriodPay](fcnXrefSchedulePeriodToSchedulePeriodPay.md)

## Llamado por

- [fcnInitializePayTripListSchedulePeriods](fcnInitializePayTripListSchedulePeriods.md)

## Historial de cambios

```
US18085 - Melissa S - 7/29/2014 - Refactored for performance
```


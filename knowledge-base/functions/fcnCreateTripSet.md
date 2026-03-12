# fcnCreateTripSet

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripSet
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCreateTripSet`

## Propósito
US18085 - Melissa S - 7/29/2014 - New function for shared TripSet creation

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| inFlightRequest | boolean | |
| aSchedulePeriodPayList | List<SchedulePeriodPay> | |

## Lógica de negocio

```blaze
aTripSet is some TripSet initially a TripSet.if (inFlightRequest) then{aTripSet.schedulePeriodName = aPayTrip.startsInSchedulePeriod.if (aSchedulePeriodPayList <> null) then aTripSet.schedulePeriodName = fcnGetSchedulePeriodNameForDateTime(aPayTrip.nonDeadheadBeginDateTime, aSchedulePeriodPayList). aTripSet.startDateTime = aPayTrip.beginDateTime.if (aPayTrip.nonDeadheadBeginDateTime <> null) then aTripSet.startDateTime = aPayTrip.nonDeadheadBeginDateTime.aTripSet.endDateTime = aPayTrip.endDateTime.if (aPayTrip.nonDeadheadEndDateTime <> null) then aTripSet.endDateTime = aPayTrip.nonDeadheadEndDateTime.aTripSet.tripSetName = "TripSet-" aTripSet.schedulePeriodName "-" aTripSet.startDateTime.toString().}else //FO Request{aTripSet.schedulePeriodName = aPayTrip.startsInSchedulePeriod;aTripSet.tripSetName = "TripSet-" aPayTrip.startsInSchedulePeriod "-" aPayTrip.beginDateTime.toString().aTripSet.startDateTime = aPayTrip.beginDateTime.aTripSet.endDateTime = aPayTrip.endDateTime.}aTripSet.addPayTrip(aPayTrip).aPayTrip.tripSet = aTripSet.if (aPayTrip.multiDutyPeriodTrip) then aTripSet.incrementCountOfMultiDutyPeriodTrips(). fcnShow("aTripSet.tripSetName " aTripSet.tripSetName).fcnShow("aTripSet.schedulePeriodName " aTripSet.schedulePeriodName).fcnShow("aTripSet.startDateTime " aTripSet.startDateTime).fcnShow("aTripSet.endDateTime " aTripSet.endDateTime).return aTripSet.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSchedulePeriodNameForDateTime](fcnGetSchedulePeriodNameForDateTime.md)
- `fcnShow()`

## Llamado por

- [fcnCreateInflightTripSets](fcnCreateInflightTripSets.md)

## Historial de cambios

```
US18085 - Melissa S - 7/29/2014 - New function for shared TripSet creation
```


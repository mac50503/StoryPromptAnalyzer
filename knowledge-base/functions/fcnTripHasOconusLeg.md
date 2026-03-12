# fcnTripHasOconusLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnTripHasOconusLeg`

## Propósito
Ben Lang - US8942 - 03/10/14 - The fcnTripHasOconusLeg returns true if the there is a PayLeg in the PayTrip that has a departureLocation outside the continental US,

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
if (aPayTrip.dutyPeriodList is not equal to null and aPayTrip.dutyPeriodList.size() > 0) then {for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do {if (it.legList is not equal to null and it.legList.size() > 0) then {for each PayLeg in it.legList as an array of PayLeg do {aDepartureStation is some Station initially aGlobalDataCache.stationMap.get(it.departureLocation). // Added a station variable to check for null because of failing gherkinsanArrivalStation is some Station initially aGlobalDataCache.stationMap.get(it.arrivalLocation).if (aDepartureStation is not equal to null and aDepartureStation.isContinentalUS is equal to false) thenreturn true.if (anArrivalStation is not equal to null and anArrivalStation.isContinentalUS is equal to false) thenreturn true.}}}}return false.
```

## Llamado por

- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)

## Historial de cambios

```
Ben Lang - US8942 - 03/10/14 - The fcnTripHasOconusLeg returns true if the there is a PayLeg in the PayTrip that has a departureLocation outside the continental US,
otherwise return false.
US18085 - Melissa S - 7/29/2014 - Refactored for performance
```


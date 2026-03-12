# fcnSetTripDomicileTimeZone

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnSetTripDomicileTimeZone`

## Propósito
6/20/25 - APIC-1584 -Santosh Kudumu: New function to set domicile time zone for Flying Trip,Reserves and Non-flies.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnSetTripDomicileTimeZone with Trip = " aPayTrip.tripName "....sequence number" aPayTrip.sequenceNumber);domicileStation is some Station initially a Station;// Flying TripTime Zone Assignment if(aPayTrip.firstDutyPeriod <> null and aPayTrip.firstDutyPeriod <> unknown and aPayTrip.firstDutyPeriod.beginLocation <> null and aPayTrip.firstDutyPeriod.beginLocation <> unknown) then {domicileStation = aGlobalDataCache.stationMap.get(aPayTrip.firstDutyPeriod.beginLocation);}// ReserveTime Zone Assignmentelse if(aPayTrip.firstDutyPeriod<> null and aPayTrip.firstDutyPeriod<> unknown and aPayTrip.firstDutyPeriod.firstLeg <> null and aPayTrip.firstDutyPeriod.firstLeg<> unknown andaPayTrip.firstDutyPeriod.firstLeg.departureLocation <> null and aPayTrip.firstDutyPeriod.firstLeg.departureLocation <> unknown) then {domicileStation = aGlobalDataCache.stationMap.get(aPayTrip.firstDutyPeriod.firstLeg.departureLocation);}// Non-FlyTime Zone assignmentelse if(fcnIsNotABlankString(aPayTrip.nonFlyCode)) then {domicileStation = aGlobalDataCache.stationMap.get(aPayTrip.nonFlyBase);}if(domicileStation <> null and domicileStation <> unknown and fcnIsNotABlankString(domicileStation.timezone)) then {aPayTrip.tripDomicileTimeZone = domicileStation.timezone;}fcnShow("===>>> EXITING fcnSetTripDomicileTimeZone...");
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsNotABlankString](fcnIsNotABlankString.md)
- `fcnShow()`

## Llamado por

- [fcnCreateTripPayResponse](fcnCreateTripPayResponse.md)

## Historial de cambios

```
6/20/25 - APIC-1584 -Santosh Kudumu: New function to set domicile time zone for Flying Trip,Reserves and Non-flies.
9/11/25 - APIC-1580 - Jeremiah Connelly:  Updated the Non-FlyTime Zone Assignment logic to remove it being "defaulted" to Chicago and Throw Exception
9/26/2025 APIC-1656 : Removed The exception Part for Nonfly
```


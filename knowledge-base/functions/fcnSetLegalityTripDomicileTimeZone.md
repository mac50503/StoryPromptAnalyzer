# fcnSetLegalityTripDomicileTimeZone

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnSetLegalityTripDomicileTimeZone`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegalityTrip | LegalityTrip | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnSetLegalityTripDomicileTimeZone with Trip = " aLegalityTrip.tripName "....sequence number" aLegalityTrip.sequenceNumber);domicileStation is some Station initially a Station;// Flying TripTime Zone Assignment if(aLegalityTrip.firstDutyPeriod <> null and aLegalityTrip.firstDutyPeriod <> unknown and aLegalityTrip.firstDutyPeriod.beginLocation <> null and aLegalityTrip.firstDutyPeriod.beginLocation <> unknown) then {domicileStation = aGlobalDataCache.stationMap.get(aLegalityTrip.firstDutyPeriod.beginLocation);}// ReserveTime Zone Assignmentelse if(aLegalityTrip.firstDutyPeriod<> null and aLegalityTrip.firstDutyPeriod<> unknown and aLegalityTrip.firstDutyPeriod.firstLeg <> null and aLegalityTrip.firstDutyPeriod.firstLeg<> unknown andaLegalityTrip.firstDutyPeriod.firstLeg.departureLocation <> null and aLegalityTrip.firstDutyPeriod.firstLeg.departureLocation <> unknown) then {domicileStation = aGlobalDataCache.stationMap.get(aLegalityTrip.firstDutyPeriod.firstLeg.departureLocation);}// Non-FlyTime Zone assignmentelse if(aLegalityTrip.nonFlyCode <> null and aLegalityTrip.nonFlyCode <> unknown and aLegalityTrip.nonFlyBase <> null and aLegalityTrip.nonFlyBase <> unknown) then {domicileStation = aGlobalDataCache.stationMap.get(aLegalityTrip.nonFlyBase);}if(domicileStation <> null and domicileStation <> unknown and domicileStation.timezone <> null and domicileStation <> unknown) then {aLegalityTrip.tripDomicileTimeZone = domicileStation.timezone;}fcnShow("===>>> EXITING fcnSetLegalityTripDomicileTimeZone...");
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`


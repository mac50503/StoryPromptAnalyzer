# fcnAssociateAirportStandbyWithOverlappingTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAssociateAirportStandbyWithOverlappingTrip`

## Propósito
US16560 - MP - 07/17/2014 - This function will look for a reserve trip to associate with an airport standby, and set the association if one is found.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |
| thePayTripList | List<PayTrip> | |
| tripIndex | integer | |

## Lógica de negocio

```blaze
if (thePayTrip.nonFlyCode is equal to (ignoring case) ("AS1" or "ASB1" or "ASB2" or "ASB3" or "ASB4") and tripIndex<thePayTripList.size()-1) then {theNextTrip is some PayTrip initially thePayTripList.get(tripIndex + 1).if (theNextTrip<>null and                    fcnIsNonFlyTrip(theNextTrip) = false and    //// DE7174 - do not associate airport standbys with nonfly trips    theNextTrip.beginDateTime.isBefore(thePayTrip.beginDateTime) = false and                    theNextTrip.beginDateTime.isAfter(thePayTrip.endDateTime )= false) then{if(theNextTrip.payTripInflight.isReserveTrip = false)then theNextTrip.associatedAirportStandby = thePayTrip.thePayTrip.associatedTrip = theNextTrip.}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsNonFlyTrip](fcnIsNonFlyTrip.md)

## Historial de cambios

```
US16560 - MP - 07/17/2014 - This function will look for a reserve trip to associate with an airport standby, and set the association if one is found.
10/22/2014 Corey Gu US18781 - Replaced theTrip.assignmentLabel =(ignoring case) "R" with payTripInflight.isReserveTrip = true.
US18581 - Corey Gu 10/10/2014 - Added a new condition to check it the rest between the endDateTime of the Airport Standby trip and the beginDateTime of  my reserve trip &lt; 8
```


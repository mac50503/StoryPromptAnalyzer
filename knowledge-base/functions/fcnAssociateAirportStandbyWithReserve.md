# fcnAssociateAirportStandbyWithReserve

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAssociateAirportStandbyWithReserve`

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
if thePayTrip.nonFlyCode is equal to (ignoring case) ("AS1" or "ASB1" or "ASB2" or "ASB3" or "ASB4") then {tripCounter is an integer initially tripIndex + 1.theNextTrip is some PayTrip.breakLoop is a boolean initially false.while (tripCounter < thePayTripList.size() and breakLoop =  false) do {theNextTrip = thePayTripList.get(tripCounter).if theNextTrip.beginDateTime.isAfter(thePayTrip.beginDateTime) then {if (fcnIsSameSwaDay(thePayTrip.beginDateTime, theNextTrip.beginDateTime) and      Duration.newInstance(thePayTrip.endDateTime, theNextTrip.beginDateTime).standardHours < 8) then{if (theNextTrip.payTripInflight.isReserveTrip = true and    theNextTrip.associatedAirportStandby is equal to null) then {theNextTrip.associatedAirportStandby = thePayTrip.    thePayTrip.associatedReserveTrip = theNextTrip.    breakLoop = true.}} elsebreakLoop = true.}tripCounter+=1.}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsSameSwaDay](fcnIsSameSwaDay.md)

## Historial de cambios

```
US16560 - MP - 07/17/2014 - This function will look for a reserve trip to associate with an airport standby, and set the association if one is found.
10/22/2014 Corey Gu US18781 - Replaced theTrip.assignmentLabel =(ignoring case) "R" with payTripInflight.isReserveTrip = true.
US18581 - Corey Gu 10/10/2014 - Added a new condition to check it the rest between the endDateTime of the Airport Standby trip and the beginDateTime of  my reserve trip &lt; 8
```


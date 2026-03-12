# fcnDutyHasNightFlightLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDutyHasNightFlightLeg`

## Propósito
01/27/2016 CSCH-375 Matt C - Initial development -  function for determining a night flight violation

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| theNightFlightMaxDutyList | List<NightFlightMaxDuty> | |

## Lógica de negocio

```blaze
aReturnVal is some LegalityLeg initially null;aNightFlightMaxDuty is some NightFlightMaxDuty initially null;if (theNightFlightMaxDutyList.size() > 0) then {for each NightFlightMaxDuty in theNightFlightMaxDutyList  as an array of NightFlightMaxDuty               do {aNightFlightMaxDuty = it;for each LegalityLeg in theDutyPeriod.legList as an array of LegalityLegdo {if (aReturnVal = null and theDutyPeriod.contDutyDuration > aNightFlightMaxDuty.maxDuty)  then {             if  (aNightFlightMaxDuty.rangeDescription = "departure" ) then {               //leg departure is a night flight violation        if (fcnLegArrivesDepartsWithinACurrentOrPreviousDayWindow(aNightFlightMaxDuty.startTime, aNightFlightMaxDuty.endTime, it.scheduledDepartureInLocalTimezone.toLocalTime())) then {aReturnVal =  it.        }} else if (aNightFlightMaxDuty.rangeDescription = "arrival")   then {           //leg arrival is a night flight violation        if (fcnLegArrivesDepartsWithinACurrentOrPreviousDayWindow(aNightFlightMaxDuty.startTime, aNightFlightMaxDuty.endTime, it.scheduledArrivalInLocalTimezone.toLocalTime())) then {aReturnVal =  it.       }} else if (aNightFlightMaxDuty.rangeDescription = "non-stop")  then {     //leg nonstop is a night flight violation      if (fcnLegArrivalDepartureSpansACurrentOrPreviousDayWindow(aNightFlightMaxDuty.startTime, aNightFlightMaxDuty.endTime, it.scheduledDepartureInLocalTimezone, it.scheduledArrivalInLocalTimezone)) then {aReturnVal =  it.       }}}                               }}}return aReturnVal;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnLegArrivalDepartureSpansACurrentOrPreviousDayWindow](fcnLegArrivalDepartureSpansACurrentOrPreviousDayWindow.md)
- [fcnLegArrivesDepartsWithinACurrentOrPreviousDayWindow](fcnLegArrivesDepartsWithinACurrentOrPreviousDayWindow.md)

## Historial de cambios

```
01/27/2016 CSCH-375 Matt C - Initial development -  function for determining a night flight violation
```


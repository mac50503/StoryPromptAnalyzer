# fcnIsPriorCalendarDayAReserveBlock

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnIsPriorCalendarDayAReserveBlock`

## Propósito
04/19/2025 Namratha BLAZER-391 This Function is related to code template ctPriorCalendayDayReserveBlock used in FAA Rest

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |
| thePreviousTrip | LegalityTrip | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.//theTrip is a Reserve Block and thePreviousTrip is a FlyingTrip or a Duty Nonflyif(thePreviousTrip <> unknown and thePreviousTrip <> null and theTrip <> unknown and theTrip <> null) then {if(theTrip.priorDayReserveBlock is true) then {retVal =  true.}else if (theTrip.priorConsecutiveReserveBlock = null) then{ if (thePreviousTrip.priorConsecutiveReserveBlock <> unknown and thePreviousTrip.priorConsecutiveReserveBlock <> null and thePreviousTrip.priorConsecutiveReserveBlock.lastDutyPeriod <> unknown and thePreviousTrip.priorConsecutiveReserveBlock.lastDutyPeriod <> null and fcnIsDatesOnSameCalendarDay(theTrip.beginDateTime.minusDays(1),thePreviousTrip.priorConsecutiveReserveBlock.lastDutyPeriod.reportDateTime) ) then{retVal =  true.}}else if(theTrip.priorConsecutiveReserveBlock <> null and theTrip.priorConsecutiveReserveBlock.lastDutyPeriod <> unknown and theTrip.priorConsecutiveReserveBlock.lastDutyPeriod <>  null) then {if (fcnIsDatesOnSameCalendarDay(theTrip.beginDateTime.minusDays(1),theTrip.priorConsecutiveReserveBlock.lastDutyPeriod.reportDateTime)) then{retVal =  true.}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDatesOnSameCalendarDay](fcnIsDatesOnSameCalendarDay.md)

## Historial de cambios

```
04/19/2025 Namratha BLAZER-391 This Function is related to code template ctPriorCalendayDayReserveBlock used in FAA Rest
```


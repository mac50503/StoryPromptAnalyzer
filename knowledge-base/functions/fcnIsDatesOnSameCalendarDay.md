# fcnIsDatesOnSameCalendarDay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnIsDatesOnSameCalendarDay`

## Propósito
04/10/2025 Namratha BLAZER-364 To Check if two dateTimes is on Same Calendar Day

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDateTime1 | DateTime | |
| aDateTime2 | DateTime | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if(aDateTime1 is known and aDateTime1 <> null and aDateTime2 is known and aDateTime2 <> null) then {earlierDate is some DateTime initially  DateTime.newInstance(aDateTime1.year, aDateTime1.monthOfYear, aDateTime1.dayOfMonth, 0, 0, 0);laterDate is some DateTime initially   DateTime.newInstance(aDateTime2.year, aDateTime2.monthOfYear, aDateTime2.dayOfMonth, 0, 0, 0);if (earlierDate.equals(laterDate))then {retVal = true;}}return  retVal.
```

## Llamado por

- [fcnIsPriorCalendarDayAReserveBlock](fcnIsPriorCalendarDayAReserveBlock.md)

## Historial de cambios

```
04/10/2025 Namratha BLAZER-364 To Check if two dateTimes is on Same Calendar Day
```


# fcnGetEndOfDayInSWATime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetEndOfDayInSWATime`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| baseDate | DateTime | |

## Lógica de negocio

```blaze
//fcnShow("===>>> INSIDE FUNCTION  fcnGetEndOfDayInSWATime with arg baseDate = " baseDate).// Return a DateTime that represents the end of the day in SWA time for the DateTime passed in  if baseDate <> null then {if (baseDate.hourOfDay < 3) then { // if DateTime arg passed in is before 3 AM...//fcnShow("===>>> RUNNING FUNCTION  fcnGetEndOfDayInSWATime before 3 AM").return DateTime.newInstance(baseDate.year, baseDate.monthOfYear, baseDate.dayOfMonth, 3, 00).} else {//fcnShow("===>>> RUNNING FUNCTION  fcnGetEndOfDayInSWATime after 3 AM").nextDay is some DateTime initially baseDate.plusHours(24).//fcnShow("===>>> nextDay: " nextDay).return DateTime.newInstance(nextDay.year, nextDay.monthOfYear, nextDay.dayOfMonth, 3, 00);}}return null.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnDistributePerdiemPayToDutyPeriods](fcnDistributePerdiemPayToDutyPeriods.md)
- [fcnGetCountOfSwaDays](fcnGetCountOfSwaDays.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```


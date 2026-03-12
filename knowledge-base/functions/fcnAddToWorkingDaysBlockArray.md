# fcnAddToWorkingDaysBlockArray

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnAddToWorkingDaysBlockArray`

## Propósito
4/13/2015 - Melissa S - Updated to always set start to 3am

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theBeginDateTime | DateTime | |
| theEndDateTime | DateTime | |

## Lógica de negocio

```blaze
theWorkingDaysBlock is a WorkingDaysBlock initially  {startDateTime = theBeginDateTime.endDateTime = theEndDateTime.}// The working days block should always start at 3am to include the entire dayif (theBeginDateTime.hourOfDay < 3) then {theWorkingDaysBlock.startDateTime = theBeginDateTime.minusDays(1).withTime(3,0,0,0).} else {theWorkingDaysBlock.startDateTime = theBeginDateTime.withTime(3,0,0,0).}// Should be 2:59 but because of DST issues we have to use 3:00 and then compare with < laterif (theEndDateTime.hourOfDay < 3) thentheWorkingDaysBlock.endDateTime = theEndDateTime.withTime(3, 0, 0, 0).elsetheWorkingDaysBlock.endDateTime = theEndDateTime.plusDays(1).withTime(3, 0, 0, 0).workingDaysBlockArray.append(theWorkingDaysBlock).
```

## Llamado por

- [fcnDetermineWorkingDay](fcnDetermineWorkingDay.md)
- [fcnDetermineWorkingDayWithDomicileTime](fcnDetermineWorkingDayWithDomicileTime.md)

## Historial de cambios

```
4/13/2015 - Melissa S - Updated to always set start to 3am
```


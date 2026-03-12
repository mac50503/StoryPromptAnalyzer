# fcnIsSameSwaDay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnIsSameSwaDay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDateTime1 | DateTime | |
| aDateTime2 | DateTime | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.adjDateTime1 is some DateTime initially aDateTime1.adjDateTime2 is some DateTime initially aDateTime2.if (aDateTime1 <> null and aDateTime2 <> null) then{if (aDateTime1.hourOfDay < 3) then adjDateTime1 = aDateTime1.minusDays(1).if (aDateTime2.hourOfDay < 3) then adjDateTime2 = aDateTime2.minusDays(1).if (adjDateTime1.year = adjDateTime2.year and      adjDateTime1.dayOfYear = adjDateTime2.dayOfYear) thenretVal = true.}return retVal.
```

## Llamado por

- [fcn](fcn.md)
- [fcnAssociateAirportStandbyWithReserve](fcnAssociateAirportStandbyWithReserve.md)
- [fcnAssociateInflightPayDutyPeriodsToRaps](fcnAssociateInflightPayDutyPeriodsToRaps.md)
- [fcnCalculateReserveSingleAndMultiDayGuarantee](fcnCalculateReserveSingleAndMultiDayGuarantee.md)
- [fcnDetermineWorkingDayWithDomicileTime](fcnDetermineWorkingDayWithDomicileTime.md)
- [fcnIsPayTripMultiDay](fcnIsPayTripMultiDay.md)


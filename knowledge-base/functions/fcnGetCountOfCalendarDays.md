# fcnGetCountOfCalendarDays

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetCountOfCalendarDays`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aStartDateTime | DateTime | |
| aEndDateTime | DateTime | |

## Lógica de negocio

```blaze
retVal is an integer initially 0.if(aStartDateTime is not null and aEndDateTime is not null) then {retVal = 1+ Days.daysBetween(aStartDateTime.toLocalDate(), aEndDateTime.toLocalDate()).days.}return retVal.
```

## Llamado por

- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)


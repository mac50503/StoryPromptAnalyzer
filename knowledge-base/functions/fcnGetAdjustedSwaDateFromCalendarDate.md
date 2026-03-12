# fcnGetAdjustedSwaDateFromCalendarDate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetAdjustedSwaDateFromCalendarDate`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| sourceDate | DateTime | |

## Lógica de negocio

```blaze
//fcnShow("===> ENTERING function fcnGetAdjustedSwaDateFromCalendarDate ...sourceDate = " sourceDate).retVal is some DateTime initially sourceDate.if (sourceDate <> null and sourceDate.hourOfDay < 3) then retVal =sourceDate.minusDays(1).if (retVal <> null) thenretVal = retVal.withTime(3, 0, 0, 0). /// sets time of day returned to 3AM...return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`


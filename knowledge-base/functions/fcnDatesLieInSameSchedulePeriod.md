# fcnDatesLieInSameSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnDatesLieInSameSchedulePeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDateTime1 | DateTime | |
| aDateTime2 | DateTime | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.adjDateTime1 is some DateTime initially aDateTime1.adjDateTime2 is some DateTime initially aDateTime2.if (aDateTime1 <> null and aDateTime2 <> null) then{if (aDateTime1.hourOfDay < 3) then adjDateTime1 = aDateTime1.minusDays(1).if (aDateTime2.hourOfDay < 3) then adjDateTime2 = aDateTime2.minusDays(1).if (adjDateTime1.year = adjDateTime2.year and adjDateTime1.monthOfYear = adjDateTime2.monthOfYear) then retVal = true.}return retVal.
```


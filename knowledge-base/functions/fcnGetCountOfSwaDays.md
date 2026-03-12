# fcnGetCountOfSwaDays

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetCountOfSwaDays`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aStartDateTime | DateTime | |
| aEndDateTime | DateTime | |

## Lógica de negocio

```blaze
retVal is an integer initially 1.end is some DateTime initially fcnGetEndOfDayInSWATime(aStartDateTime).while (end.isAfter(aEndDateTime) = false) do{retVal +=1.end = end.plusDays(1).}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetEndOfDayInSWATime](fcnGetEndOfDayInSWATime.md)

## Llamado por

- [fcnInitializeNonflyPayDays](fcnInitializeNonflyPayDays.md)


# fcnGetStartOfPreviousSwaDay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetStartOfPreviousSwaDay`

## Propósito
17 Feb - Tim A - USCH-2158 - added this utility function

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDateTime | DateTime | |

## Lógica de negocio

```blaze
retVal is some DateTime initially null.if (aDateTime.hourOfDay < 3) then retVal =aDateTime.minusDays(2).elseretVal =aDateTime.minusDays(1).retVal = retVal.withTime(3, 0, 0, 0). /// sets start of day retuned to 3AM...return retVal.
```

## Llamado por

- [fcnSetPreviousDayReserve](fcnSetPreviousDayReserve.md)

## Historial de cambios

```
17 Feb - Tim A - USCH-2158 - added this utility function
```


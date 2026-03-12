# fcnGetDateTimeStringOrNull

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetDateTimeStringOrNull`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDateTime | DateTime | |

## Lógica de negocio

```blaze
retVal is a string.retVal = "null".if (aDateTime <> null) thenretVal = DateTimeUtilities.getShortDateTimeString(aDateTime).return retVal.
```


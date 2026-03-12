# fcnFormatLegalityDate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnFormatLegalityDate`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateToFormat | DateTime | |

## Lógica de negocio

```blaze
return DateTimeUtilities.formatLegalityDateTime(dateToFormat, "ddMMMyy").
```

## Llamado por

- [fcnDetermineMixedLanguageMessage](fcnDetermineMixedLanguageMessage.md)
- [fcnReserveBlockTripConflictLegality](fcnReserveBlockTripConflictLegality.md)
- [fcnTripConflictLegality](fcnTripConflictLegality.md)


# fcnFormatLegalityDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnFormatLegalityDateTime`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateToFormat | DateTime | |

## Lógica de negocio

```blaze
if (dateToFormat = null) then { return "".} else {return DateTimeUtilities.formatLegalityDateTime(DateTimeUtilities.convertDateTimeToCentral(dateToFormat), "HHmm") " on " DateTimeUtilities.formatLegalityDateTime(DateTimeUtilities.convertDateTimeToCentral(dateToFormat), "ddMMMyy").}
```

## Llamado por

- [fcnDetermineMixedLanguageMessage](fcnDetermineMixedLanguageMessage.md)
- [fcnReserveBlockTripConflictLegality](fcnReserveBlockTripConflictLegality.md)
- [fcnTripConflictLegality](fcnTripConflictLegality.md)


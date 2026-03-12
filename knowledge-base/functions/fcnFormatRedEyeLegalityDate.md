# fcnFormatRedEyeLegalityDate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnFormatRedEyeLegalityDate`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| workingLegAfterRedEye | LegalityLeg | |
| workingLegAfterLabeledRedEye | LegalityLeg | |

## Lógica de negocio

```blaze
if(workingLegAfterRedEye <> null) then {return DateTimeUtilities.formatLegalityDateTime(workingLegAfterRedEye.scheduledDepartureDateTime, "ddMMMyy").} else if(workingLegAfterLabeledRedEye <> null) then {return DateTimeUtilities.formatLegalityDateTime(workingLegAfterLabeledRedEye.scheduledDepartureDateTime, "ddMMMyy").} else {return null.}
```


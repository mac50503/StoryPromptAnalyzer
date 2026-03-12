# fcnGetPreviousReleaseDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnGetPreviousReleaseDateTime`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePreviousTrip | LegalityTrip | |
| thePreviousDutyPeriod | LegalityDutyPeriod | |

## Lógica de negocio

```blaze
if(thePreviousDutyPeriod <> null) then {return thePreviousDutyPeriod.releaseDateTime;} else {// If the previous duty period is null then the duty period we're looking at is the first one in a trip// use the previous trip release time insteadreturn thePreviousTrip.endDateTime;}
```


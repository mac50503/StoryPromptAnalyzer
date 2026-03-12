# fcnDutyHasLabeledRedEyeLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegalityLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDutyHasLabeledRedEyeLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| legalityLegs | List<LegalityLeg> | |

## Lógica de negocio

```blaze
for each LegalityLeg in legalityLegs as an array of LegalityLeg do {if ((it.redEye <> unknown) and (it.redEye is equal to RedEyeType.SCHEDULED)) then {return it.}}return null.
```


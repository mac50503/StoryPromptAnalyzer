# fcnRedEyeFlightNumber

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnRedEyeFlightNumber`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| workingLegAfterRedEye | LegalityLeg | |
| workingLegAfterLabeledRedEye | LegalityLeg | |

## Lógica de negocio

```blaze
if(workingLegAfterRedEye <> null) then {return workingLegAfterRedEye.flightNumber.} else if(workingLegAfterLabeledRedEye <> null) then {return workingLegAfterLabeledRedEye.flightNumber} else {return 0.}
```


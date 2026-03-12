# fcnSetLodoQualification

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnSetLodoQualification`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| lodo | boolean | |
| theLeg | LegalityLeg | |

## Lógica de negocio

```blaze
theLeg.lodoQualified = lodo.
```


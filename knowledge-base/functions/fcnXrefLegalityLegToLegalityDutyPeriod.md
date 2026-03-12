# fcnXrefLegalityLegToLegalityDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnXrefLegalityLegToLegalityDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLeg | LegalityLeg | |
| theDutyPeriod | LegalityDutyPeriod | |

## Lógica de negocio

```blaze
if (theLeg <> null and theDutyPeriod <> null) thentheLeg.legalityDutyPeriod = theDutyPeriod.
```

## Llamado por

- [fcnXrefLegalityLegsDutiesAndTrips](fcnXrefLegalityLegsDutiesAndTrips.md)


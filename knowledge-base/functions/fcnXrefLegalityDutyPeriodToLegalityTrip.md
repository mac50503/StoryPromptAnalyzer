# fcnXrefLegalityDutyPeriodToLegalityTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\CommonLegality\Functions\fcnXrefLegalityDutyPeriodToLegalityTrip`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
if (theDutyPeriod <> null and theTrip <> null) thentheDutyPeriod.legalityTrip = theTrip.
```

## Llamado por

- [fcnXrefLegalityLegsDutiesAndTrips](fcnXrefLegalityLegsDutiesAndTrips.md)


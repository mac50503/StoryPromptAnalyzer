# fcnIsReserveBlock

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsReserveBlock`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null and aPayTrip.tripType =(ignoring case) "R") thenreturn true.elsereturn false.
```

## Llamado por

- [fcnCalculateConusAndOconusLimitsForTripset](fcnCalculateConusAndOconusLimitsForTripset.md)
- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)
- [fcnCalculateCrewMealPerdiem](fcnCalculateCrewMealPerdiem.md)
- [fcnCreateInflightTripSets](fcnCreateInflightTripSets.md)
- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)
- [fcnSetPreviousDayReserve](fcnSetPreviousDayReserve.md)
- [fcnShowTripPaySummary](fcnShowTripPaySummary.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```


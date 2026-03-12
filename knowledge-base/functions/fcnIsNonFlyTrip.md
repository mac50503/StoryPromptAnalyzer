# fcnIsNonFlyTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsNonFlyTrip`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null and aPayTrip.nonFlyCode <> null and aPayTrip.nonFlyCode.length() > 0) then return true.elsereturn false.
```

## Llamado por

- [fcnAssociateAirportStandbyWithOverlappingTrip](fcnAssociateAirportStandbyWithOverlappingTrip.md)
- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)
- [fcnCalculateExperiencePayBucket](fcnCalculateExperiencePayBucket.md)
- [fcnCreateInflightTripSets](fcnCreateInflightTripSets.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```


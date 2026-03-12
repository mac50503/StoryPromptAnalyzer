# fcnGetLastPayLegForTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetLastPayLegForTrip`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (thePayTrip.lastDutyPeriod <> null and     thePayTrip.lastDutyPeriod <> unknown and     thePayTrip.lastDutyPeriod.lastLeg <> null and     thePayTrip.lastDutyPeriod.lastLeg <> unknown) then return thePayTrip.lastDutyPeriod.lastLeg.else return null.
```


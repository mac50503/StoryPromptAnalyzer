# fcnSetPayTripTransientTerms

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetPayTripTransientTerms`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
// Find and save the first flying legaPayTrip.firstFlyingLeg = fcnGetFirstFlyingLeg(aPayTrip).aPayTrip.containsRON =fcnTripContainsRON(aPayTrip).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFirstFlyingLeg](fcnGetFirstFlyingLeg.md)
- [fcnTripContainsRON](fcnTripContainsRON.md)


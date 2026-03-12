# fcnSetTripRig

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetTripRig`

## Propósito
03/06/2015 Tim A. added function for DE6035

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aTripPay <> null and aTripPay.tripPayInflight <> null and aTripPay.tripPayInflight.ronRigTotal > 0.0) then{fcnShow("===>>> adding trip " aTripPay.tripName "'s trip RIG of " aTripPay.tripPayInflight.tripRIG  " with its ronRigTotal of " aTripPay.tripPayInflight.ronRigTotal " ...trip RIG now = " aTripPay.tripPayInflight.tripRIG + aTripPay.tripPayInflight.ronRigTotal).aTripPay.tripPayInflight.tripRIG += aTripPay.tripPayInflight.ronRigTotal.}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
03/06/2015 Tim A. added function for DE6035
7/7/2015 - Melissa S - Updated wording of logging
```


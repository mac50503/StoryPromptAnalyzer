# fcnAssignTripNoPremium

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnAssignTripNoPremium`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aTripPay <> null) thenaTripPay.payValueNoPremiumLegs = aTripPay.thisMonthPay.
```


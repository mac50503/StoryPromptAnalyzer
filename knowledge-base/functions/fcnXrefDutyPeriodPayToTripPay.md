# fcnXrefDutyPeriodPayToTripPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefDutyPeriodPayToTripPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aDutyPeriodPay <> null and aTripPay <> null) thenaDutyPeriodPay.tripPay = aTripPay.
```

## Llamado por

- [fcnCreateTripPay](fcnCreateTripPay.md)


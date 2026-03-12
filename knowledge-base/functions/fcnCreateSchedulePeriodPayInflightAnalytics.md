# fcnCreateSchedulePeriodPayInflightAnalytics

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCreateSchedulePeriodPayInflightAnalytics`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (aSchedulePeriodPay <> null and aSchedulePeriodPay.schedulePeriodPayInflight <> null) then{if (aSchedulePeriodPay.tripPayList <> null and aSchedulePeriodPay.tripPayList.size() > 0) thenfor each TripPay in aSchedulePeriodPay.tripPayList as an array of TripPay do fcnCreateTripPayInflightAnalytics(it).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCreateTripPay](fcnCreateTripPay.md)
- [fcnCreateTripPayInflightAnalytics](fcnCreateTripPayInflightAnalytics.md)


# fcnGetTripDistributedBasePay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetTripDistributedBasePay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| theTripSequenceNumber | integer | |

## Lógica de negocio

```blaze
if (theSchedulePeriodPay <> null and theSchedulePeriodPay <> unknown) thenfor each TripPay in theSchedulePeriodPay.tripPayList as an array of TripPay doif it.sequenceNumber = theTripSequenceNumber thenreturn it.distributedBasePay.return 0.0.
```


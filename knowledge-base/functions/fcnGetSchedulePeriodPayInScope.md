# fcnGetSchedulePeriodPayInScope

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSchedulePeriodPayInScope`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
if(theTripPay<>null)then{if(theTripPay.startSchedulePeriodPay<>null and theTripPay.startSchedulePeriodPay.tripPayList<>null and theTripPay.startSchedulePeriodPay.tripPayList.contains(theTripPay))then return theTripPay.startSchedulePeriodPay;else if(theTripPay.endSchedulePeriodPay<>null and theTripPay.endSchedulePeriodPay.tripPayList<>null and theTripPay.endSchedulePeriodPay.tripPayList.contains(theTripPay))then return theTripPay.endSchedulePeriodPay;}return null;
```

## Llamado por

- [fcnGetNonRONDutyPeriodBasePay](fcnGetNonRONDutyPeriodBasePay.md)
- [fcnGetNonRONpremium](fcnGetNonRONpremium.md)


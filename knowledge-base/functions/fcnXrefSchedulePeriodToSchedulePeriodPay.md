# fcnXrefSchedulePeriodToSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefSchedulePeriodToSchedulePeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriod | SchedulePeriod | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (aSchedulePeriod <> null and aSchedulePeriodPay <> null) then{aSchedulePeriod.schedulePeriodPay = aSchedulePeriodPay.aSchedulePeriodPay.schedulePeriod = aSchedulePeriod.aSchedulePeriodPay.schedulePeriodName = aSchedulePeriod.schedulePeriodName.aSchedulePeriodPay.schedulePeriodStart = aSchedulePeriod.schedulePeriodStart.aSchedulePeriodPay.schedulePeriodEnd = aSchedulePeriod.schedulePeriodEnd.}
```

## Llamado por

- [fcnCreateCrewPayResponse](fcnCreateCrewPayResponse.md)
- [fcnInitializePayTripSchedulePeriods](fcnInitializePayTripSchedulePeriods.md)


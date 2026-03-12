# fcnXrefLegPayToDutyPeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefLegPayToDutyPeriodPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegPay | LegPay | |
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
if (aLegPay <> null and aDutyPeriodPay <> null) thenaLegPay.dutyPeriodPay = aDutyPeriodPay.
```

## Llamado por

- [fcnCreateTripPay](fcnCreateTripPay.md)


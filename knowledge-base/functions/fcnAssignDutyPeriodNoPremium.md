# fcnAssignDutyPeriodNoPremium

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnAssignDutyPeriodNoPremium`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
if (aDutyPeriodPay <> null) thenaDutyPeriodPay.payValueNoPremiumLegs = aDutyPeriodPay.thisMonthPay.
```


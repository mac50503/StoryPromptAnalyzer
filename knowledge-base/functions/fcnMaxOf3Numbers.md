# fcnMaxOf3Numbers

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnMaxOf3Numbers`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| arg1 | real | |
| arg2 | real | |
| arg3 | real | |

## Lógica de negocio

```blaze
return math().max(arg1, math().max(arg2, arg3)).
```

## Llamado por

- [fcnCalculateReserveBlockCredit](fcnCalculateReserveBlockCredit.md)
- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnGetDutyPeriodPay](fcnGetDutyPeriodPay.md)
- [fcnMaxOf4Numbers](fcnMaxOf4Numbers.md)
- [fcnSetHighestRigAmounts](fcnSetHighestRigAmounts.md)


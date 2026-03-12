# fcnGetEffectiveReportDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetEffectiveReportDateTime`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if (theDutyPeriod.payDutyPeriodInflight = null) thenreturn theDutyPeriod.reportDateTime.elsereturn fcnGetFirstFlyingLegScheduledDepartureDateTime(theDutyPeriod).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFirstFlyingLeg](fcnGetFirstFlyingLeg.md)
- [fcnGetFirstFlyingLegScheduledDepartureDateTime](fcnGetFirstFlyingLegScheduledDepartureDateTime.md)

## Llamado por

- [fcnDetermineCarryOverTripCredits](fcnDetermineCarryOverTripCredits.md)
- [fcnDetermineDutyTripExcess](fcnDetermineDutyTripExcess.md)


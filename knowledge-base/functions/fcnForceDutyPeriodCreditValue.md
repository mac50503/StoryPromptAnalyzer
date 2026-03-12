# fcnForceDutyPeriodCreditValue

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnForceDutyPeriodCreditValue`

## Propósito
Ben Lang - US16557 - 7/23/2014

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |
| theDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
if (theDutyPeriod <> null and theDutyPeriodPay <> null) then {theDutyPeriodPay.payValue = theDutyPeriod.basePay.theDutyPeriodPay.creditType = "F".if (theDutyPeriod.payTrip.assignmentLabel = (ignoring case) ("J" or "U" or "V")) thentheDutyPeriodPay.premiumPayValue = theDutyPeriod.basePay.fcnShow("===>>> fcnForceDutyPeriodCreditValue ...payValue = " theDutyPeriodPay.payValue " ...passed in credit type = " theDutyPeriod.creditType " ...credit type = " theDutyPeriodPay.creditType).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
Ben Lang - US16557 - 7/23/2014
```


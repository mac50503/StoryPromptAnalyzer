# fcnDutyPeriodCreditsBypassRuleAction

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDutyPeriodCreditsBypassRuleAction`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
if (theDutyPeriodPay <> null) then {containsAllNonPaidLimos is a  boolean initially fcnDutyContainsAllNonPaidLimos(theDutyPeriodPay.payDutyPeriod).if (containsAllNonPaidLimos = false) then               theDutyPeriodPay.payValue = math().max(theDutyPeriodPay.dutyHourRatio,math().max(theDutyPeriodPay.basePay,theDutyPeriodPay.sumLegTotalCredits)).if (theDutyPeriodPay.payValue = theDutyPeriodPay.dutyHourRatio) then theDutyPeriodPay.creditType = "E".else theDutyPeriodPay.creditType = "P".fcnShow("===>>> fcnDutyPeriodCreditsBypassRuleAction ...setting duty period " theDutyPeriodPay.sequenceNumber "’s pay value to  " theDutyPeriodPay.payValue " and it's credit type to " theDutyPeriodPay.creditType " ... contains all non-paid LIMO's? = " containsAllNonPaidLimos).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDutyContainsAllNonPaidLimos](fcnDutyContainsAllNonPaidLimos.md)
- `fcnShow()`


# fcnDutyContainsAllNonPaidLimos

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDutyContainsAllNonPaidLimos`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayDutyPeriod <> null) then{if (aPayDutyPeriod.legList.size() > 0) then{retVal = true.for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do{if (fcnIsNonPaidLimoLeg(it) = false) thenretVal = false.}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsNonPaidLimoLeg](fcnIsNonPaidLimoLeg.md)

## Llamado por

- [fcnDutyPeriodCreditsBypassRuleAction](fcnDutyPeriodCreditsBypassRuleAction.md)
- [fcnSetCombinedDutyDurationStart](fcnSetCombinedDutyDurationStart.md)


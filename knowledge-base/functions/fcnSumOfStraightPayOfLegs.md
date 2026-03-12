# fcnSumOfStraightPayOfLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnSumOfStraightPayOfLegs`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
fcnShow("...Entering function fcnSumOfStraightPayOfLegs...").retVal is a real initially 0.0.if (aDutyPeriodPay <> null and aDutyPeriodPay.legPayList.size() > 0) then{for each LegPay in aDutyPeriodPay.legPayList as an array of LegPay do{retVal += it.payValueNoPremium.//fcnShow("...adding LegPay: " it.sequenceNumber "'s payValueNoPremium of " it.payValueNoPremium " to sum of legs... value now = " retVal).}}fcnShow("...Exiting function fcnSumOfStraightPayOfLegs...returning: " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`


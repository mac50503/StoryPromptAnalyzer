# fcnGetSchedulePeriodPayForLegPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSchedulePeriodPayForLegPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegPay | LegPay | |

## Lógica de negocio

```blaze
retVal is some SchedulePeriodPay initially null.aSchedulePeriodPay is some SchedulePeriodPay initially null.if (aLegPay <> null) then{retVal =  fcnGetSchedulePeriodPayForDutyPeriodPay(aLegPay.dutyPeriodPay).}if (retVal = null) thenfcnShow("===>>> EXITING function fcnGetSchedulePeriodPayForLegPay with leg = " fcnGetLegIdentificationString(aLegPay.payLeg) " ...SP Pay = null...").elsefcnShow("===>>> EXITING function fcnGetSchedulePeriodPayForLegPay with leg = " fcnGetLegIdentificationString(aLegPay.payLeg) " ...SP Pay = " retVal.schedulePeriodName).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetLegIdentificationString](fcnGetLegIdentificationString.md)
- [fcnGetSchedulePeriodPayForDutyPeriodPay](fcnGetSchedulePeriodPayForDutyPeriodPay.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateTripCpCodePay](fcnCalculateTripCpCodePay.md)
- [fcnIsDPPayEndsInNextSPPay](fcnIsDPPayEndsInNextSPPay.md)


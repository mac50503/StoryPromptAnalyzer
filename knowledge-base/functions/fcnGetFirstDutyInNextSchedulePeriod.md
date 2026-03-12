# fcnGetFirstDutyInNextSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetFirstDutyInNextSchedulePeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
retVal is some PayDutyPeriod initially null.if (aPayTrip <> null and aPayTrip.tripPay <> null and aPayTrip.dutyPeriodList.size() > 1) then{for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{if (retVal = null and aPayTrip.tripPay.startSchedulePeriodPay <> fcnGetSchedulePeriodPayForDutyPeriodPay(it.dutyPeriodPay)) thenretVal = it.}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSchedulePeriodPayForDutyPeriodPay](fcnGetSchedulePeriodPayForDutyPeriodPay.md)

## Llamado por

- [fcnIsDPPayEndsInNextSPPay](fcnIsDPPayEndsInNextSPPay.md)


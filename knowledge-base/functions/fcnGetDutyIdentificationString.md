# fcnGetDutyIdentificationString

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetDutyIdentificationString`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
retVal is a string initially "".if (aDutyPeriodPay <> null and aDutyPeriodPay.payDutyPeriod <> null and aDutyPeriodPay.tripPay <> null) then{position is an integer initially aDutyPeriodPay.tripPay.dutyPeriodPayList.indexOf(aDutyPeriodPay).dpOrder is a string initially "first ".select positioncase 0 : dpOrder = "1st ".case 1 : dpOrder = "2nd ".case 2 : dpOrder = "3rd ".case 3 : dpOrder = "4th ".case 4 : dpOrder = "5th ".case 5 : dpOrder = "6th ".case 6 : dpOrder = "7th ".case 7 : dpOrder = "8th ".otherwise : dpOrder = "??? ".aPayDutyPeriod is some PayDutyPeriod initially aDutyPeriodPay.payDutyPeriod.retVal = dpOrder "duty period " aPayDutyPeriod.beginLocation "-" aPayDutyPeriod.endLocation " from trip ".if (aPayDutyPeriod.payTrip <> null) thenretVal = retVal "" aPayDutyPeriod.payTrip.tripNameAndDate.retVal = retVal " beginning on  " fcnGetShortDateTimeString(aPayDutyPeriod.reportDateTime).}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetShortDateTimeString](fcnGetShortDateTimeString.md)

## Llamado por

- [fcnDistributePerdiemPayToDutyPeriods](fcnDistributePerdiemPayToDutyPeriods.md)
- [fcnDistributeRemainingReserveGuarantee](fcnDistributeRemainingReserveGuarantee.md)


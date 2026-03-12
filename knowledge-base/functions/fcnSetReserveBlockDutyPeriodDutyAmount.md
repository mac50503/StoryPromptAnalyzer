# fcnSetReserveBlockDutyPeriodDutyAmount

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetReserveBlockDutyPeriodDutyAmount`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aReserveBlock | PayTrip | |

## Lógica de negocio

```blaze
if ( aReserveBlock <> null) then{for each PayDutyPeriod in aReserveBlock.dutyPeriodList as an array of PayDutyPeriod do{it.dutyPeriodPay.dutyAmount = DateTimeUtilities.getHoursAndMinutesString(fcnGetTimeDiffInMinutes(it.reportDateTime, it.releaseDateTime)).it.payDutyPeriodInflight.combinedDurationBeginDateTime = it.reportDateTime.}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)


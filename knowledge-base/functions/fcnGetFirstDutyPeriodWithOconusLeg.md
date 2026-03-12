# fcnGetFirstDutyPeriodWithOconusLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetFirstDutyPeriodWithOconusLeg`

## Propósito
Ben Lang - US8942 - 03/10/14 - The fcnGetFirstDutyPeriodWithOconusLeg returns the first PayDutyPeriod that contains a Oconus Leg

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
aPayDutyPeriod is some PayDutyPeriod initially null.if (aPayTrip.dutyPeriodList is not equal to null and aPayTrip.dutyPeriodList.size() > 0) then {for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{aPayDutyPeriod = it.if (it.legList is not equal to null and it.legList.size() > 0) then {for each PayLeg in it.legList as an array of PayLeg do {departureStation is some Station initially aGlobalDataCache.stationMap.get(it.departureLocation).arrivalStation is some Station initially aGlobalDataCache.stationMap.get(it.arrivalLocation).if ((departureStation <> null and departureStation.isContinentalUS = false) or (arrivalStation<>null and arrivalStation.isContinentalUS = false)) thenreturn aPayDutyPeriod.}}}}return null.
```

## Llamado por

- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)

## Historial de cambios

```
Ben Lang - US8942 - 03/10/14 - The fcnGetFirstDutyPeriodWithOconusLeg returns the first PayDutyPeriod that contains a Oconus Leg
```


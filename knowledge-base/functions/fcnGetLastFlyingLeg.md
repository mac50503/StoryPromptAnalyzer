# fcnGetLastFlyingLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLastFlyingLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
dpCounter is an integer initially 0;legCounter is an integer initially 0;aPayDuty is some PayDutyPeriod initially null;if(aPayTrip.dutyPeriodList<>null and aPayTrip.dutyPeriodList.size()>0)then{dpCounter = aPayTrip.dutyPeriodList.size()-1;while(dpCounter >= 0) do{aPayDuty = aPayTrip.dutyPeriodList.get(dpCounter);if(aPayDuty.legList<>null and aPayDuty.legList.size()>0)then{legCounter = aPayDuty.legList.size()-1;while(legCounter >=0) do{if(aPayDuty.legList.get(legCounter).legWorkCodeList<>null andaPayDuty.legList.get(legCounter).legWorkCodeList.contains("RS")=false)then return aPayDuty.legList.get(legCounter).legCounter-=1;}}dpCounter-=1;}}return null;
```

## Llamado por

- [fcnCalculateCrewMealPerdiumInternational](fcnCalculateCrewMealPerdiumInternational.md)
- [fcnSetTripNonDeadheadBeginEndTime](fcnSetTripNonDeadheadBeginEndTime.md)


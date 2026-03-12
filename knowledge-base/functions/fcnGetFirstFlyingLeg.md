# fcnGetFirstFlyingLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetFirstFlyingLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
dpCounter is an integer initially 0;legCounter is an integer initially 0;aPayDuty is some PayDutyPeriod initially null;if(aPayTrip.dutyPeriodList<>null and aPayTrip.dutyPeriodList.size()>0)then{while(dpCounter < aPayTrip.dutyPeriodList.size()) do{aPayDuty = aPayTrip.dutyPeriodList.get(dpCounter);legCounter = 0;if(aPayDuty.legList<>null and aPayDuty.legList.size()>0)then{while(legCounter < aPayDuty.legList.size()) do{if(aPayDuty.legList.get(legCounter).legWorkCodeList<>null andaPayDuty.legList.get(legCounter).legWorkCodeList.contains("RS")=false)then return aPayDuty.legList.get(legCounter).legCounter+=1;}}dpCounter+=1;}}return null;
```

## Llamado por

- [fcnAssociateInflightPayDutyPeriodsToRaps](fcnAssociateInflightPayDutyPeriodsToRaps.md)
- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)
- [fcnCalculateCrewMealPerdiumInternational](fcnCalculateCrewMealPerdiumInternational.md)
- [fcnDistributeRedEyePremiumToPayBucket](fcnDistributeRedEyePremiumToPayBucket.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay](fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay.md)
- [fcnGetEffectiveReportDateTime](fcnGetEffectiveReportDateTime.md)
- [fcnSetPayTripTransientTerms](fcnSetPayTripTransientTerms.md)


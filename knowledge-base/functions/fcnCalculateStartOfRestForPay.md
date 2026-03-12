# fcnCalculateStartOfRestForPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateStartOfRestForPay`

## Propósito
10/13/2015 - DE7572 - Changed to use fcnDutyContainsAllLimosOfZeroDuration instead of fcnDutyContainsAllNonPaidLimos.  Per the customers, if a duty period with all LIMOS has any duration, it should be considered.  Only skip if there is no duration

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
retVal is some DateTime initially null.prevDuty is some PayDutyPeriod initially null.if (aPayTrip <> null and aPayTrip.dutyPeriodList.size() > 0 and aPayDutyPeriod <> null) then{retVal = aPayDutyPeriod.reportDateTime.minusHours(10).foundCandidateDutyPeriod is a boolean initially false.restEnd is some DateTime initially aPayDutyPeriod.reportDateTime.prevDuty = fcnGetPreviousPayDutyPeriod(aPayTrip.dutyPeriodList, aPayTrip.dutyPeriodList.indexOf(aPayDutyPeriod)).if (prevDuty = null) then{retVal = restEnd.minusHours(10).}else{while foundCandidateDutyPeriod = false do{if (prevDuty <> null and fcnDutyContainsAllLimosOfZeroDuration(prevDuty) = true) thenprevDuty = fcnGetPreviousPayDutyPeriod(aPayTrip.dutyPeriodList, aPayTrip.dutyPeriodList.indexOf(prevDuty)).elsefoundCandidateDutyPeriod = true. }if (prevDuty = null) thenretVal = restEnd.minusHours(10).else{legDuration is an integer initially 0.isLimo is a boolean initially false.aPayLeg is some PayLeg initially null.for each PayLeg in prevDuty.legList as an array of PayLeg do{aPayLeg = it.isLimo = aPayLeg.limoFlag.legDuration = fcnGetTimeDiffInMinutes(aPayLeg.determineBestDepartureDateTimeNoEstimated(), aPayLeg.determineBestArrivalDateTimeNoEstimated()).if (isLimo = false or legDuration > 0) thenretVal = aPayLeg.determineBestArrivalDateTimeNoEstimated().}}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDutyContainsAllLimosOfZeroDuration](fcnDutyContainsAllLimosOfZeroDuration.md)
- [fcnGetPreviousPayDutyPeriod](fcnGetPreviousPayDutyPeriod.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Llamado por

- [fcnSetPayDutyPeriodTransientTerms](fcnSetPayDutyPeriodTransientTerms.md)

## Historial de cambios

```
10/13/2015 - DE7572 - Changed to use fcnDutyContainsAllLimosOfZeroDuration instead of fcnDutyContainsAllNonPaidLimos.  Per the customers, if a duty period with all LIMOS has any duration, it should be considered.  Only skip if there is no duration
```


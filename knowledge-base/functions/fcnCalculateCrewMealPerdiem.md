# fcnCalculateCrewMealPerdiem

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCalculateCrewMealPerdiem`

## Propósito
5/06/2024 - Namratha- APIC-1102-Created Main Function for Crew meal Perdiem

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aTripPay | TripPay | |
| aGlobalDataCache | GlobalDataCache | |
| aSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
qualifiedLegSequenceNumberList is some List<String> initially an ArrayList.aCrewPerdiemMeal is some CrewPerDiemMeal initially null.aCrewPerdiemMeal = fcnGetMealsPerDiemDetailsFromConfigCollection(aPayTrip.beginDateTime).if(aCrewPerdiemMeal <> null and aCrewPerdiemMeal <> unknown and fcnIsDataValidInCrewMealPerdiemValue(aCrewPerdiemMeal)) then {fcnShow("===>>> ENTERING function fcnCalculateCrewMealPerdium with trip " aPayTrip.tripNameAndDate).fcnShow("===>>> aCrewPerdiemMeal.perDiemRate in  fcnCalculateCrewMealPerdium with trip " aCrewPerdiemMeal.perDiemRate).dpCounter is an integer initially 0;mealsPayCountAtTrip is a real initially 0.crewMealPerdiemRate is a real initially aCrewPerdiemMeal.perDiemRate.if(aPayTrip.dutyPeriodList<>null and aPayTrip.dutyPeriodList.size()>0 and fcnIsReserveBlock(aPayTrip) is false)then{dpCounter = aPayTrip.dutyPeriodList.size()-1.aCurrentPayDuty is some PayDutyPeriod initially null.aPreviousPayDuty is some PayDutyPeriod initially null.mealsPayCountInternational is a real initially 0.mealsPayDomesticCountAtDP is a real initially 0.mealsPayInternationalCountAtDP is a real initially 0.while(dpCounter >= 0) do{            mealsPaytDomesticCountAtLeg is a real initially 0.mealsPayCountInternationalAtLeg is a real initially 0.aCurrentPayDuty = aPayTrip.dutyPeriodList.get(dpCounter);if(dpCounter >= 1) then{aPreviousPayDuty = aPayTrip.dutyPeriodList.get(dpCounter-1);}if(aCurrentPayDuty <> null and aCurrentPayDuty.legList<>null and aCurrentPayDuty.legList.size()>0 and aPreviousPayDuty<>null and aPreviousPayDuty.legList.size()>0 and aPreviousPayDuty.legList.size()>0)then{mealsPayCountInternationalAtLeg = fcnCalculateCrewMealPerdiumInternational(aCurrentPayDuty,aPreviousPayDuty,aGlobalDataCache,qualifiedLegSequenceNumberList,aCrewPerdiemMeal,aSchedulePeriodPay,reportFilterStart,reportFilterEnd).} //Calling function to  calulate Domestic Legs mealsPaytDomesticCountAtLeg = fcnCalculateCrewMealPerdiumDomesticLegs(aCurrentPayDuty,aGlobalDataCache,qualifiedLegSequenceNumberList,aCrewPerdiemMeal,aSchedulePeriodPay,reportFilterStart,reportFilterEnd).dpCounter-=1.mealsPayDomesticCountAtDP += mealsPaytDomesticCountAtLeg.mealsPayInternationalCountAtDP += mealsPayCountInternationalAtLeg.}                                                                         //Contains Value for only legs in PayrollReportDate Filter RangemealsPayCountAtTrip = mealsPayDomesticCountAtDP+mealsPayInternationalCountAtDP.fcnShow("===>>> Count of Eligible Domestic Leg for Crew Mel Perdiem--> " mealsPayDomesticCountAtDP).fcnShow("===>>> Count of Eligible Internationa Leg for Crew Mel Perdiem--> " mealsPayInternationalCountAtDP).}//Getting Sequence Number of Legs to set the IndicatorfcnSetHasCrewMealPerdiemInLeg(qualifiedLegSequenceNumberList,aTripPay).//The Trip Pay value will consider all the  qualifying legs in the given tripif(qualifiedLegSequenceNumberList <> null and qualifiedLegSequenceNumberList is known) then {aTripPay.crewMealPerDiem = (qualifiedLegSequenceNumberList.size() )* crewMealPerdiemRate. }cmpBucketValueForTrip is a real initially 0.cmpBucketValueForTrip = mealsPayCountAtTrip * crewMealPerdiemRate.//Set Bucket Values-- Bucket Value will consider only legs tha fall in between PayRoll Report FilterfcnSetPayBucketValuesForCrewMealPerdiem(aSchedulePeriodPay,aCrewPerdiemMeal.payRateCode,cmpBucketValueForTrip,mealsPayCountAtTrip,aCrewPerdiemMeal.perDiemRate).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCalculateCrewMealPerdiumDomesticLegs](fcnCalculateCrewMealPerdiumDomesticLegs.md)
- [fcnCalculateCrewMealPerdiumInternational](fcnCalculateCrewMealPerdiumInternational.md)
- [fcnGetMealsPerDiemDetailsFromConfigCollection](fcnGetMealsPerDiemDetailsFromConfigCollection.md)
- [fcnIsDataValidInCrewMealPerdiemValue](fcnIsDataValidInCrewMealPerdiemValue.md)
- [fcnIsReserveBlock](fcnIsReserveBlock.md)
- [fcnSetHasCrewMealPerdiemInLeg](fcnSetHasCrewMealPerdiemInLeg.md)
- [fcnSetPayBucketValuesForCrewMealPerdiem](fcnSetPayBucketValuesForCrewMealPerdiem.md)
- `fcnShow()`

## Historial de cambios

```
5/06/2024 - Namratha- APIC-1102-Created Main Function for Crew meal Perdiem
```


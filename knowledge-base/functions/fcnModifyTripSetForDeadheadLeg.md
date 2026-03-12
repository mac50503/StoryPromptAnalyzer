# fcnModifyTripSetForDeadheadLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnModifyTripSetForDeadheadLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayCrewMemberLine | PayCrewMemberLine | |

## Lógica de negocio

```blaze
aTripSet is some TripSet initially null;aPayTrip is some PayTrip initially null;aPayDutyPeriod is some PayDutyPeriod initially null;aPayLeg is some PayLeg initially null;nonDeadLegFoundAtStart is a boolean initially false;nonDeadLegFoundAtEnd is a boolean initially false;dpCounter is an integer initially 0;legCounter is an integer initially 0;if (aPayCrewMemberLine.tripSetList <> null and aPayCrewMemberLine.tripSetList.size() > 0) then{for each TripSet in aPayCrewMemberLine.tripSetList as an array of TripSet such that(nonDeadLegFoundAtStart=false or nonDeadLegFoundAtEnd = false) do{aTripSet = it.if (aTripSet.payTripList <> null and aTripSet.payTripList.size() > 0) then{if (aTripSet.payTripList.get(0).firstDutyPeriod<>null and     aTripSet.payTripList.get(0).firstDutyPeriod.legList<>null and aTripSet.payTripList.get(0).firstDutyPeriod.legList.size()>0 and    aTripSet.payTripList.get(0).firstDutyPeriod.legList.get(0).legWorkCodeList.contains("RS") and nonDeadLegFoundAtStart=false) then{aPayTrip=aTripSet.payTripList.get(0).dpCounter = 0.if (aPayTrip.dutyPeriodList<> null and aPayTrip.dutyPeriodList.size() > 0) then{while (dpCounter<aPayTrip.dutyPeriodList.size() and nonDeadLegFoundAtStart=false) do{aPayDutyPeriod = aPayTrip.dutyPeriodList.get(dpCounter).legCounter=0.if (aPayDutyPeriod.legList<> null and aPayDutyPeriod.legList.size() > 0) then{while (legCounter<aPayDutyPeriod.legList.size()and nonDeadLegFoundAtStart = false) do{aPayLeg = aPayDutyPeriod.legList.get(legCounter).if (nonDeadLegFoundAtStart=false and aPayLeg.legWorkCodeList.contains("RS") = false) then{aTripSet.startDateTime = aPayLeg.determineBestDepartureDateTimeNoEstimated().minusMinutes(30).nonDeadLegFoundAtStart=true.}legCounter+=1.}  //end of PayLeg loop}dpCounter+=1.}  //end of duty period loop}}//Modifying the TripSet's end date timeif (aTripSet.payTripList.get(aTripSet.payTripList.size()-1).lastDutyPeriod<>null and aTripSet.payTripList.get(aTripSet.payTripList.size()-1).lastDutyPeriod.lastLeg<>null and     aTripSet.payTripList.get(aTripSet.payTripList.size()-1).lastDutyPeriod.lastLeg.legWorkCodeList.contains("RS") and nonDeadLegFoundAtEnd = false) then{aPayTrip = aTripSet.payTripList.get(aTripSet.payTripList.size()-1).dpCounter = aPayTrip.dutyPeriodList.size()-1.if (aPayTrip.dutyPeriodList<> null and aPayTrip.dutyPeriodList.size() > 0) then{while (dpCounter>=0 and nonDeadLegFoundAtEnd = false) do{aPayDutyPeriod = aPayTrip.dutyPeriodList.get(dpCounter).legCounter=aPayDutyPeriod.legList.size()-1.if (aPayDutyPeriod.legList<> null and aPayDutyPeriod.legList.size() > 0) then{while (legCounter>=0 and nonDeadLegFoundAtEnd = false) do{aPayLeg = aPayDutyPeriod.legList.get(legCounter).if (nonDeadLegFoundAtEnd=false and aPayLeg.legWorkCodeList.contains("RS") = false) then{aTripSet.startDateTime = aPayLeg.determineBestArrivalDateTimeNoEstimated().plusMinutes(30).nonDeadLegFoundAtEnd=true.}legCounter -= 1.}  //end of PayLeg loop}dpCounter-=1.}  //end of duty period loop}}}}//end of TripSet loop}
```


# fcnSetHasCrewMealPerdiemInLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnSetHasCrewMealPerdiemInLeg`

## Propósito
5/06/2024 - Namratha- APIC-1102- FunctionTo Set the CrewMealPerdim Indicator in the ResponsePayload

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLegSequenceNumber | List<String> | |
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
seqCounter is an integer initially 0.if (aTripPay is not equal to null andaTripPay.dutyPeriodPayList is not equal to null andaTripPay.dutyPeriodPayList.size() > 0) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do {if (it.legPayList is not equal to null and it.legPayList.size() > 0) then {for each LegPay in it.legPayList as an array of LegPay do {if(aPayLegSequenceNumber <> null and aPayLegSequenceNumber is known) then {seqCounter = aPayLegSequenceNumber.size().}while(seqCounter >0) do{if (it.sequenceNumber as a string is equal to aPayLegSequenceNumber.get(seqCounter-1)) then {it.hasCrewMealPerDiem = true.}seqCounter-=1;} }}}}
```

## Llamado por

- [fcnCalculateCrewMealPerdiem](fcnCalculateCrewMealPerdiem.md)

## Historial de cambios

```
5/06/2024 - Namratha- APIC-1102- FunctionTo Set the CrewMealPerdim Indicator in the ResponsePayload
```


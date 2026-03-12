# fcnCalculateCrewMealPerdiumInternational

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCalculateCrewMealPerdiumInternational`

## Propósito
5/06/2024 - Namratha- APIC-1102- Function for Crew meal Perdiem International Legs

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aCurrentPayDuty | PayDutyPeriod | |
| aPreviousPayDuty | PayDutyPeriod | |
| aGlobalDataCache | GlobalDataCache | |
| qualifiedLegSequenceNumberList | List<String> | |
| aCrewPerdiemMeal | CrewPerDiemMeal | |
| aSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
mealsPayCountInternationalAtLeg is a real initially 0.aPayLegCurrentDP is some PayLeg initially null.aPayLegPreviousDP is some PayLeg initially null.aPayLegCurrentDP  =   fcnGetFirstFlyingLegOfDutyPeriod(aCurrentPayDuty).aPayLegPreviousDP = fcnGetLastFlyingLegOfDutyPeriod(aPreviousPayDuty).if(aPayLegPreviousDP <> null and aPayLegCurrentDP <> null) then {//Check for International Leg OvernightmealsPayCountInternationalAtLeg=fcnCalculateCrewMealPerdiumInternationalLegs(aPayLegCurrentDP,aPayLegPreviousDP,aGlobalDataCache,qualifiedLegSequenceNumberList,aCrewPerdiemMeal,aSchedulePeriodPay,reportFilterStart,reportFilterEnd).}return mealsPayCountInternationalAtLeg
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCalculateCrewMealPerdiumInternationalLegs](fcnCalculateCrewMealPerdiumInternationalLegs.md)
- [fcnGetFirstFlyingLeg](fcnGetFirstFlyingLeg.md)
- [fcnGetFirstFlyingLegOfDutyPeriod](fcnGetFirstFlyingLegOfDutyPeriod.md)
- [fcnGetLastFlyingLeg](fcnGetLastFlyingLeg.md)
- [fcnGetLastFlyingLegOfDutyPeriod](fcnGetLastFlyingLegOfDutyPeriod.md)

## Llamado por

- [fcnCalculateCrewMealPerdiem](fcnCalculateCrewMealPerdiem.md)
- [fcnCalculateCrewMealPerdiumInternationalLegs](fcnCalculateCrewMealPerdiumInternationalLegs.md)

## Historial de cambios

```
5/06/2024 - Namratha- APIC-1102- Function for Crew meal Perdiem International Legs
```


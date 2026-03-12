# fcnSetNonRonLegPremium

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetNonRonLegPremium`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aTripPay <> null and     aTripPay.tripPayInflight <> null and     aTripPay.dutyPeriodPayList.size() > 0 and    aTripPay.tripPayInflight.rigsGreaterThanPremium = false) then {aDutyPeriodPay is some DutyPeriodPay initially null.aLegPay is some LegPay initially null.valueToAdd is a real initially 0.0.for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{if (it.payDutyPeriod.dutyType <> "RON" and    it.rigsGreaterThanPremium = false) then {aDutyPeriodPay = it.if (aDutyPeriodPay.legPayList.size() >0) then{for each LegPay in it.legPayList as an array of LegPay do{valueToAdd  = 0.0.aLegPay = it.if (aLegPay.basePay < aLegPay.payValue) then{valueToAdd  = aLegPay.payValue - aLegPay.basePay.valueToAdd  = fcnRoundUpAt2DecimalPlaces(valueToAdd).aTripPay.tripPayInflight.nonRONlegPremium += valueToAdd.}valueToAdd = 0.00.if (aTripPay.assignmentLabel = ("J" or "U" or "V") or (aTripPay.creditType = "F" and aTripPay.assignmentLabel = "S")) then{valueToAdd = aLegPay.payValue - (aLegPay.basePay * 1.5).valueToAdd = fcnRoundUpAt2DecimalPlaces(valueToAdd).aTripPay.tripPayInflight.nonRONlegPremiumOverJV += valueToAdd.}else if(aTripPay.assignmentLabel = "E") then{valueToAdd = aLegPay.payValue - (aLegPay.basePay * 2.0).valueToAdd = fcnRoundUpAt2DecimalPlaces(valueToAdd).aTripPay.tripPayInflight.nonRONlegPremiumOverJV += valueToAdd.}}}}}aTripPay.tripPayInflight.nonRONlegPremium = fcnRoundUpAt2DecimalPlaces(aTripPay.tripPayInflight.nonRONlegPremium).aTripPay.tripPayInflight.nonRONlegPremiumOverJV = fcnRoundUpAt2DecimalPlaces(aTripPay.tripPayInflight.nonRONlegPremiumOverJV).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)


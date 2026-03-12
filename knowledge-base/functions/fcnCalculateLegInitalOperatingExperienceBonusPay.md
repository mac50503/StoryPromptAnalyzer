# fcnCalculateLegInitalOperatingExperienceBonusPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateLegInitalOperatingExperienceBonusPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegPay | LegPay | |

## Lógica de negocio

```blaze
if (aLegPay <> null and aLegPay.legPayInflightAnalytics <> null and aLegPay.payLeg <> null and     aLegPay.payLeg.payDutyPeriod <> null and aLegPay.payLeg.payDutyPeriod.payTrip <> null and    aLegPay.payLeg.payDutyPeriod.payTrip.assignmentLabel <>  (ignoring case) "I" and    aLegPay.payLeg.legWorkCodeList <> null and aLegPay.payLeg.legWorkCodeList.contains("IP") and    aLegPay.payLeg.nonFlyCode <> ("DH" and "DM" and "NM" and "NP" and "DP" and "OM") and     aLegPay.payLeg.limoFlag = false) then{aLegPay.legPayInflightAnalytics.legBonusPayMap.put("operating experience", 2.0).}
```


# fcnDutyContainsAllDeadheadLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDutyContainsAllDeadheadLegs`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayDutyPeriod <> null and aPayDutyPeriod.legList.size() >0) then{retVal = true.for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do{if (retVal = true and (it.deadHeadCode = null or                                  (it.deadHeadCode.contains("DH") = false and      it.deadHeadCode.contains("DM") = false and      it.deadHeadCode.contains("NM") = false and      it.deadHeadCode.contains("DP") = false and      it.deadHeadCode.contains("NP") = false))) thenretVal = false. }}return retVal.
```


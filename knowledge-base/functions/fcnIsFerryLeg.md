# fcnIsFerryLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnIsFerryLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayLeg <> null and     aPayLeg.payDutyPeriod <> null and     aPayLeg.payDutyPeriod.payTrip <> null and     aPayLeg.payDutyPeriod.payTrip.tripClass = ("C" or "L") and     (aPayLeg.legWorkCodeList = null or        (aPayLeg.legWorkCodeList <> null and aPayLeg.legWorkCodeList.contains("CT") = false))) then{retVal = true.}return retVal.
```


# fcnRestorePremiumLegWorkCodes

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnRestorePremiumLegWorkCodes`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
if (aPayLeg <> null and     aPayLeg.legWorkCodeList <> null and     aPayLeg.tempLegWorkCodeList <> null and    aPayLeg.tempLegWorkCodeList.size() > 0) then{fcnShowLegWorkCodeList(aPayLeg).if (aPayLeg.legWorkCodeList <> null and aPayLeg.tempLegWorkCodeList.size() > 0) then{aPayLeg.legWorkCodeList.clear().for each string in aPayLeg.tempLegWorkCodeList as an array of string do{aPayLeg.addLegWorkCode(it).} }fcnShow("RESTORED LEGWORKCODES..."). fcnShowLegWorkCodeList(aPayLeg).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`
- [fcnShowLegWorkCodeList](fcnShowLegWorkCodeList.md)


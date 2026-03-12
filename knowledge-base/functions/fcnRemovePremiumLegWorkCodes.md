# fcnRemovePremiumLegWorkCodes

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnRemovePremiumLegWorkCodes`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
if (aPayLeg <> null and aPayLeg.legWorkCodeList <> null and aPayLeg.legWorkCodeList.size() > 0) then{/// FIRST MAKE A COPY OF THE ORIGINAL...for each string in aPayLeg.legWorkCodeList as an array of string do{aPayLeg.tempLegWorkCodeList.add(it).}.fcnShow("ORIGINAL LEGWORKCODES..."). fcnShowLegWorkCodeList(aPayLeg).aPayLeg.legWorkCodeList.remove("PP").aPayLeg.legWorkCodeList.remove("VR").aPayLeg.legWorkCodeList.remove("CT").aPayLeg.legWorkCodeList.remove("DT").fcnShow("MODIFIED LEGWORKCODES..."). fcnShowLegWorkCodeList(aPayLeg).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`
- [fcnShowLegWorkCodeList](fcnShowLegWorkCodeList.md)


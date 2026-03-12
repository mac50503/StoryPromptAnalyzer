# fcnGetHomeStudyPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetHomeStudyPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
retVal is a real initially 0.00.if (aPayTrip <> null and    aPayTrip.nonFlyCode = "HS" and     aGlobalDataCache <> null and    aGlobalDataCache.homeStudyPayList <> null and    aGlobalDataCache.homeStudyPayList.size() > 0) then{aHomeStudyPay is some HomeStudyPay initially null.for each HomeStudyPay in aGlobalDataCache.homeStudyPayList as an array of HomeStudyPay do{aHomeStudyPay = it.if (retVal = 0.00 and aHomeStudyPay.year = aPayTrip.beginDateTime.year) thenreturn aHomeStudyPay.tfp.}}return retVal.
```


# fcnDutyContainsAllLimoLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDutyContainsAllLimoLegs`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayDutyPeriod <> null) then{if (aPayDutyPeriod.legList.size() > 0) then{retVal = true.for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do{isLimo is a boolean initially it.limoFlag.if (isLimo = false) thenretVal = false.}}//fcnShow("===>>> returning " retVal " from fcnDutyContainsAllLimos with DP " aPayDutyPeriod.sequenceNumber " from trip " aPayDutyPeriod.payTrip.tripName).}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnGetPreviousLegBestArrivalForRONTAFB](fcnGetPreviousLegBestArrivalForRONTAFB.md)


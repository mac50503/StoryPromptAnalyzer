# fcnGetTripLegList

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<PayLeg>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripLegList`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
retVal is some ArrayList initially a ArrayList.if (aPayTrip <> null and aPayTrip.dutyPeriodList.size() > 0) then{retVal = an ArrayList.for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{for each PayLeg in it.legList as an array of PayLeg doretVal.add(it).}}fcnShow("===>>> legList for trip " aPayTrip.tripNameAndDate " contains " retVal.size() " legs...").return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnGetEndDateTimeForRONTHR](fcnGetEndDateTimeForRONTHR.md)
- [fcnGetPreviousLegBestArrivalForRONTAFB](fcnGetPreviousLegBestArrivalForRONTAFB.md)


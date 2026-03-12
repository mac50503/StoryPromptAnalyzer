# fcnGetPayTripListForSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<PayTrip>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayTripListForSchedulePeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| candidateList | List<PayTrip> | |
| schedulePeriod | SchedulePeriod | |

## Lógica de negocio

```blaze
retVal is some List<PayTrip> initially null.if (schedulePeriod is not equal to null and    candidateList is not equal to null and     candidateList.size() > 0) then{for each PayTrip in candidateList as an array of PayTrip do{if (it.startsInSchedulePeriod is equal to (ignoring case) schedulePeriod.schedulePeriodName or     it.endsInSchedulePeriod is equal to (ignoring case) schedulePeriod.schedulePeriodName) then{if retVal is equal to null thenretVal = an ArrayList.if retVal.contains(it) is equal to false thenretVal.add(it).}}}return retVal.
```


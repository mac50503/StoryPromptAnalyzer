# fcnInitializePayTripListSchedulePeriods

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnInitializePayTripListSchedulePeriods`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTripList | List<PayTrip> | |
| theSchedulPeriodList | List<SchedulePeriod> | |

## Lógica de negocio

```blaze
if (thePayTripList is not equal to null and     thePayTripList is not equal to null and    thePayTripList.size() > 0) then{for each PayTrip in thePayTripList as an array of PayTrip do{fcnInitializePayTripSchedulePeriods(it, theSchedulPeriodList).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnInitializePayTripSchedulePeriods](fcnInitializePayTripSchedulePeriods.md)


# fcnXrefPayMileageToMileagePay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefPayMileageToMileagePay`

## Propósito
02/28/2014 Tim Albright - US16955

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayMileage | PayMileage | |
| aMileagePay | MileagePay | |

## Lógica de negocio

```blaze
if (aPayMileage <> null and aMileagePay <> null) then{aMileagePay.departureLocation = aPayMileage.departureLocation.aMileagePay.arrivalLocation = aPayMileage.arrivalLocation.aMileagePay.mileage = aPayMileage.mileage.aMileagePay.payMileage = aPayMileage.aPayMileage.mileagePay = aMileagePay.}
```

## Historial de cambios

```
02/28/2014 Tim Albright - US16955
```


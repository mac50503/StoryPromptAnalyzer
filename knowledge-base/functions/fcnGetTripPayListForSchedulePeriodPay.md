# fcnGetTripPayListForSchedulePeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: List<TripPay>
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripPayListForSchedulePeriodPay`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (aSchedulePeriodPay <> null) thenreturn aSchedulePeriodPay.tripPayList.elsereturn null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```


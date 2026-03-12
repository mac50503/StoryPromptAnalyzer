# fcnGetLastNonRONDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetLastNonRONDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |

## Lógica de negocio

```blaze
counter is an integer initially 0.while counter < theTrip.dutyPeriodList.size() do {if (theTrip.dutyPeriodList.get(counter).dutyType = "RON" and counter > 0) then {fcnShow("The last Non RON duty period = " theTrip.dutyPeriodList.get(counter - 1).sequenceNumber).return theTrip.dutyPeriodList.get(counter - 1).}else if (theTrip.dutyPeriodList.get(counter).dutyType = "RON") then {fcnShow("The last Non RON duty period = null").return null.}counter += 1.}fcnShow("No RON duty period found... Returning the last duty period...").return theTrip.lastDutyPeriod.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`


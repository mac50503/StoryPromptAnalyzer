# fcnGetTimeDiffInHours

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetTimeDiffInHours`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateTime1 | DateTime | |
| dateTime2 | DateTime | |

## Lógica de negocio

```blaze
if (dateTime1 <> null and dateTime2 <> null) then{//fcnShow("===>>> in fucntion fcnGetTimeDiffInHours diff between " dateTime1 " and " dateTime2 " = " (dateTime2.millis - dateTime1.millis) / 60000 / 60).return math().truncate(fcnGetTimeDiffInMinutes(dateTime1, dateTime2) / 60).}elsereturn 0.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- `fcnShow()`


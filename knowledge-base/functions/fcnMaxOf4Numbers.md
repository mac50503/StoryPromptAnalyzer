# fcnMaxOf4Numbers

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnMaxOf4Numbers`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| arg1 | real | |
| arg2 | real | |
| arg3 | real | |
| arg4 | real | |

## Lógica de negocio

```blaze
return math().max(arg1, fcnMaxOf3Numbers(arg2, arg3, arg4)).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnMaxOf3Numbers](fcnMaxOf3Numbers.md)

## Llamado por

- [fcnGetDutyPeriodPay](fcnGetDutyPeriodPay.md)
- [fcnGetTripPay](fcnGetTripPay.md)
- [fcnMaxOf5Numbers](fcnMaxOf5Numbers.md)


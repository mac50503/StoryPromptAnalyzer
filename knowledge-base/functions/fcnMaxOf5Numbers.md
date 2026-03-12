# fcnMaxOf5Numbers

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnMaxOf5Numbers`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| arg1 | real | |
| arg2 | real | |
| arg3 | real | |
| arg4 | real | |
| arg5 | real | |

## Lógica de negocio

```blaze
return math().max(arg1, fcnMaxOf4Numbers(arg2, arg3, arg4, arg5)).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnMaxOf4Numbers](fcnMaxOf4Numbers.md)

## Llamado por

- [fcnMaxOf6Numbers](fcnMaxOf6Numbers.md)


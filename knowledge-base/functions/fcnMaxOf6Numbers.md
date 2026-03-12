# fcnMaxOf6Numbers

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnMaxOf6Numbers`

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
| arg6 | real | |

## Lógica de negocio

```blaze
return math().max(arg1, fcnMaxOf5Numbers(arg2, arg3, arg4, arg5, arg6)).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnMaxOf5Numbers](fcnMaxOf5Numbers.md)


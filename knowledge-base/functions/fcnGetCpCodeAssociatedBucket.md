# fcnGetCpCodeAssociatedBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetCpCodeAssociatedBucket`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| cpCode | string | |

## Lógica de negocio

```blaze
retVal is a string initially null.select cpCodecase "SA" : retVal = "SAFBUCKET".otherwise : retVal = null.return retVal;
```

## Llamado por

- [fcnCalculateTripCpCodePay](fcnCalculateTripCpCodePay.md)


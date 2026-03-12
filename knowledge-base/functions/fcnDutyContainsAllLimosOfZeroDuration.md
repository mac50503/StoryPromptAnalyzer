# fcnDutyContainsAllLimosOfZeroDuration

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDutyContainsAllLimosOfZeroDuration`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
legIndex is an integer initially 0.if (aPayDutyPeriod <> null) then {if (aPayDutyPeriod.legList.size() > 0) then {while (legIndex < aPayDutyPeriod.legList.size()) do {isLimo is a boolean initially aPayDutyPeriod.legList.get(legIndex).limoFlag.if fcnDetermineLimoOfZeroDuration(aPayDutyPeriod.legList.get(legIndex)) = false then {return false.}legIndex += 1.}return true.}}return false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDetermineLimoOfZeroDuration](fcnDetermineLimoOfZeroDuration.md)

## Llamado por

- [fcnCalculateStartOfRestForPay](fcnCalculateStartOfRestForPay.md)


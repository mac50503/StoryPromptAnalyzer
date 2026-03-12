# fcnCreateMileagePayResponse

## Metadata
- **Tipo**: SRL Function
- **Retorna**: MileagePayResponse
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCreateMileagePayResponse`

## Propósito
*(Sin descripción)*

## Lógica de negocio

```blaze
aMileagePayResponse is a MileagePayResponse.aMileagePay1 is a MileagePay.aMileagePay1.departureLocation = "DAL".aMileagePay1.departureLocation = "HOU".aMileagePay1.mileage = 239.0.aMileagePay1.payValue = 1.0.aMileagePay2 is a MileagePay.aMileagePay2.departureLocation = "DAL".aMileagePay2.departureLocation = "OKC".aMileagePay2.mileage = 182.0.aMileagePay2.payValue = 1.0.aMileagePay3 is a MileagePay.aMileagePay3.departureLocation = "MIA".aMileagePay3.departureLocation = "LAX".aMileagePay3.mileage = 2340.0.aMileagePay3.payValue = 6.2.aMileagePay4 is a MileagePay.aMileagePay4.departureLocation = "ORD".aMileagePay4.departureLocation = "HOU".aMileagePay4.mileage = 945.0.aMileagePay4.payValue = 2.8.aMileagePay5 is a MileagePay.aMileagePay5.departureLocation = "SFO".aMileagePay5.departureLocation = "JFK".aMileagePay5.mileage = 2580.0.aMileagePay5.payValue = 6.8.aMileagePay6 is a MileagePay.aMileagePay6.departureLocation = "IND".aMileagePay6.departureLocation = "SEA".aMileagePay6.mileage = 1860.0.aMileagePay6.payValue = 5.0.aMileagePayResponse.addMileagePay(aMileagePay1).aMileagePayResponse.addMileagePay(aMileagePay2).aMileagePayResponse.addMileagePay(aMileagePay3).aMileagePayResponse.addMileagePay(aMileagePay4).aMileagePayResponse.addMileagePay(aMileagePay5).aMileagePayResponse.addMileagePay(aMileagePay6).return aMileagePayResponse.
```


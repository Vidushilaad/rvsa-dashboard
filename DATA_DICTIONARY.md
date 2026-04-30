# Data Dictionary — India Vehicle Sales Dataset
**Project:** Region-wise Vehicle Sales Analysis across India  
**Dataset:** `india_vehicle_sales_raw.csv`  
**Generated:** Synthetic, anchored to SIAM FY2019–FY2024 published statistics  
**Rows:** ~2,700 (after introducing data quality issues)  
**Columns:** 10  

---

## Primary Sources (Ground Truth Anchors)
- SIAM (Society of Indian Automobile Manufacturers) — Annual Domestic Sales Reports FY2019–FY2024
- VAHAN Dashboard (Ministry of Road Transport & Highways) — State-wise EV registrations
- Published OEM annual reports (Hero MotoCorp, Maruti Suzuki, Tata Motors, etc.)

---

## Column Descriptions

| # | Column Name | Data Type | Description | Example Values |
|---|---|---|---|---|
| 1 | `Year` | String (Categorical) | Financial year of sale (April–March cycle) | FY2019, FY2020, … FY2024 |
| 2 | `Quarter` | String (Categorical) | Quarter within financial year | Q1 (Apr–Jun), Q2 (Jul–Sep), Q3 (Oct–Dec), Q4 (Jan–Mar) |
| 3 | `State` | String (Categorical) | Indian state where vehicle was sold | Maharashtra, Uttar Pradesh, Tamil Nadu … |
| 4 | `Region` | String (Categorical) | Macro-region grouping of states | North, South, East, West, Central, Northeast |
| 5 | `Segment` | String (Categorical) | Broad vehicle category | Two-Wheeler, Passenger Car, Commercial Vehicle, Electric Vehicle |
| 6 | `Vehicle_Class` | String (Categorical) | Sub-category within segment | SUV, Motorcycle, LCV, E-Two-Wheeler … |
| 7 | `Manufacturer` | String (Categorical) | OEM (Original Equipment Manufacturer) | Maruti Suzuki, Hero MotoCorp, Tata Motors … |
| 8 | `Fuel_Type` | String (Categorical) | Propulsion/fuel technology | Petrol, Diesel, Electric, CNG |
| 9 | `Units_Sold` | Float (Numeric) | Number of vehicles sold in that record | 12,450 — *2% 
| 10 | `Avg_Price_INR` | Float (Numeric) | Average selling price in Indian Rupees | 950,000 — *1.5% 
---

## Region Mapping

| Region | States Included |
|---|---|
| North | Uttar Pradesh, Delhi, Rajasthan, Haryana, Punjab, Uttarakhand, Himachal Pradesh, Jammu & Kashmir |
| South | Tamil Nadu, Karnataka, Andhra Pradesh, Telangana, Kerala |
| West | Maharashtra, Gujarat, Goa |
| East | West Bengal, Bihar, Odisha, Jharkhand |
| Central | Madhya Pradesh, Chhattisgarh |
| Northeast | Assam, Tripura, Meghalaya, Manipur, Nagaland, Sikkim |

---



## Key Metric — Units Sold vs Real SIAM Anchors (FY2019–FY2024 Cumulative)

| Segment | Real SIAM Total | Synthetic Total | Variance |
|---|---|---|---|
| Two-Wheeler | 101,118,000 | ~98,742,207 | 2.3% |
| Passenger Car | 20,020,000 | ~19,459,299 | 2.8% |
| Commercial Vehicle | 4,770,000 | ~4,755,820 | 0.3% |
| Electric Vehicle | 3,497,000 | ~3,377,969 | 3.4% |



## Granularity

Each row represents: **one (State × Year × Quarter × Segment × Manufacturer) combination**  
Not individual vehicle transactions — aggregated sales records, similar to SIAM's reporting format.

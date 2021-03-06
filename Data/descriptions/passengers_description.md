# Table **passengers**

Features:

- **departures_scheduled**: Departures Scheduled
- **departures_performed**: Departures Performed
- **payload**: Available Payload (pounds)
- **seats**: Available Seats
- **passengers**: Non-Stop Segment Passengers Transported
- **freight**: Non-Stop Segment Freight Transported (pounds)
- **mail**: Non-Stop Segment Mail Transported (pounds)
- **distance**: Distance between airports (miles)
- **ramp_to_ramp**: Ramp to Ramp Time (minutes)
- **air_time**: Airborne Time (minutes)
- **unique_carrier**: Unique Carrier Code. When the same code has been used by multiple carriers, a numeric suffix is used for earlier users, for example, PA, PA(1), PA(2). Use this field for analysis across a range of years.
- **airline_id**: An identification number assigned by US DOT to identify a unique airline (carrier). A unique airline (carrier) is defined as one holding and reporting under the same DOT certificate regardless of its Code, Name, or holding company/corporation.
- **unique_carrier_name**: Unique Carrier Name. When the same name has been used by multiple carriers, a numeric suffix is used for earlier users, for example, Air Caribbean, Air Caribbean (1).
- **region**: Carrier's Operation Region. Carriers Report Data by Operation Region
- **carrier**: Code assigned by IATA and commonly used to identify a carrier. As the same code may have been assigned to different carriers over time, the code is not always unique. For analysis, use the Unique Carrier Code.
- **carrier_name**: Carrier Name
- **carrier_group**: Carrier Group Code
- **carrier_group_new**: Carrier Group New
- **origin_airport_id**: Origin Airport, Airport ID. An identification number assigned by US DOT to identify a unique airport. Use this field for airport analysis across a range of years because an airport can change its airport code and airport codes can be reused.
- **origin_city_market_id**: Origin Airport, City Market ID. City Market ID is an identification number assigned by US DOT to identify a city market. Use this field to consolidate airports serving the same city market.	
- **origin**: Origin Airport
- **origin_city_name**: Origin City
- **origin_country**: Origin Country Code
- **origin_country_name**: Origin Country
- **dest_airport_id**: Destination Airport, Airport ID. An identification number assigned by US DOT to identify a unique airport. Use this field for airport analysis across a range of years because an airport can change its airport code and airport codes can be reused.
- **dest_city_market_id**: Destination Airport, City Market ID. City Market ID is an identification number assigned by US DOT to identify a city market. Use this field to consolidate airports serving the same city market.
- **dest**: Destination Airport
- **dest_city_name**: Destination City
- **dest_country**: Destination Country Code
- **dest_country_name**: Destination Country
- **aircraft_group**: Aircraft Group
- **aircraft_type**: Aircraft Type
- **aircraft_config**: Aircraft Configuration
- **month**: Month
- **year**: Year
- **distance_group**: Distance Intervals, every 500 Miles, for Flight Segment
- **class**: Service Class
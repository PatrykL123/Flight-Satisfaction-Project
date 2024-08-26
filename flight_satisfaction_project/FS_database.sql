CREATE DATABASE IF NOT EXISTS flight_satisfaction;
USE flight_satisfaction;


DROP TABLE IF EXISTS passenger_satisfaction;

CREATE TABLE passenger_satisfaction
(
			Gender BIT NOT NULL,
            Customer_Type BIT NOT NULL,
            Type_of_travel BIT NOT NULL,
            Business_Class BIT NOT NULL,
            Economy_Class BIT NOT NULL,
            Economy_Plus_Class BIT NOT NULL,
            Departure_Delay INT NOT NULL,
            Arrival_Delay INT NOT NULL,
            Time_Convenience INT NOT NULL,
            Ease_of_onl_booking INT NOT NULL,
            Check_in_Service INT NOT NULL,
            Online_Boarding INT NOT NULL,
            Gate_Location INT NOT NULL,
            On_board_service INT NOT NULL,
            Leg_Room_service INT NOT NULL,
            Cleanliness INT NOT NULL,
            In_flight_servie INT NOT NULL,
            in_fligh_wifi_service INT NOT NULL,
            in_flight_entertainment INT NOT NULL,
            Baggage_Handling INT NOT NULL,
            Probability DECIMAL(10,6) NOT NULL,
            Prediction INT NOT NULL 
            
            
            
);


SELECT Business_class,AVG(Prediction) * 100 as satisfaction_rate
FROM passenger_satisfaction
GROUP BY business_class;
SELECT * FROM passenger_satisfaction;


USE flight_satisfaction;

SELECT 
	CASE 
    WHEN customer_type = 0 THEN 'First Time' ELSE 'Returning' END as customer_type,
    CASE
    WHEN type_of_travel = 0 THEN 'Business' ELSE 'Personal' END as type_of_travel,
    AVG(prediction)
FROM passenger_satisfaction
GROUP BY customer_type,type_of_travel;
;


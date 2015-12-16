CREATE DATABASE IF NOT EXISTS BloodDonationStorage;

USE BloodDonationStorage;

CREATE TABLE IF NOT EXISTS Donors
(
First_name VARCHAR(100) NOT NULL,
Last_name VARCHAR(100) NOT NULL,
Weight INTEGER NOT NULL,
Gender VARCHAR(1) NOT NULL,
Date_of_birth DATE NOT NULL,
Donation_date DATE NOT NULL,
Sickness VARCHAR(1) NOT NULL,
ID_number VARCHAR(8) NOT NULL PRIMARY KEY,
Expiration_date DATE NOT NULL,
Blood_type VARCHAR(3) NOT NULL,
Email_address VARCHAR(100) NOT NULL,
Mobile_number VARCHAR(12) NOT NULL,
Hemoglobin_level INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Events
(
Id INTEGER AUTO_INCREMENT PRIMARY KEY,
Date_of_Event DATE NOT NULL,
Start_time DATE NOT NULL,
End_time DATE NOT NULL,
Zip_code INTEGER NOT NULL,
City VARCHAR(100) NOT NULL,
Address VARCHAR(100) NOT NULL,
Available_beds INTEGER NOT NULL,
Planned_donors INTEGER NOT NULL,
Max_donor_numbers INTEGER NOT NULL,
Successful_donations INTEGER NOT NULL
);
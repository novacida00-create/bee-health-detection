CREATE DATABASE IF NOT EXISTS bee_detection;
USE bee_detection;

CREATE TABLE IF NOT EXISTS detections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_filename VARCHAR(255) NOT NULL,
    health_status VARCHAR(100) NOT NULL,
    health_name VARCHAR(200) NOT NULL,
    health_confidence FLOAT NOT NULL,
    subspecies_name VARCHAR(200) NOT NULL,
    subspecies_confidence FLOAT NOT NULL,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

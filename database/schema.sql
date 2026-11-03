CREATE DATABASE IF NOT EXISTS fitnex_db;

USE fitnex_db;

-- 1. USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    gender VARCHAR(20),
    date_of_birth DATE,
    height DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- 2. HEALTH RECORDS TABLE
CREATE TABLE IF NOT EXISTS health_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    record_date DATE NOT NULL,
    steps INT DEFAULT 0,
    sleep_hours DECIMAL(4,2) DEFAULT 0,
    water_intake DECIMAL(4,2) DEFAULT 0,
    calories_consumed INT DEFAULT 0,
    calories_burned INT DEFAULT 0,
    heart_rate INT,
    weight DECIMAL(5,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    UNIQUE (user_id, record_date)
);


-- 3. FITNESS GOALS TABLE
CREATE TABLE IF NOT EXISTS fitness_goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    daily_steps INT DEFAULT 10000,
    daily_sleep DECIMAL(4,2) DEFAULT 8.00,
    daily_water DECIMAL(4,2) DEFAULT 3.00,
    daily_exercise INT DEFAULT 45,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);


-- 4. ACTIVITY RECORDS TABLE
CREATE TABLE IF NOT EXISTS activity_records (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    activity_name VARCHAR(100) NOT NULL,
    duration_minutes INT NOT NULL,
    calories_burned INT DEFAULT 0,
    activity_date DATE NOT NULL,
    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);


-- 5. USER SETTINGS TABLE
CREATE TABLE IF NOT EXISTS user_settings (
    setting_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    theme VARCHAR(20) DEFAULT 'dark',
    notifications BOOLEAN DEFAULT TRUE,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);
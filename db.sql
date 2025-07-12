-- Criar DB para o SíntesePlay


CREATE DATABASE IF NOT EXISTS SintesePlay;

USE SintesePlay;

CREATE TABLE IF NOT EXISTS state (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    abbreviation VARCHAR(2) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES state(id)
);

CREATE TABLE IF NOT EXISTS sports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone VARCHAR(17) NOT NULL,
    role ENUM('player', 'arena') NOT NULL DEFAULT 'player',
    full_name VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
);

-- Many to many entre usuários e esportes
CREATE TABLE IF NOT EXISTS favorite_sports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    sport_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

CREATE TABLE IF NOT EXISTS profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    skill_level ENUM('beginner', 'intermediate', 'advanced') NOT NULL DEFAULT 'beginner',
    city_id INT NOT NULL,
    profile_picture VARCHAR(255),
    banner_picture VARCHAR(255),
    date_of_birth DATE NOT NULL,
    bio TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id),
)

CREATE TABLE IF NOT EXISTS arena (
    -- Olhar com carinho
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city_id INT NOT NULL,
    phone VARCHAR(17),
    email VARCHAR(100),

    FOREIGN KEY (city_id) REFERENCES city(id)
);


CREATE TABLE IF NOT EXISTS arena_sports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    arena_id INT NOT NULL,
    sport_id INT NOT NULL,
    FOREIGN KEY (arena_id) REFERENCES arena(id),
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

CREATE TABLE IF NOT EXISTS arena_employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    arena_id INT NOT NULL,
    role ENUM('manager', 'staff') NOT NULL DEFAULT 'staff',
    user_id INT NOT NULL,
    FOREIGN KEY (arena_id) REFERENCES arena(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    arena_id INT,
    sport_id INT NOT NULL,
    status ENUM('public', 'private') NOT NULL DEFAULT 'public',
    date DATETIME NOT NULL,
    duration INT NOT NULL, -- duração em minutos
    max_players INT NOT NULL,
    FOREIGN KEY (schedule_id) REFERENCES schedule(id),
    FOREIGN KEY (arena_id) REFERENCES arena(id),
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

CREATE TABLE IF NOT EXISTS game_teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    team_name VARCHAR(100) NOT NULL,
    points INT NOT NULL DEFAULT 0,
    team_color VARCHAR(50),
    FOREIGN KEY (game_id) REFERENCES games(id)
);

CREATE TABLE IF NOT EXISTS game_participants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    user_id INT NOT NULL,
    team_id INT,
    status ENUM('confirmed', 'waiting', 'cancelled') NOT NULL DEFAULT 'waiting',
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS community (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS community_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    community_id INT NOT NULL,
    user_id INT NOT NULL,
    role ENUM('admin', 'member') NOT NULL DEFAULT 'member',
    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (community_id) REFERENCES community(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS community_posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    community_id INT NOT NULL,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (community_id) REFERENCES community(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    arena_id INT NOT NULL,
    sport_id INT NOT NULL,
    date DATETIME NOT NULL,
    duration INT NOT NULL,
    max_players INT NOT NULL,
    FOREIGN KEY (arena_id) REFERENCES arena(id),
    FOREIGN KEY (sport_id) REFERENCES sports(id)
);

CREATE TABLE IF NOT EXISTS schedule_participants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    schedule_id INT NOT NULL,
    user_id INT NOT NULL,
    status ENUM('confirmed', 'waiting', 'cancelled') NOT NULL DEFAULT 'waiting',
    FOREIGN KEY (schedule_id) REFERENCES schedule(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
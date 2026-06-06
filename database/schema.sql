USE recruitai;

CREATE TABLE IF NOT EXISTS candidates (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(255),

    email VARCHAR(255) UNIQUE,

    phone VARCHAR(20),

    skills TEXT,

    education TEXT,

    experience TEXT,

    ats_score INT DEFAULT 0,

    status ENUM(
        'Pending',
        'Shortlisted',
        'Rejected'
    ) DEFAULT 'Pending',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS jobs (

    id INT AUTO_INCREMENT PRIMARY KEY,

    title VARCHAR(255),

    description TEXT,

    required_skills TEXT,

    min_experience INT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS interviews (

    id INT AUTO_INCREMENT PRIMARY KEY,

    candidate_id INT,

    interview_date DATE,

    interview_time TIME,

    status VARCHAR(50),

    FOREIGN KEY(candidate_id)
    REFERENCES candidates(id)
);
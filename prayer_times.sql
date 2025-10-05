CREATE TABLE prayer_times (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    island VARCHAR(50),
    date DATE,
    imsaak TIME,
    fajr TIME,
    sunrise TIME,
    dhuhr TIME,
    asr TIME,
    maghrib TIME,
    isha TIME
);

import random
from datetime import datetime, timedelta

LOG_LEVELS = ["INFO", "ERROR", "DEBUG", "WARN"]

MESSAGES = {
    "INFO": [
        "User admin logged in",
        "User accessed dashboard",
        "Process completed successfully",
        "Session started"
    ],
    "ERROR": [
        "Failed to connect to database",
        "Timeout while calling external service",
        "Null pointer exception",
        "Permission denied"
    ],
    "DEBUG": [
        "Query executed in 120ms",
        "Cache refreshed",
        "Debugging authentication flow",
        "Payload validated successfully"
    ],
    "WARN": [
        "Connection pool running low",
        "High memory usage detected",
        "Disk space reaching limit",
        "Retrying failed request"
    ]
}

TOTAL_LINES = 1_000_000
START_TIME = datetime(2024, 11, 8, 10, 0, 0)

with open("app.log", "w", encoding="utf-8") as file:
    current_time = START_TIME

    for _ in range(TOTAL_LINES):
        log_level = random.choice(LOG_LEVELS)
        message = random.choice(MESSAGES[log_level])

        log_entry = f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} {log_level} {message}\n"
        file.write(log_entry)

        # Incrementa o timestamp em alguns segundos aleatórios
        current_time += timedelta(seconds=random.randint(1, 5))

print("Arquivo app.log gerado com sucesso com 1 milhão de linhas.")
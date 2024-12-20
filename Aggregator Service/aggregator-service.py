import psycopg2
from datetime import datetime

# Redshift connection details
DB_CONFIG = {
    "dbname": "meditrack",
    "user": "awsuser",
    "password": "Mitesp2024",
    "host": "medi-track-cluster.cbbshrcivxlr.us-east-1.redshift.amazonaws.com:5439/dev",
    "port": 5439
}

def aggregate_data():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Example Aggregations
        # 1. Appointments per doctor
        cursor.execute("""
            INSERT INTO metrics.appointments_per_doctor (doctor_id, appointment_count)
            SELECT doctor_id, COUNT(*) AS appointment_count
            FROM appointments
            GROUP BY doctor_id;
        """)

        # 2. Appointment frequency over time
        cursor.execute("""
            INSERT INTO metrics.appointment_frequency (appointment_day, daily_count)
            SELECT DATE(appointment_date) AS appointment_day, COUNT(*) AS daily_count
            FROM appointments
            GROUP BY appointment_day
            ORDER BY appointment_day;
        """)

        # 3. Symptoms by specialty
        cursor.execute("""
            INSERT INTO metrics.symptoms_by_specialty (specialty, symptom, occurrence)
            SELECT specialty, symptom, COUNT(*) AS occurrence
            FROM patient_records
            GROUP BY specialty, symptom
            ORDER BY occurrence DESC;
        """)

        conn.commit()
        print("Metrics successfully stored in Redshift!")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error storing metrics in Redshift: {e}")

if __name__ == "__main__":
    aggregate_data()

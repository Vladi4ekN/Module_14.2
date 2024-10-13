import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE id = ?", (6,))
conn.commit()


cursor.execute("SELECT COUNT(*) FROM users")
total_records = cursor.fetchone()[0]


cursor.execute("SELECT SUM(balance) FROM users")
total_balance = cursor.fetchone()[0]


average_balance = total_balance / total_records if total_records > 0 else 0
print(f"Общее количество записей: {total_records}")
print(f"Сумма всех балансов: {total_balance}")
print(f"Средний баланс: {average_balance:.2f}")

conn.close()
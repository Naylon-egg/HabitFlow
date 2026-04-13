from database import cursor
from collections import Counter

def habit_stats(habit_id):
    cursor.execute("SELECT done FROM records WHERE habit_id=?", (habit_id,))
    data = cursor.fetchall()

    total = len(data)
    done = sum([x[0] for x in data])

    if total == 0:
        return "No data yet."

    rate = (done / total) * 100
    return f"Completion rate: {rate:.2f}%"


def best_day():
    cursor.execute("SELECT date FROM records")
    dates = [row[0] for row in cursor.fetchall()]

    days = [d.split('-')[2] for d in dates]
    count = Counter(days)

    if not count:
        return "Not enough data."

    best = count.most_common(1)[0]
    return f"Most productive day: {best[0]}"
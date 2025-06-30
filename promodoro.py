import time

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f'\r⏳ Χρόνος: {timer}', end='')
        time.sleep(1)
        total_seconds -= 1
    print('\n🛎️ Ο χρόνος έληξε!')

def pomodoro():
    while True:
        print('\n💼 Ώρα για συγκέντρωση (25 λεπτά)...')
        countdown(25)

        print('\n☕ Μικρό διάλειμμα (5 λεπτά)...')
        countdown(5)

        again = input('\n🔁 Θες να ξεκινήσεις άλλον κύκλο; (ναι/όχι): ').strip().lower()
        if again != 'ναι':
            print('👋 Καλή ξεκούραση!')
            break

pomodoro()
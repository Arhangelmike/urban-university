import threading, time
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}"
            file.write(word + '\n')

            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")

# method start 1

start_time_thread = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time_thread = datetime.now()
delta_time = end_time_thread - start_time_thread
print(f"Время выполнения потоков: {delta_time} секунд")

# method start 2

start_time = datetime.now()

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

# thread1 = threading.Timer(0.1, write_words, args=(10, 'example5.txt'))
# thread2 = threading.Timer(0.1, write_words, args=(30, 'example6.txt'))
# thread3 = threading.Timer(0.1, write_words, args=(200, 'example7.txt'))
# thread4 = threading.Timer(0.1, write_words, args=(100, 'example8.txt'))


thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time = datetime.now()
delta_time1 = end_time - start_time
print(f"Время выполнения потоков: {delta_time1} секунд")
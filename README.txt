# Инструкция по запуску на Render

1. Зайди на https://render.com и зарегистрируйся (можно через Google/GitHub).
2. Создай новый **Web Service** или **Background Worker** (лучше Worker).
3. Когда Render попросит подключить репозиторий — загрузи папку с этим ботом на GitHub.
4. В Render укажи:
   - Start Command: `python bot.py`
   - Environment: Python 3
5. Добавь переменную окружения (Environment Variable):
   - KEY: `API_TOKEN`
   - VALUE: твой токен Telegram.
6. Нажми Deploy — бот запустится и будет работать 24/7.

FROM python

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Command to run the bot
CMD ["python", "bot.py"]

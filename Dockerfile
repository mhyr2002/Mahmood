# استفاده از تصویر رسمی پایتون 3.8 به صورت سبک به عنوان تصویر پایه
FROM python:3.8-slim-buster

# تنظیم متغیرهای محیطی برای جلوگیری از نوشتن فایل‌های .pyc در دیسک
ENV PYTHONDONTWRITEBYTECODE=1
# اطمینان از اینکه خروجی به طور مستقیم به ترمینال ارسال می‌شود بدون بافر
ENV PYTHONUNBUFFERED=1

# تنظیم دایرکتوری کاری داخل کانتینر به /app
WORKDIR /app

# کپی کردن فایل requirements.txt به دایرکتوری /app در کانتینر
COPY requirements.txt /app/

# به‌روزرسانی pip به آخرین نسخه
RUN pip3 install --upgrade pip

# نصب بسته‌های پایتون مشخص شده در requirements.txt
RUN pip3 install -r requirements.txt

# کپی کردن فایل‌های اصلی برنامه از میزبان به دایرکتوری /app در کانتینر
COPY ./core /app

# خط زیر را برای اجرای سرور توسعه Django فعال کنید
# CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
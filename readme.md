# THAI ID CARD OCR RECOGNIZATION AND HANDLING


## How to Install
1. Install Tesseract from [Tesseract](https://github.com/tesseract-ocr/tesseract#installing-tesseract)
2. Update the Tesseract to the path variable
3. Install required libraries by ```pip install -r requirements.txt```
4. On bash, write following commands (must be in the same directory)
```console
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

the server will be started on http://127.0.0.1:8000

## Screenshots of webapplication

1. Home Page
![image](https://github.com/aditya-1511-rathore/AdityaSingh_Qoala/assets/72315357/e10cebf9-5c43-42b8-8411-37aa0f8d200e)

3. After Upload of Image
![image](https://github.com/aditya-1511-rathore/AdityaSingh_Qoala/assets/72315357/16e8382c-9538-4c9c-9220-f52606591bda)

4. Result is shown after the OCR scanning is completed, and prompt to edit and delete
![image](https://github.com/aditya-1511-rathore/AdityaSingh_Qoala/assets/72315357/227d1a40-86b5-43a2-9cb8-c9a60cf88276)

5. List of all Scans
![image](https://github.com/aditya-1511-rathore/AdityaSingh_Qoala/assets/72315357/43547d67-2c72-48e9-8180-45497b4ea0c1)

6. Result after uploading the Thai id card that is already available int he database
![image](https://github.com/aditya-1511-rathore/AdityaSingh_Qoala/assets/72315357/196b6400-6a88-4c26-856a-afbd4ede1f70)


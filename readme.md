# Deploy Django App to vercel

## 1. project settings.py 
	`DEBUG = False`
	`ALLOWED_HOSTS = ['.vercel.app']`

	You must set settings.ALLOWED_HOSTS if DEBUG is False.
	
	`ALLOWED_HOSTS = ['*']` 

## 2. Add 'vercel.json' file in root folder

## 3. create 'app' variable in wsgi.py file
	`app = application`

## 4. Congratulations! You have successfully deployed Django Application to vercel
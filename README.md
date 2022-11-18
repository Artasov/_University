# UNIVERSITY APP

## **Project deployment**

1. In the `terminal` (Windows/Linux).

    ```
    git clone https://github.com/Artasov/_University.git
    cd _University
    ```
2. Quick start `Postgres` and `Redis`.
    ```
    docker run -d --name redis-server -p 6379:6379 redis/redis-stack-server:latest
    docker run --name postgres-server -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=db -d postgres:latest
    ```
3. In the folder with the file `manage.py`.
    ```
    python manage.py runserver
    WIN: celery -A config worker -l INFO --pool=solo
    LINUX: celery -A config worker -l INFO
    ```
4. Go to:
    - http://localhost:8000/ - Redirect to API docs (Swagger).
    - http://localhost:8000/docs/ - API docs (Swagger).
    - http://localhost:8000/admin - Admin Panel
    
6. For create test case:
    ```
    python manage.py init_university_test_case
    ```
    ```
    Generated(login:pass):
        Superuser
            admin:1
        Administrator 
            a1:1
        Curator 
            c1:1   
        Curator 
            c2:1
        50 students  
            s0,s1,s2,...,s49:1
        
        Other tables are also slightly filled in.
    ```

7. The environment variables are specified in the .env file.
    ```
    DEBUG=1
    DB_NAME=db
    DB_USERNAME=root
    DB_PASSWORD=root
    DB_HOST=localhost
    DB_PORT=5432
    REDIS_HOST=localhost
    REDIS_PORT=6379
    ```
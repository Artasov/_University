# UNIVERSITY APP

## **Project deployment**

1. In the `terminal` (Windows/Linux).

    ```
    git clone https://github.com/Artasov/Chat.git
    cd Chat
    ```
3. Go to:
    - http://localhost:8000/ - to get started.
    - http://localhost:8000/docs/ - API docs (Swagger).
    - http://localhost:8000/admin - Admin Panel
    - http://localhost:8000/file-manager/ - File Manager
    - http://localhost:8000/mkdir/ - Make Dir
    - http://localhost:8000/upload/ - Upload Files
    - http://localhost:9000/ - Minio Storage
    - http://localhost:9001/ - Minio GUI
    - http://localhost:5432/ - Postgres
    
4. The environment variables are specified in the .env file.
    ```
    MINIO_ACCESS_KEY="adminadmin"
    MINIO_SECRET_KEY="adminadmin"
    MINIO_ROOT_USER="adminadmin"
    MINIO_ROOT_PASSWORD="adminadmin"
    POSTGRES_NAME="adminadmin"
    POSTGRES_USER="adminadmin"
    POSTGRES_PASSWORD="adminadmin"
    POSTGRES_PORT="5432"
    DJANGO_SUPERUSER_USERNAME="adminadmin"
    DJANGO_SUPERUSER_PASSWORD="adminadmin"
    DJANGO_SUPERUSER_EMAIL="adminadmin@admin.admin"
    DEBUG="1"
    NAME_MAIN_FILEMANAGER_DIR="MAIN"
    ```

4. Automatically created users:
    ```
    admin - adminadmin:adminadmin
    user1 - user1:user1
    user2 - user2:user2
    ```

5. The environment variables are specified in the .env file.
    ```
    POSTGRES_NAME="adminadmin"
    POSTGRES_USER="adminadmin"
    POSTGRES_PASSWORD="adminadmin"
    POSTGRES_PORT="5432"
    DJANGO_SUPERUSER_USERNAME="adminadmin"
    DJANGO_SUPERUSER_PASSWORD="adminadmin"
    DJANGO_SUPERUSER_EMAIL="adminadmin@admin.admin"
    DEBUG="1"
    ```
   
    Использовать Postgres при больших объемах не эффективно, 
    если бы это был реальный проект я бы посмотрел на nosql бд.
    Пагинация реализована.
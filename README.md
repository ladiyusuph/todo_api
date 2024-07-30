## A Django Rest Framework (DRF) CRUD API project for managing todo lists with user authentication.
### Endpoints

   #### Authentication:
        Login: /api/v1/login/
        Logout: /api/v1/logout/
   #### Tasks:
        List: /api/v1/tasks/
        Create: /api/v1/tasks/create/
        Update: /api/v1/tasks/<id>/update
        Delete: /api/v1/tasks/<id>/delete
        Filter by status: /api/v1/tasks/?status=<status>
        Get individual task: /api/v1/tasks/<id>/


# Coderhouse Python - 54130

## Taskbuddy

Proyecto final: aplicación de gestión de tareas. Las tareas se agrupan en proyectos y cada tarea puede tener subtareas. En algún caso puede que no se muestren las tareas asociadas a un proyecto o las subtareas asociadas a una tarea, no llegué a solucionar ese tema de las relaciones entre elementos del modelo pero se dijo en clase que no era obligatorio debido a su dificultad.

### Author

        Walter Zein - walter.zein@gmail.com

### Listado de URLs

        "/", Home View,
        "projects/about/", Acerca del autor
        "projects/list/", Vista de lista de proyectos
        "projects/create/", Vista de creación de proyecto
        "projects/<int:pk>/detail/", Vista de detalle de proyecto
        "projects/<int:pk>/update/", Vista de actualización/edición de proyecto
        "projects/<int:pk>/delete/", Vista de borrado de proyecto
        "tasks/list/", Vista de lista de tareas
        "tasks/create/", Vista de creación de tarea
        "tasks/<int:pk>/detail/", Vista de detalle de tarea
        "tasks/<int:pk>/update/", Vista de actualización de tarea
        "tasks/<int:pk>/delete/", Vista de borrado de tarea
        "tasks/search/", Vista de búsqueda de tarea
        "subtasks/list/", Vista de lista de subtareas
        "subtasks/create/", Vista de creación de subtarea
        "subtasks/<int:pk>/detail/", Vista de detalle de subtarea
        "subtasks/<int:pk>/update/", Vista de actualización de subtarea
        "subtasks/<int:pk>/delete/", Vista de borrado de subtarea
        "login", Vista de login de usuario
        "logout", Vista de logout de usuario
        "edit-user/", Vista de edición de usuario

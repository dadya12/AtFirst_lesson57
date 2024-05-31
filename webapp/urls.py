from django.urls import path
from webapp.templates.tag_views.views import TagCreate, TagUpdate, TagDetail, TagDelete
from webapp.templates.project_views.views import IndexView, ProjectDetail, ProjectCreate, ProjectUpdate, ProjectDelete, \
    UpdateUserView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='detail_project'),
    path('project/create/', ProjectCreate.as_view(), name='create_project'),
    path('project/<int:pk>/update', ProjectUpdate.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='delete_project'),
    path('project/<int:pk>/create/tag', TagCreate.as_view(), name='tag_create'),
    path('project/<int:pk>/update/tag', TagUpdate.as_view(), name='tag_update'),
    path('project/<int:pk>/detail/tag', TagDetail.as_view(), name='tag_detail'),
    path('project/<int:pk>/delete/tag', TagDelete.as_view(), name='tag_delete'),
    path('projects/<int:pk>/users/update/', UpdateUserView.as_view(), name='update_user'),

]

from rest_framework_nested import routers
from . import views

# Define the main router and register the main viewsets
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet, basename='Course')
router.register('teachers', views.TeacherViewSet, basename='Teacher')
router.register('log', views.LogViewSet, basename='log')
router.register('prereg', views.PreregViewSet, basename="Prereg")

# Define the nested router for courses
courses_router = routers.NestedDefaultRouter(router, 'courses', lookup='course')
courses_router.register('attributes', views.CourseAttributesViewSet, basename='course-attributes')

urlpatterns = router.urls + courses_router.urls
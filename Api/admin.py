from django.contrib import admin

# Register your models here.
from .models import Elevator_System,Elevator,ElevatorRequest

class ElevatorAdmin(admin.StackedInline):
    model = Elevator # Adds under a Elevator System

class ElevatorSystemAdmin(admin.ModelAdmin):
    inlines = [ElevatorAdmin] # For adding multiple elevators in ADMIN Panel

admin.site.register(Elevator) # Also adding option to add Elevator independently

# To register an elevator to a elevator_system through ADMIN.
admin.site.register(Elevator_System,ElevatorSystemAdmin)

class ElevatorRequestAdmin(admin.ModelAdmin):
      list_display=["elevator","from_floor","to_floor","is_active"]
      list_filter=["created_time","elevator"]
      
admin.site.register(ElevatorRequest,ElevatorRequestAdmin)

from django.db import models

RELEVANCE_CHOICES = (
    (0, ("STEADY")),
    (1, ("GOING_UP")),
    (2, ("GOING_DOWN"))
)

# Represents ELEVATOR SYSYTEM object for a particular building.
class Elevator_System(models.Model):
  
  name = models.CharField(max_length = 225,blank=True,null=True)
  minimum_floor = models.IntegerField(default=0,blank=True,null=True)
  maximum_floor = models.IntegerField(blank=True,null=True)
  number_of_elevators = models.PositiveSmallIntegerField(blank=True,null=True)

  def __str__(self):
    return str(self.name)

# Respresents any ELEVATOR for an ELEVATOR SYSTEM for a building, with all its specs.
class Elevator(models.Model):

  elevator_system = models.ForeignKey(Elevator_System , on_delete=models.CASCADE)
  doors_opened = models.BooleanField(default=True,blank=True,null=True)
  elevator_number = models.IntegerField(blank=True,null=True)
  current_floor = models.PositiveSmallIntegerField(default=0,blank=True,null=True)
  is_working = models.BooleanField(default=True,blank=True,null=True)
  status = models.IntegerField(choices=RELEVANCE_CHOICES,default=0,blank=True,null=True)


  def __str__(self):
    return "Elevator_Number" + str(self.elevator_number)
    
# Respresents details of an Elevator requested by a user/tenant/owner.
class ElevatorRequest(models.Model):
  
  elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
  from_floor = models.PositiveSmallIntegerField(blank=True,null=True)
  to_floor = models.PositiveSmallIntegerField(blank=True,null=True)
  created_time = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True,blank=True,null=True)

  def __str__(self):
    return str(self.elevator)+" is Requested from floor "+str(self.from_floor)+" to floor "+str(self.to_floor)
    

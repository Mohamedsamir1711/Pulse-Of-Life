from django.db import models

class loginpage(models.Model):
    Email = models.EmailField()
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.Email
    
    class Meta:
        verbose_name = 'log in page'
        ordering = ['Email']

class profil(models.Model):
    gen = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    fname = models.CharField(max_length= 15)
    lname = models.CharField(max_length= 15)
    Email = models.EmailField()
    Password = models.CharField(max_length=20) 
    gender = models.CharField(max_length=20, choices=gen)


    def __str__(self):
        return self.fname
    
    class Meta:
        verbose_name = 'Profile'
        ordering = ['fname']


class Appointment(models.Model):
    DOCTORS = [
        ('john_smith', 'Dr. John Smith — Cardiologist'),
        ('emily_johnson', 'Dr. Emily Johnson — Pediatrician'),
        ('robert_brown', 'Dr. Robert Brown — Family Physician'),
        ('sarah_davis', 'Dr. Sarah Davis — Obstetrician'),
        ('michael_wilson', 'Dr. Michael Wilson — Surgeon'),
        ('jessica_taylor', 'Dr. Jessica Taylor — Internist'),
    ]
    VISIT_TYPES = [
        ('in_person', 'In-person visit'),
        ('video', 'Video consultation'),
    ]
    TIME_SLOTS = [
        ('09:00', '09:00 AM'), ('10:00', '10:00 AM'), ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'), ('14:00', '02:00 PM'), ('15:00', '03:00 PM'),
        ('16:00', '04:00 PM'), ('17:00', '05:00 PM'),
    ]
    STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL, related_name='appointments')
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    doctor = models.CharField(max_length=40, choices=DOCTORS)
    visit_type = models.CharField(max_length=20, choices=VISIT_TYPES, default='in_person')
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_SLOTS)
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} — {self.get_doctor_display()} on {self.date} {self.time}"

    class Meta:
        ordering = ['-created_at']

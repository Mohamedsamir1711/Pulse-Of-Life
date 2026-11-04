# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Ftable(models.Model):
#     age = models.IntegerField(db_column='Age')  # Field name made lowercase.
#     restingbp = models.IntegerField(db_column='RestingBP')  # Field name made lowercase.
#     cholesterol = models.IntegerField(db_column='Cholesterol')  # Field name made lowercase.
#     fastingbs = models.IntegerField(db_column='FastingBS')  # Field name made lowercase.
#     maxhr = models.IntegerField(db_column='MaxHR')  # Field name made lowercase.
#     oldpeak = models.FloatField(db_column='Oldpeak')  # Field name made lowercase.
#     heartdisease = models.IntegerField(db_column='HeartDisease')  # Field name made lowercase.
#     patientid = models.IntegerField(db_column='PatientID')  # Field name made lowercase.
#     timestep = models.IntegerField(db_column='TimeStep')  # Field name made lowercase.
#     heartrate = models.FloatField(db_column='HeartRate')  # Field name made lowercase.
#     oxygensaturation = models.FloatField(db_column='OxygenSaturation')  # Field name made lowercase.
#     sex_m = models.FloatField(db_column='Sex_M')  # Field name made lowercase.
#     chestpaintype_ata = models.FloatField(db_column='ChestPainType_ATA')  # Field name made lowercase.
#     chestpaintype_nap = models.FloatField(db_column='ChestPainType_NAP')  # Field name made lowercase.
#     chestpaintype_ta = models.FloatField(db_column='ChestPainType_TA')  # Field name made lowercase.
#     restingecg_normal = models.FloatField(db_column='RestingECG_Normal')  # Field name made lowercase.
#     restingecg_st = models.FloatField(db_column='RestingECG_ST')  # Field name made lowercase.
#     exerciseangina_1 = models.FloatField(db_column='ExerciseAngina_1')  # Field name made lowercase.
#     st_slop_flat = models.FloatField(db_column='ST_Slop_Flat')  # Field name made lowercase.
#     st_slop_up = models.FloatField(db_column='ST_Slop_Up')  # Field name made lowercase.
#     deviceid = models.IntegerField(db_column='deviceID', unique=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ftable'


# class HomeLoginpage(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     email = models.CharField(db_column='Email', max_length=254)  # Field name made lowercase.
#     password = models.CharField(max_length=40)

#     class Meta:
#         managed = False
#         db_table = 'home_loginpage'


# class HomeProfil(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     fname = models.CharField(max_length=15)
#     lname = models.CharField(max_length=15)
#     email = models.CharField(db_column='Email', max_length=254)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
#     gender = models.CharField(max_length=20)

#     class Meta:
#         managed = False
#         db_table = 'home_profil'


# class ShowReportsResult(models.Model):
#     id = models.BigAutoField(primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'show_reports_result'


# class Stable(models.Model):
#     age = models.IntegerField(db_column='Age')  # Field name made lowercase.
#     sex = models.TextField(db_column='Sex')  # Field name made lowercase.
#     chestpaintype = models.TextField(db_column='ChestPainType')  # Field name made lowercase.
#     restingbp = models.IntegerField(db_column='RestingBP')  # Field name made lowercase.
#     cholestrol = models.IntegerField(db_column='Cholestrol')  # Field name made lowercase.
#     fastingbs = models.IntegerField(db_column='FastingBS')  # Field name made lowercase.
#     restingecg = models.TextField(db_column='RestingECG')  # Field name made lowercase.
#     maxhr = models.IntegerField(db_column='MaxHR')  # Field name made lowercase.
#     exerciseangina = models.TextField(db_column='ExerciseAngina')  # Field name made lowercase.
#     oldpeak = models.FloatField(db_column='Oldpeak')  # Field name made lowercase.
#     st_slope = models.TextField(db_column='ST_Slope')  # Field name made lowercase.
#     heartdisease = models.IntegerField(db_column='HeartDisease')  # Field name made lowercase.
#     patientid = models.IntegerField(db_column='PatientID')  # Field name made lowercase.
#     timestep = models.IntegerField(db_column='TimeStep')  # Field name made lowercase.
#     heartrate = models.FloatField(db_column='HeartRate')  # Field name made lowercase.
#     bloodpressure = models.FloatField(db_column='BloodPressure')  # Field name made lowercase.
#     oxygensaturation = models.FloatField(db_column='OxygenSaturation')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'stable'

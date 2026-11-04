# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ftable(models.Model):
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    restingbp = models.IntegerField(db_column='RestingBP')  # Field name made lowercase.
    cholesterol = models.IntegerField(db_column='Cholesterol')  # Field name made lowercase.
    fastingbs = models.IntegerField(db_column='FastingBS')  # Field name made lowercase.
    maxhr = models.IntegerField(db_column='MaxHR')  # Field name made lowercase.
    oldpeak = models.FloatField(db_column='Oldpeak')  # Field name made lowercase.
    heartdisease = models.IntegerField(db_column='HeartDisease')  # Field name made lowercase.
    patientid = models.IntegerField(db_column='PatientID',primary_key=True)  # Field name made lowercase.
    timestep = models.IntegerField(db_column='TimeStep')  # Field name made lowercase.
    heartrate = models.FloatField(db_column='HeartRate')  # Field name made lowercase.
    oxygensaturation = models.FloatField(db_column='OxygenSaturation')  # Field name made lowercase.
    sex_m = models.FloatField(db_column='Sex_M')  # Field name made lowercase.
    chestpaintype_ata = models.FloatField(db_column='ChestPainType_ATA')  # Field name made lowercase.
    chestpaintype_nap = models.FloatField(db_column='ChestPainType_NAP')  # Field name made lowercase.
    chestpaintype_ta = models.FloatField(db_column='ChestPainType_TA')  # Field name made lowercase.
    restingecg_normal = models.FloatField(db_column='RestingECG_Normal')  # Field name made lowercase.
    restingecg_st = models.FloatField(db_column='RestingECG_ST')  # Field name made lowercase.
    exerciseangina_1 = models.FloatField(db_column='ExerciseAngina_1')  # Field name made lowercase.
    st_slop_flat = models.FloatField(db_column='ST_Slop_Flat')  # Field name made lowercase.
    st_slop_up = models.FloatField(db_column='ST_Slop_Up')  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='deviceID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ftable'


class Stable(models.Model):
    age = models.IntegerField(db_column='Age') # Field name made lowercase.
    sex = models.TextField(db_column='Sex')  # Field name made lowercase.
    chestpaintype = models.TextField(db_column='ChestPainType')  # Field name made lowercase.
    restingbp = models.IntegerField(db_column='RestingBP')  # Field name made lowercase.
    cholestrol = models.IntegerField(db_column='Cholestrol')  # Field name made lowercase.
    fastingbs = models.IntegerField(db_column='FastingBS')  # Field name made lowercase.
    restingecg = models.TextField(db_column='RestingECG')  # Field name made lowercase.
    maxhr = models.IntegerField(db_column='MaxHR')  # Field name made lowercase.
    exerciseangina = models.TextField(db_column='ExerciseAngina')  # Field name made lowercase.
    oldpeak = models.FloatField(db_column='Oldpeak')  # Field name made lowercase.
    st_slope = models.TextField(db_column='ST_Slope')  # Field name made lowercase.
    heartdisease = models.IntegerField(db_column='HeartDisease')  # Field name made lowercase.
    patientid = models.IntegerField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    timestep = models.IntegerField(db_column='TimeStep')  # Field name made lowercase.
    heartrate = models.FloatField(db_column='HeartRate')  # Field name made lowercase.
    bloodpressure = models.FloatField(db_column='BloodPressure')  # Field name made lowercase.
    oxygensaturation = models.FloatField(db_column='OxygenSaturation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stable'

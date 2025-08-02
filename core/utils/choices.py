"""
This file contains all the choices used in the application.
"""

from django.utils.translation import gettext_lazy as _

TYPES_SERVICES_CHOICES = (
    ("EP", _("Team")),
    ("MQ", _("Machine")),
    ("TP", _("Transport")),
    ("SA", _("Health")),
)
CATEGORY_FILES_CHOICES = (
    ("C", _("Contract")),
    ("A", _("Addendum")),
)
DAYS_WEEK_CHOICES = (
    ("SEGUNDA-FEIRA", _("Monday")),
    ("TERÇA-FEIRA", _("Tuesday")),
    ("QUARTA-FEIRA", _("Wednesday")),
    ("QUINTA-FEIRA", _("Thursday")),
    ("SEXTA-FEIRA", _("Friday")),
    ("SÁBADO", _("Saturday")),
    ("DOMINGO", _("Sunday")),
)
PERSON_TYPE_CHOICES = (
    ("F", _("Physical Person")),
    ("J", _("Legal Person")),
)

SEGMENT_CHOICES = (
    ("PV", _("Private")),
    ("PB", _("Public")),
)

STATUS_MAINTENANCE_CHOICES = (
    ("A", _("Scheduled")),
    ("E", _("In Progress")),
    ("C", _("Cancelled")),
    ("F", _("Finished")),
)
COMPOSITION_CHOICES = (
    ("JT", _("Together")),
    ("IN", _("Individuals")),
)
UNIT_CONSIDER_CALC_CHOICES = (
    ("PS", _("Weight")),
    ("VL", _("Volume")),
    ("NA", _("Does Not Apply")),
)
WASTE_UNIT_CHOICES = (
    ("KG", _("Kilogram")),
    ("TON", _("Tonne")),
)
UNIT_CHOICES = WASTE_UNIT_CHOICES + (
    ("HRS", _("Hours")),
    ("M³", _("Cubic Meter")),
    ("DIA", _("Daily")),
    ("MEN", _("Monthly")),
    ("VIA", _("Trip")),
)
WORKFORCE_CHOICES = (
    ("EP", _("Team")),
    ("HRS", _("Hours")),
    ("DIA", _("Daily")),
    ("MEN", _("Monthly")),
)
TYPE_FRANCHISE_CHOICES = (
    ("CON", _("Contract")),
    ("MEN", _("Monthly")),
    ("UNI", _("Unitary")),
)

CONFERENCE_MEMBER_STATUS_CHOICES = (
    ("P", _("Present")),
    ("A", _("Absent")),
)

PHOTO_STATUS_CHOICES = (
    ("APR", _("Approved")),
    ("REJ", _("Rejected")),
)

PHOTOGRAPHIC_REGISTER_STATUS_CHOICES = PHOTO_STATUS_CHOICES + (("PEN", _("Pending")),)

HOLIDAY_SCOPE_CHOICES = (
    ("NAC", _("National")),
    ("EST", _("State")),
    ("MUN", _("Municipal")),
)

CONTRACT_TYPES_CHOICES = (
    ("LIM", _("Public Cleaning")),
    ("SAU", _("Health")),
    ("AVU", _("Detached")),
    ("MAO", _("Workforce")),
)

PERIOD_DAY_CHOICES = (
    ("MAT", _("Morning")),
    ("VES", _("Afternoon")),
    ("NOT", _("Night")),
)

ZONE_CHOICES = (
    ("URB", _("Urban")),
    ("RUR", _("Rural")),
)

VEHICLE_TYPE_CHOICES = (
    ("VE", _("Vehicle")),
    ("MQ", _("Machine")),
)

VEHICLE_STATUS = (
    ("DIS", _("Available")),
    ("MAT", _("Maintenance")),
    ("USO", _("In Use")),
)

VEHICLE_FUEL_CHOICES = (
    ("DIE", _("Diesel")),
    ("GAS", _("Gasoline")),
    ("ETA", _("Ethanol")),
    ("FLE", _("Flex")),
    ("ELE", _("Electric")),
)

VEHICLE_STATUS = (
    ("DIS", _("Available")),
    ("MAT", _("Maintenance")),
    ("USO", _("In Use")),
)

VEHICLE_FUEL_CHOICES = (
    ("DIE", _("Diesel")),
    ("GAS", _("Gasoline")),
    ("ETA", _("Ethanol")),
    ("FLE", _("Flex")),
    ("ELE", _("Electric")),
)

TRACTION_CHOICES = (
    ("N/A", "N/A"),
    ("4X2", "4x2"),
    ("4X4", "4x4"),
    ("6X2", "6x2"),
    ("6X4", "6x4"),
    ("8X2", "8x2"),
    ("8X4", "8x4"),
)

LOCOMOTION_CHOICES = (
    ("PN", _("Tire")),
    ("ES", _("Treadmill")),
)

FUEL_SITUATION_CHOICES = (
    ("0", "0"),
    ("1/4", "1/4"),
    ("1/2", "1/2"),
    ("3/4", "3/4"),
    ("1", "1"),
)

STATUS_VEHICLE_RELEASE = (
    ("AGE", _("Scheduled")),
    ("ROT", _("On Route")),
    ("FIN", _("Completed")),
)

STATUS_VEHICLE_SERVICE_ORDER = (
    ('ABE', _("Open")),
    ('EXE', _("In Progress")),
    ('ENC', _("Closed")),
)

STATUS_VEHICLE_SUPPLY_CHOICES = (
    ('SOL', _("Requested")),
    ('AUT', _("Authorized")),
    ('CON', _("Finished")),
)

MANIFEST_STATUS_CHOICES = (
    ("PRE", _("Pre-Released")),
    ("COL", _("Collected")),
    ("TRA", _("Treated")),
)

SCHEDULING_TYPE_CHOICES = (
    ("FI", _("Fixed")),
    ("FL", _("Flexible")),
)

DAY_MONTH_DAY_WEEK_CHOICES = (
    ("SEM", _("Week")),
    ("MES", _("Month")),
)

ADDENDUM_TYPE_CHOICES = (
    ("PRAZO", _("Term")),
    ("VALOR", _("Value")),
    ("ESCOPO", _("Scope")),
    ("QUANTIDADE", _("Quantity")),
)

TYPE_CHANGE_HISTORY_CHOICES = (
    ("FIS", _("Inspector")),
    ("COM", _("Component")),
)

TYPE_ACTION_HISTORY_CHOICES = (
    ("SUB", _("Replacement")),
    ("ADC", _("Added")),
    ("REM", _("Removed")),
)

REPLACEMENT_REASON_TYPE_CHOICES = (
    ("FER", _("Vacation")),
    ("SUB", _("Substitution")),
    ("RES", _("Resignation")),
    ("ATE", _("Temporary Absence")),
    ("ADM", _("Administrative")),
    ("OUT", _("Other")),
    ("N/A", _("N/A")),
)

JUSTIFICATION_TYPE_CHOICES = (
    ("ATE", _("Medical Certificate")),
    ("FOL", _("Work Break")),
    ("FER", _("Vacation")),
    ("FOC", _("Work Time Off Compensate")),
    ("OUT", _("Other")),
    ("N/A", _("N/A")),
)

TYPE_USER_CHOICES = (
    ("INT", _("Internal")),
    ("EXT", _("External")),
)

LEVEL_USER_CHOICES = (
    ("DEF", _("Default")),
    ("ADM", _("Admin")),
)

PERSONAL_SPECIALITY_CHOICES = (
    ('strength', _('Strength Training')),
    ('endurance', _('Endurance')),
    ('rehabilitation', _('Rehabilitation')),
    ('flexibility', _('Flexibility')),
    ('crossfit', _('CrossFit')),
    ('yoga', _('Yoga')),
    ('cardio', _('Cardio')),
    ('martialarts', _('Martial Arts')),
    ('other', _('Other')),
)

NUTRITIONIST_SPECIALTY_CHOICES = (
    ('clinical', _('Clinical Nutrition')),
    ('sports', _('Sports Nutrition')),
    ('pediatric', _('Pediatric Nutrition')),
    ('geriatric', _('Geriatric Nutrition')),
    ('dietary', _('Dietary Planning')),
    ('other', _('Other')),
)

BODY_PART_CHOICES = (
    ('chest', _('Chest')),
    ('back', _('Back')),
    ('shoulders', _('Shoulders')),
    ('arms', _('Arms')),
    ('legs', _('Legs')),
    ('other', _('Other')),
)

UNIVERSITY_DEGREE_CHOICES = (
    ('nutrition', _('Bachelor in Nutrition')),
    ('dietetics', _('Bachelor in Dietetics')),
    ('food_science', _('Bachelor in Food Science')),
    ('biomedicine', _('Bachelor in Biomedicine')),
    ('physical_education', _('Bachelor in Physical Education')),
    ('other', _('Other')),
)

BLOOD_TYPE_CHOICES = (
    ('A+', _('A+')),
    ('A-', _('A-')),
    ('B+', _('B+')),
    ('B-', _('B-')),
    ('AB+', _('AB+')),
    ('AB-', _('AB-')),
    ('O+', _('O+')),
    ('O-', _('O-')),
)

WORKOUT_INTAKE_ACTIVITY_LEVEL_CHOICES = (
    ('sedentary', _('Sedentary')),
    ('lightly_active', _('Lightly Active')),
    ('moderately_active', _('Moderately Active')),
    ('very_active', _('Very Active')),
    ('extra_active', _('Extra Active')),
)

CHRONIC_CONDITIONS_CHOICES = (
    ('hypertension', _('Hypertension')),
    ('diabetes', _('Diabetes')),
    ('heart_disease', _('Heart Disease')),
    ('asthma', _('Asthma')),
    ('high_colesterol', _('High Cholesterol')),
    ('kidney_disease', _('Kidney Disease')),
    ('osteoarthrosis', _('Osteoarthrosis')),
    ('other', _('Other')),
)


MEDICAL_RESTRICTIONS_CHOICES = (
    ('cardio_exercise', _('Cardio Exercise')),
    ('high_impact', _('High Impact Movements')),
    ('weight_lifting', _('Heavy Weight Lifting')),
    ('flexibility', _('Flexibility or Stretching')),
    ('balance', _('Balance Exercises')),
    ('respiratory_limit', _('Respiratory Limitations')),
    ('joint_pain', _('Joint Pain or Arthritis')),
    ('lower_back', _('Lower Back Issues')),
    ('knee_pain', _('Knee Problems')),
    ('shoulder_pain', _('Shoulder Restrictions')),
    ('neck_pain', _('Neck Limitations')),
    ('pregnancy', _('Pregnancy')),
    ('post_surgery', _('Post-Surgery Recovery')),
    ('hypertension', _('High Blood Pressure')),
    ('diabetes', _('Diabetes')),
    ('none', _('No Restrictions')),
)

SUPERIOR_INJURY_CHOICES = (
    ('shoulder', _('Shoulder')),
    ('elbow', _('Elbow')),
    ('wrist', _('Wrist')),
    ('none', _('None')),	
)

INFERIOR_INJURY_CHOICES = (
    ('hip', _('Hip')),
    ('knee', _('Knee')),
    ('ankle', _('Ankle')),
    ('none', _('None')),
)

CORE_INJURY_CHOICES = (
    ('cervical', _('Cervical')),
    ('lumbar', _('Lumbar')),
    ('core', _('Core')),
    ('none', _('None')),
)

WORKOUT_GOALS_CHOICES = (
    ('strength', _('Increase Strength')),
    ('endurance', _('Improve Muscular Endurance')),
    ('hypertrophy', _('Muscle Hypertrophy / Gain Muscle Mass')),
    ('weight_loss', _('Weight Loss / Fat Burning')),
    ('flexibility', _('Improve Flexibility')),
    ('balance', _('Enhance Balance and Coordination')),
    ('cardio', _('Improve Cardiovascular Health')),
    ('mobility', _('Increase Mobility')),
    ('performance', _('Sports Performance')),
    ('rehabilitation', _('Injury Rehabilitation')),
    ('general_health', _('General Health and Wellbeing')),
    ('other', _('Other')),
)

SECONDARY_GOALS_CHOICES = (
    ('posture', _('Improve Posture')),
    ('balance', _('Improve Balance')),
    ('cardio_conditioning', _('Improve Cardiovascular Conditioning')),
    ('flexibility', _('Increase Flexibility')),
    ('core_strength', _('Strengthen Core')),
    ('injury_recovery', _('Injury Recovery')),
)

INTENSITY_LEVEL_CHOICES = [(i, str(i)) for i in range(1, 11)]

TRAINING_DURATION_CHOICES = (
    ('1_month', _('1 Month')),
    ('3_months', _('3 Months')),
    ('6_months', _('6 Months')),
    ('1_year', _('1 Year')),
    ('long_term', _('Long Term')),
)

OCCUPATION_CHOICES = (
    ('sedentary_job', _('Sedentary Job (Office Work)')),
    ('moderate_activity_job', _('Job with Moderate Physical Activity')),
    ('physically_active_job', _('Physically Demanding Job')),
    ('student', _('Student')),
    ('retired', _('Retired')),
    ('other', _('Other')),
)

STRESS_LEVEL_CHOICES = (
    ('low', _('Low')),
    ('moderate', _('Moderate')),
    ('high', _('High')),
)

ALCOHOL_CONSUMPTION_CHOICES = (
('never', _('Never')),
('occasional', _('Occasional')),
('frequent', _('Frequent')),
)

PREFERRED_TIME_CHOICES = (
    ('morning', _('Morning')),
    ('afternoon', _('Afternoon')),
    ('evening', _('Evening')),
)

WEEK_DAYS_CHOICES = (
    ('mon', _('Monday')),
    ('tue', _('Tuesday')),
    ('wed', _('Wednesday')),
    ('thu', _('Thursday')),
    ('fri', _('Friday')),
    ('sat', _('Saturday')),
    ('sun', _('Sunday')),
)

NUTRITION_HABITS_CHOICES = (
    ('breakfast', _('Eats breakfast regularly')),
    ('regular_meals', _('Has meals at regular times')),
    ('protein', _('Consumes protein in all meals')),
    ('vegetables', _('Eats vegetables daily')),
    ('water', _('Drinks at least 2L of water per day')),
    ('supplements', _('Uses dietary supplements')),
)

PREFERRED_DURATION_CHOICES = (
    ('30', _('30 minutes')),
    ('45', _('45 minutes')),
    ('60', _('1 hour')),
    ('90', _('1.5 hours')),
)

TRAINING_LOCATION_CHOICES = (
    ('gym', _('Gym (Full Equipment)')),
    ('home', _('At Home (Limited Equipment or Bodyweight)')),
    ('outdoor', _('Outdoor (Parks, Public Areas)')),
    ('hybrid', _('Hybrid (Combination of Locations)')),
)

EXERCISE_PREFERENCES_CHOICES = (
    ('weight_training', _('Musculação')),
    ('functional_training', _('Treino funcional')),
    ('pilates', _('Pilates')),
    ('crossfit', _('CrossFit')),
    ('cardio', _('Cardio')),
    ('hiit', _('HIIT')),
    ('yoga', _('Yoga')),
    ('calisthenics', _('Calistenia')),
)

WEEKDAYS_CHOICES = [
    ("monday", "Segunda-feira"),
    ("tuesday", "Terça-feira"),
    ("wednesday", "Quarta-feira"),
    ("thursday", "Quinta-feira"),
    ("friday", "Sexta-feira"),
    ("saturday", "Sábado"),
    ("sunday", "Domingo"),
]

BODY_PART_CHOICES = [
    ("chest", "Peito"),
    ("back", "Costas"),
    ("legs", "Pernas"),
    ("arms", "Braços"),
    ("shoulders", "Ombros"),
    ("core", "Core"),
    ("full_body", "Corpo inteiro"),
]

DAY_OF_WEEK_CHOICES = (
    ("MON", _("Monday")),
    ("TUE", _("Tuesday")),
    ("WED", _("Wednesday")),
    ("THU", _("Thursday")),
    ("FRI", _("Friday")),
    ("SAT", _("Saturday")),
    ("SUN", _("Sunday")),
)

WORKOUT_STATUS_CHOICES = [
    ("pending", "Pendente"),
    ("accepted", "Aceito"),
    ("refused", "Recusado"),
]

PROFILE_TYPE_CHOICES = [
    ("TRAINER", "Treinador"),
    ("STUDENT", "Aluno"),
    ("NUTRITIONIST", "Nutricionista"),
    ("ADMIN", "Admin"),
]

STATUS_CHOICES = [
    ("PENDING", "Pendente"),
    ("ACCEPTED", "Aceita"),
    ("REJECTED", "Recusada"),
]

REQUESTED_BY_CHOICES = [
    ("STUDENT", "Aluno"),
    ("TRAINER", "Personal"),
]

LEVEL_CHOICES = [
    ("BEGINNER", "Iniciante"),
    ("INTERMEDIATE", "Intermediário"),
    ("ADVANCED", "Avançado"),
]
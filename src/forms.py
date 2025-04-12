from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    SelectField,
    BooleanField,
    FloatField,
    IntegerField,
    TimeField,
    SubmitField,
    RadioField,
)
from wtforms.validators import InputRequired, Optional, Length, NumberRange

OBSERVER_CHOICES = [
    ("", "-- Select Observer --"),
    ("Dr Abraham Phillips", "Dr Abraham Phillips"),
    ("Dr Navina Jayabalan", "Dr Navina Jayabalan"),
    ("Dr Sharwind Supermanian", "Dr Sharwind Supermanian"),
]

CARDIAC_RHYTHM_CHOICES = [
    ("", "-- Select Rhythm --"),
    ("Sinus Rhythm", "Sinus Rhythm"),
    ("Sinus Bradycardia", "Sinus Bradycardia"),
    ("Second Degree Heart block", "Second Degree Heart block"),
    ("Third Degree Heart block", "Third Degree Heart block"),
    ("Sinus Tachycardia", "Sinus Tachycardia"),
    ("Atrial Fibrillation", "Atrial Fibrillation"),
    ("Atrial Flutter", "Atrial Flutter"),
    ("Paced", "Paced"),
]

CVC_LOCATION_CHOICES = [
    ("", "-- Select Location --"),
    ("L) IJ", "L) IJ"),
    ("R) IJ", "R) IJ"),
    ("L) SCV", "L) SCV"),
    ("R) SCV", "R) SCV"),
    ("L) PICC", "L) PICC"),
    ("R) PICC", "R) PICC"),
]


class RecordForm(FlaskForm):


    # Patient Info
    patient_ur = StringField(
        "Patient UR No", validators=[InputRequired(), Length(max=80)]
    )
    patient_serial = StringField(
        "Patient's Serial Number", validators=[InputRequired(), Length(max=80)]
    )
    collection_date = DateField(
        "Date of Data Collection", validators=[InputRequired()], format="%Y-%m-%d"
    )
    observer = SelectField(
        "Observer", choices=OBSERVER_CHOICES, validators=[InputRequired()]
    )  
    check_head_of_bed = BooleanField("Head of Bed 30 degrees", validators=[InputRequired()])
    check_transducer_level = BooleanField("Transducer leveled and zeroed", validators=[InputRequired()])
    height_cm = FloatField("Height (cm)", validators=[InputRequired(), NumberRange(min=0)])
    weight_kg = FloatField("Weight (kg)", validators=[InputRequired(), NumberRange(min=0)])
    bsa = FloatField("BSA (m²)", validators=[Optional(), NumberRange(min=0)])



    # Current Patient Treatment
    ventilation = RadioField(
        "Ventilation",
        choices=[
            ("spontaneous", "Spontaneous Ventilation"),
            ("invasive", "Invasive Ventilation"),
            ("noninvasive", "Non-Invasive Ventilation"),
        ],
        validators=[InputRequired()]
    )
    peep = FloatField("PEEP", validators=[InputRequired(), NumberRange(min=0)])



    # Medicaitons
    medication_aramine = BooleanField("Aramine")
    medication_noradrenaline = BooleanField("Noradrenaline")
    medication_adrenaline = BooleanField("Adrenaline")
    medication_gtn = BooleanField("GTN")
    medication_milrinone = BooleanField("Milrinone")
    medication_isoprenaline = BooleanField("Isoprenaline")
    medication_dobutamine = BooleanField("Dobutamine")



    # Observations
    cardiac_rhythm = SelectField(
        "Cardiac Rhythm", choices=CARDIAC_RHYTHM_CHOICES, validators=[InputRequired()]
    )
    cvc_location = SelectField(
        "CVC Location", choices=CVC_LOCATION_CHOICES, validators=[InputRequired()]
    )
    jvp_height_cm = FloatField(
        "JVP height (cm)", validators=[InputRequired(), NumberRange(min=0)]
    )
    photograph_taken = BooleanField("Photograph with ruler and patient SN, taken", validators=[InputRequired()])



    # Echo Measurements
    echo_start_time = TimeField(
        "ECHO START TIME", validators=[InputRequired()], format="%H:%M"
    )
    echo_completion_time = TimeField(
        "ECHO COMPLETION TIME", validators=[InputRequired()], format="%H:%M"
    )
    echo_total_time_min = IntegerField(
        "Total Time (min)", validators=[Optional(), NumberRange(min=0)]
    )

    ivc_diameter_cm = FloatField(
        "IVC diameter (2cm from IVC-RA junction) (cm)",
        validators=[Optional(), NumberRange(min=0)],
    )
    systemic_venous_flow_velocity_mps = FloatField(
        "Systemic venous flow velocity (m/sec)",
        validators=[Optional(), NumberRange(min=0)],
    )
    tricuspid_valve_doppler_inflow_mps = FloatField(
        "Tricuspid valve Doppler inflow (m/sec)",
        validators=[Optional(), NumberRange(min=0)],
    )
    tr_max_mps = FloatField(
        "TR Max (M/sec)", validators=[Optional(), NumberRange(min=0)]
    )
    tr_peak_gradient_mmhg = FloatField(
        "TR peak gradient (mm Hg)", validators=[Optional(), NumberRange(min=0)]
    )
    rap_mmhg = FloatField("RAP (mm Hg)", validators=[Optional(), NumberRange(min=0)])
    rvsp_mmhg = FloatField("RVSP (mm Hg)", validators=[Optional(), NumberRange(min=0)])
    vti_cm = FloatField("VTI (cm)", validators=[Optional(), NumberRange(min=0)])

    e_velocity_mps = FloatField(
        "E velocity (M/sec)", validators=[Optional(), NumberRange(min=0)]
    )
    a_velocity_mps = FloatField(
        "A velocity (M/sec)", validators=[Optional(), NumberRange(min=0)]
    )
    mean_gradient_mmhg = FloatField(
        "Mean Gradient (mmHg)", validators=[Optional(), NumberRange(min=0)]
    )
    dt_mps = FloatField(
        "DT (M/sec)", validators=[Optional(), NumberRange(min=0)]
    )  # Deceleration Time
    pht_mps = FloatField(
        "PHT (M/sec)", validators=[Optional(), NumberRange(min=0)]
    )  # Pressure Half-Time
    tva_cont_cm2 = FloatField(
        "TVA (cont) (Cm2)", validators=[Optional(), NumberRange(min=0)]
    )  # Tricuspid Valve Area
    rsv_prime = FloatField(
        "RSV'", validators=[Optional(), NumberRange(min=0)]
    )  # Assuming numeric, unit unclear
    tev_prime = FloatField(
        "TEV'", validators=[Optional(), NumberRange(min=0)]
    )  # Assuming numeric, unit unclear



    # Heamodynamics
    hr = IntegerField("HR", validators=[Optional(), NumberRange(min=0)])
    sys_bp_mmhg = IntegerField(
        "Sys BP (mmHg)", validators=[Optional(), NumberRange(min=0)]
    )
    dia_bp_mmhg = IntegerField(
        "Dia BP (mmHg)", validators=[Optional(), NumberRange(min=0)]
    )
    map_bp_mmhg = IntegerField(
        "Map BP (mmHg)", validators=[Optional(), NumberRange(min=0)]
    )
    cvp_mmhg = IntegerField("CVP (mmHg)", validators=[Optional(), NumberRange(min=0)])
    pulse_pressure_variation_mmhg = FloatField(
        "Pulse Pressure Variation (mmHg)", validators=[Optional(), NumberRange(min=0)]
    )



    submit = SubmitField("Save Record")

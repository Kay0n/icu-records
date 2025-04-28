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

class UnitFloatField(FloatField):
    def __init__(self, label=None, validators=None, unit=None, **kwargs):
        self.unit = unit
        super().__init__(label=label, validators=validators, **kwargs)

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
    patient_ur = IntegerField(
        "Patient UR No", validators=[InputRequired()]
    )
    patient_serial = IntegerField(
        "Patient's Serial Number", validators=[InputRequired()]
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
    peep = FloatField("PEEP", validators=[Optional(), NumberRange(min=0)])



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


    ivc_diameter_cm = UnitFloatField(
        "IVC diameter (2cm from IVC-RA junction)",
        unit="cm",
        validators=[InputRequired(), NumberRange(min=0)],
    )
    systemic_venous_flow_velocity_mps = UnitFloatField(
        "Systemic venous flow velocity",
        unit="cm/sec",
        validators=[InputRequired(), NumberRange(min=0)],
    )
    tricuspid_valve_doppler_inflow_mps = UnitFloatField(
        "Tricuspid valve Doppler inflow",
        unit="cm/sec",
        validators=[InputRequired(), NumberRange(min=0)],
    )
    tr_max_mps = UnitFloatField(
        "TR Max",
        unit="m/sec",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    tr_peak_gradient_mmhg = UnitFloatField(
        "TR peak gradient",
        unit="mmHg",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    rap_mmhg = UnitFloatField(
        "RAP",
        unit="mmHg",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    rvsp_mmhg = UnitFloatField(
        "RVSP",
        unit="mmHg",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    vti_cm = UnitFloatField(
        "VTI",
        unit="cm",
        validators=[InputRequired(), NumberRange(min=0)]
    )

    e_velocity_mps = UnitFloatField(
        "E velocity",
        unit="m/sec",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    a_velocity_mps = UnitFloatField(
        "A velocity",
        unit="m/sec",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    mean_gradient_mmhg = UnitFloatField(
        "Mean Gradient",
        unit="mmHg",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    dt_mps = UnitFloatField(
        "DT",
        unit="m/sec",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    pht_mps = UnitFloatField(
        "PHT",
        unit="m/sec",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    tva_cont_cm2 = UnitFloatField(
        "TVA (cont)",
        unit="cm²",
        validators=[InputRequired(), NumberRange(min=0)]
    )

    rsv_prime = FloatField(
        "RSV'",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    tev_prime = FloatField(
        "TEV'",
        validators=[InputRequired(), NumberRange(min=0)]
    )



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

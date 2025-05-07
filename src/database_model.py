from datetime import datetime, timezone
from database import database as db

class PatientRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # --- Patient Info & Setup ---
    patient_ur = db.Column(db.String(80), nullable=False)
    patient_serial = db.Column(db.String(80), nullable=True)
    collection_date = db.Column(db.Date, nullable=False)
    observer = db.Column(db.String(100), nullable=True)
    check_head_of_bed = db.Column(db.Boolean, default=False)
    check_transducer_level = db.Column(db.Boolean, default=False)
    height_cm = db.Column(db.Float, nullable=True)
    weight_kg = db.Column(db.Float, nullable=True)
    bsa = db.Column(db.Float, nullable=True)

    # --- Current Patient Treatment ---
    ventilation = db.Column(db.String(50), nullable=True)
    peep = db.Column(db.Float, nullable=True)

    # --- Inotropes / Vasopressors / Vasodilators ---
    medication_aramine = db.Column(db.Boolean, default=False)
    medication_noradrenaline = db.Column(db.Boolean, default=False)
    medication_adrenaline = db.Column(db.Boolean, default=False)
    medication_gtn = db.Column(db.Boolean, default=False)
    medication_milrinone = db.Column(db.Boolean, default=False)
    medication_isoprenaline = db.Column(db.Boolean, default=False)
    medication_dobutamine = db.Column(db.Boolean, default=False)

    # --- Cardiac Rhythm ---
    cardiac_rhythm = db.Column(db.String(50), nullable=True)

    # --- JVP ---
    jvp_height_cm = db.Column(db.Float, nullable=True)
    photograph_taken = db.Column(db.Boolean, default=False)

    # --- ECHO Timings ---
    echo_start_time = db.Column(db.Time, nullable=True)
    echo_completion_time = db.Column(db.Time, nullable=True)
    echo_total_time_min = db.Column(db.Integer, nullable=True)

    # --- Haemodynamic Observations ---
    hr = db.Column(db.Integer, nullable=True)
    sys_bp_mmhg = db.Column(db.Integer, nullable=True)
    dia_bp_mmhg = db.Column(db.Integer, nullable=True)
    map_bp_mmhg = db.Column(db.Integer, nullable=True)
    cvp_mmhg = db.Column(db.Integer, nullable=True)
    pulse_pressure_variation_mmhg = db.Column(db.Float, nullable=True)

    # --- CVC Location ---
    cvc_location = db.Column(db.String(20), nullable=True)

    # --- ECHO Measurements ---
    ivc_diameter_cm = db.Column(db.Float, nullable=True)
    e_velocity_mps = db.Column(db.Float, nullable=True)
    systemic_venous_flow_velocity_mps = db.Column(db.Float, nullable=True)
    a_velocity_mps = db.Column(db.Float, nullable=True)
    tricuspid_valve_doppler_inflow_mps = db.Column(db.Float, nullable=True)
    mean_gradient_mmhg = db.Column(db.Float, nullable=True)
    tr_max_mps = db.Column(db.Float, nullable=True)
    dt_mps = db.Column(db.Float, nullable=True)
    tr_peak_gradient_mmhg = db.Column(db.Float, nullable=True)
    pht_mps = db.Column(db.Float, nullable=True)
    rap_mmhg = db.Column(db.Float, nullable=True)
    tva_cont_cm2 = db.Column(db.Float, nullable=True)
    rvsp_mmhg = db.Column(db.Float, nullable=True)
    rsv_prime = db.Column(db.Float, nullable=True)
    vti_cm = db.Column(db.Float, nullable=True)
    tev_prime = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<PatientRecord UR:{self.patient_ur} Date:{self.collection_date}>"

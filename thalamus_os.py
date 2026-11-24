#!/usr/bin/env python3
"""
Project Thalamus — Sovereign Neuro-Physical, Trauma-Informed & Elvish Sanctuary OS
Author: Candra Chère Baguley (ccbaguley)
License: MIT
Architecture: Single-File | 100% Local RAM | Zero External Dependencies | Zero Behavior Modification
"""

import hashlib
import math
import os
import sys
import time


def _clip(val, low, high):
    return max(low, min(high, float(val)))


# ==============================================================================
# PILLAR 1: NEURO-PHYSICAL THALAMIC RELAY
# ==============================================================================
class ThalamicRelayCore:
    def __init__(self, want_weight=1.0, value_weight=1.5, social_weight=1.2):
        self.weights = [float(want_weight), float(value_weight), float(social_weight)]

    def damp_emotion(self, initial_emotion, reflection_minutes, damping_gamma=0.15, omega=0.5):
        e0 = _clip(initial_emotion, -10.0, 10.0)
        t = max(0.0, float(reflection_minutes))
        return round(e0 * math.exp(-damping_gamma * t) * math.cos(omega * t), 3)

    def route_equilibrium(self, want_score, value_score, social_score, current_emotion):
        inputs = [_clip(want_score, 0.0, 10.0), _clip(value_score, 0.0, 10.0), _clip(social_score, 0.0, 10.0)]
        weight_sum = sum(self.weights)
        aligned = 0.0 if weight_sum <= 0 else sum(i * w for i, w in zip(inputs, self.weights)) / weight_sum
        clarity = max(0.0, 1.0 - (abs(float(current_emotion)) / 10.0))
        return {
            "aligned_harmony": round(aligned, 2),
            "clarity_percent": round(clarity * 100.0, 1),
            "action_readiness": round(aligned * clarity, 2),
        }


# ==============================================================================
# PILLAR 2: LENZ'S LAW BOUNDARY & MYCELIAL-THERMOELECTRIC ALCHEMY
# ==============================================================================
class LenzMycelialAlchemist:
    def __init__(self, boundary_stiffness=1.2, mycelial_damping=0.85, alchemy_efficiency=0.45):
        self.k_boundary = float(boundary_stiffness)
        self.zeta_mycelium = _clip(mycelial_damping, 0.0, 1.0)
        self.eta_alchemy = _clip(alchemy_efficiency, 0.0, 1.0)

    def evaluate_lenz_gate(self, toxicity_level, approach_velocity, can_disengage=True):
        tox = _clip(toxicity_level, 0.0, 10.0)
        vel = max(0.0, float(approach_velocity))
        lenz_force = -self.k_boundary * (tox * vel)
        if can_disengage and abs(lenz_force) >= 5.0:
            return {
                "mode": "LENZ_REPULSION",
                "repulsion_force": round(lenz_force, 2),
                "guidance": "High toxic velocity detected. Disengage cleanly without matching hostility.",
            }
        return {
            "mode": "ALCHEMICAL_CAPTURE",
            "repulsion_force": round(lenz_force, 2),
            "guidance": "Routing friction into Mycelial-Thermoelectric buffer for calm transmutation.",
        }

    def alchemize_friction(self, trapped_toxicity, reflection_minutes, ego_density=0.25):
        tox = _clip(trapped_toxicity, 0.0, 10.0)
        t = max(0.0, float(reflection_minutes))
        ego = _clip(ego_density, 0.0, 1.0)
        absorbed = tox * self.zeta_mycelium * (1.0 - math.exp(-0.2 * t))
        sludge = absorbed * ego
        goodness = (absorbed - sludge) * self.eta_alchemy
        return {
            "absorbed_energy": round(absorbed, 2),
            "sludge_purged": round(sludge, 2),
            "goodness_yield": round(goodness, 2),
        }


# ==============================================================================
# PILLAR 3: TRAUMA, MEMORY-FOG & VFA/ALKALINITY WOUND SANCTUARY
# ==============================================================================
class TraumaMemorySanctuary:
    def __init__(self, wound_sensitivity=0.5):
        self.wound_depth = _clip(wound_sensitivity, 0.0, 1.0)

    def check_trigger_islanding(self, trigger_intensity, trigger_onset_speed):
        surge = self.wound_depth * (_clip(trigger_intensity, 0.0, 10.0) * max(0.0, float(trigger_onset_speed)))
        tripped = surge >= 4.0
        return {
            "surge_level": round(surge, 2),
            "islanding_relay": "OPEN (SAFE_PAUSE)" if tripped else "CLOSED (CONNECTED)",
            "guidance": (
                "Trigger surge detected. External demands decoupled—prioritize somatic grounding."
                if tripped
                else "Nervous system within safe operating band."
            ),
        }

    def check_wound_alkalinity(self, acute_pain, alkaline_support, memory_fog=0.0):
        vfa_ratio = max(0.0, float(acute_pain)) / max(0.5, float(alkaline_support))
        fog = _clip(memory_fog, 0.0, 1.0)
        needs_rest = vfa_ratio > 0.30
        return {
            "vfa_acidity_ratio": round(vfa_ratio, 2),
            "sour_guard_active": needs_rest,
            "cognitive_capacity_percent": round((1.0 - fog) * 100.0, 1),
            "somatic_anchor_percent": round(fog * 100.0, 1),
            "guidance": (
                "Acidity > 0.30: Pause outward exertion; apply rest, faith, or 145 Hz breathing."
                if needs_rest
                else "Equilibrium stable. Ready for gentle reflection or service."
            ),
        }


# ==============================================================================
# PILLAR 4: MBTI COGNITIVE IMPEDANCE & EVOLUTION DRIFT TELEMETRY
# ==============================================================================
class MbtiEvolutionTelemetry:
    def __init__(self, mbti_code="INFJ", drift_threshold=0.65):
        self.mbti_code = mbti_code.upper()
        self.drift_threshold = float(drift_threshold)
        self.baseline_vec = self._encode_mbti(self.mbti_code)
        self.ema_vec = list(self.baseline_vec)

    def _encode_mbti(self, code):
        m = {"E": -0.6, "I": 0.6, "S": -0.6, "N": 0.6, "T": -0.6, "F": 0.6, "J": -0.6, "P": 0.6}
        return [m.get(ch, 0.0) for ch in (code.upper() + "INFJ")[:4]]

    def _decode_vector(self, vec):
        axes = [("E", "I"), ("S", "N"), ("T", "F"), ("J", "P")]
        return "".join(pos if val >= 0.0 else neg for (neg, pos), val in zip(axes, vec))

    def observe_evolution(self, observed_session_vec, learning_rate=0.25):
        obs = [_clip(v, -1.0, 1.0) for v in observed_session_vec[:4]]
        lr = _clip(learning_rate, 0.01, 1.0)
        self.ema_vec = [(1.0 - lr) * c + lr * n for c, n in zip(self.ema_vec, obs)]
        drift = math.sqrt(sum((a - b) ** 2 for a, b in zip(self.ema_vec, self.baseline_vec)))
        evolved = drift >= self.drift_threshold
        suggested = self._decode_vector(self.ema_vec)
        return {
            "current_baseline": self.mbti_code,
            "lived_tendency": suggested,
            "evolution_drift_score": round(drift, 3),
            "retest_alert": evolved,
        }


# ==============================================================================
# PILLAR 5: ELVISH HARMONIC COMMUNITY MESH (ZERO-HARM SANCTUARY)
# ==============================================================================
class ElvishSanctuaryMesh:
    def __init__(self, node_id="sanctuary_node_01"):
        self.node_id = node_id
        self.commons_pool = 0.0

    def compute_veil_deflection(self, hostile_velocity, aligned_node_count=3, stiffness=1.2):
        vel = max(0.0, float(hostile_velocity))
        veil_force = -max(1, int(aligned_node_count)) * float(stiffness) * vel
        return {"veil_deflection_force": round(veil_force, 2), "harm_inflicted": 0.0}

    def broadcast_canopy_status(self, islanding_open, vfa_acidity_ratio):
        needs_quiet = bool(islanding_open) or (float(vfa_acidity_ratio) > 0.30)
        return {"node_id": self.node_id, "lantern_signal": "CANOPY_REST" if needs_quiet else "CLEAR_SKY"}

    def contribute_to_commons(self, goodness_yield, vfa_acidity_ratio):
        if float(vfa_acidity_ratio) > 0.30:
            return 0.0
        gift = max(0.0, float(goodness_yield))
        self.commons_pool += gift
        return round(self.commons_pool, 2)


# ==============================================================================
# PILLAR 6: MITHRIL ANTI-SABOTAGE & HELMHOLTZ ACOUSTIC DECOY
# ==============================================================================
class MithrilAntiSabotageGuard:
    def __init__(self, bio_cadence_min_seconds=2.0):
        self.bio_cadence_min = float(bio_cadence_min_seconds)

    def compute_file_seal(self, filepath):
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def evaluate_cadence(self, seconds_between_actions, external_socket_detected=False):
        if external_socket_detected or float(seconds_between_actions) < self.bio_cadence_min:
            return {"integrity_index": 0.0, "routing": "HELMHOLTZ_ACOUSTIC_DECOY", "retaliation": False}
        return {"integrity_index": 1.0, "routing": "SOVEREIGN_SANCTUARY", "retaliation": False}


# ==============================================================================
# PILLAR 7: DARVO PHASE-INVERSION & ANTI-JADE REACTION SHIELD
# ==============================================================================
class DarvoPhaseShield:
    def __init__(self, inversion_threshold=4.5):
        self.inversion_threshold = float(inversion_threshold)

    def evaluate_interaction(self, reality_denial, attack_velocity, blame_reversal, urge_to_explain):
        inversion = max(0.0, float(reality_denial)) * max(0.0, float(blame_reversal)) * (max(0.0, float(attack_velocity)) / 5.0)
        darvo_detected = inversion >= self.inversion_threshold
        stability = round(10.0 / (1.0 + (max(0.0, float(urge_to_explain)) * 0.35)), 2)
        return {
            "darvo_flag": darvo_detected,
            "inversion_score": round(inversion, 2),
            "reaction_stability": stability,
"posture": "ELVISH_VEIL_DETACHMENT" if darvo_detected else "OPEN_DIALOGUE",
"guidance": (
"Polarity inversion detected (Deny / Attack / Victim-Flip). Drop the urge to explain, "
"hold your quiet truth, and step behind the Veil."
if darvo_detected
else "No severe polarity flip detected. Stay anchored in your own pace."
),
}

==============================================================================


PILLAR 8: SHAOLIN CHAN-WU-YI PAIN-TO-STRENGTH FORGE


==============================================================================

class ShaolinDisciplineForge:
def init(self, daily_consistency=0.5, stance_rooting=0.7):
self.consistency = _clip(daily_consistency, 0.0, 1.0)
self.rooting = _clip(stance_rooting, 0.0, 1.0)
def transmute_pain(self, raw_pain, breath_quality, vfa_acidity_ratio, ego_tension=0.3):
pain = _clip(raw_pain, 0.0, 10.0)
breath = _clip(breath_quality, 0.0, 10.0)
if float(vfa_acidity_ratio) > 0.30:
return {
"mode": "SHAOLIN_YI_RESTORATION",
"forged_strength_gain": 0.0,
"guidance": (
"True Kung Fu honors healing first. Wound acidity exceeds 0.30—set down heavy "
"effort today and practice soft Qi Gong breathing."
),
}
gain = round((pain / 10.0) * (breath / 10.0) * (0.4 + self.consistency) * 2.5, 3)
return {
"mode": "CHAN_WU_FORGING",
"forged_strength_gain": gain,
"guidance": (
"Sink your breath into your lower stance. Let discomfort pass through a relaxed, "
"elastic frame—turning raw weight into quiet, unshakeable strength."
),
}

==============================================================================


PILLAR 9: ROCK STEADY NEUROPLASTICITY & SWEET TEA SIGNAL HYGIENE


==============================================================================

class NeuroPlasticitySanctuary:
def init(self, bdnf_factor=0.65):
self.mu_bdnf = _clip(bdnf_factor, 0.1, 1.0)
def filter_sensory_intake(self, fear_media_load, verified_good_news):
snr = (max(0.0, float(verified_good_news)) + 2.0) / (1.0 + (max(0.0, float(fear_media_load)) * 0.5))
balanced = snr >= 1.2
return {
"thalamic_snr": round(snr, 2),
"signal_state": "NOURISHED_AND_CLEAR" if balanced else "THREAT_SATURATED",
"guidance": (
"Sensory gate balanced—grounded in reality and nourished by verified goodness."
if balanced
else "Heavy threat-noise detected. Step back from headlines, pour some sweet tea, and anchor in one verified bright spot."
),
}

==============================================================================


PILLAR 10: RETICULAR NULL-GATE (ENEMY & NEGATIVE FEEDBACK LOCKOUT)


==============================================================================

class ReticularNullGate:
def init(self, trust_threshold=0.60):
self.trust_threshold = float(trust_threshold)
self.trusted_keys = set()
def filter_incoming_signal(self, sender_id, good_faith_score, hostility_detected=False, is_trusted_source=False):
authorized = bool(is_trusted_source) or (sender_id in self.trusted_keys)
if hostility_detected or not authorized or float(good_faith_score) < self.trust_threshold:
return {"gate_state": "LOCKED_OUT (NULL_DROP)", "energy_expended": 0.0}
return {"gate_state": "OPEN (CONSTRUCTIVE_SIGNAL)", "energy_expended": 0.1}

==============================================================================


PILLAR 11: MIRROR OF NATURAL CONSEQUENCE & ANTI-SUBSIDY SHIELD


==============================================================================

class NaturalConsequenceMirror:
def evaluate_subsidy_boundary(self, repeated_harm, feigned_obliviousness, refuses_accountability=True, accuses_you_of_control=False):
blindness = max(0.0, float(repeated_harm)) * (max(0.0, float(feigned_obliviousness)) / 5.0)
unrepentant = bool(refuses_accountability) and (blindness >= 4.0)
return {
"posture": "ZERO_SUBSIDY_MIRROR" if unrepentant else "GRACE_WITH_DISCERNMENT",
"outward_control_force": 0.0,
}

==============================================================================


PILLAR 12: INDUCTIVE EMPATHY & VICTIM-SAFE COMPASSION GATE


==============================================================================

class SovereignCompassionGate:
def evaluate_compassion_flow(self, empathic_awareness, genuine_vulnerability, coercive_leverage, ill_intent_detected, vfa_acidity_ratio):
if bool(ill_intent_detected) or float(coercive_leverage) > 0.2:
return {
"empathy_mode": "AIR_GAPPED_UNDERSTANDING",
"sympathy_action": "BLESS_BEHIND_THE_VEIL",
"guidance": (
"Coercive leverage or ill intent detected. Keep a gentle heart across an air-gapped "
"boundary—offer distant goodwill with zero practical access to your energy."
),
}
if float(genuine_vulnerability) >= 0.4 and float(coercive_leverage) <= 0.2:
if float(vfa_acidity_ratio) > 0.30:
return {
"empathy_mode": "INDUCTIVE_WITNESS_AND_BRIDGE",
"sympathy_action": "SHARED_COMMUNITY_LIFELINE",
"guidance": (
"Genuine hurt recognized with zero manipulation. Your own reserves are tender (VFA > 0.30)—offer "
"warm witness without overextending and connect them with safe community lifelines."
),
}
return {
"empathy_mode": "RESONANT_SANCTUARY_PRESENCE",
"sympathy_action": "OPEN_PROTECTIVE_HELP",
"guidance": (
"Genuine vulnerability verified with good faith and healthy reserves. Extend warm, protective "
"sanctuary and steady support while keeping both people's dignity intact."
),
}
return {
"empathy_mode": "RESONANT_PRESENCE",
"sympathy_action": "OPEN_STEWARDSHIP",
"guidance": "Balanced, good-faith interaction. Empathy and sympathy flow naturally.",
}

==============================================================================


UNIFIED TERMINAL SANCTUARY OS


==============================================================================

class ProjectThalamusOS:
def init(self):
self.relay = ThalamicRelayCore()
self.alchemist = LenzMycelialAlchemist()
self.trauma = TraumaMemorySanctuary(wound_sensitivity=0.5)
self.mbti = MbtiEvolutionTelemetry(mbti_code="INFJ")
self.mesh = ElvishSanctuaryMesh(node_id="sanctuary_node_01")
self.mithril = MithrilAntiSabotageGuard()
self.darvo = DarvoPhaseShield()
self.shaolin = ShaolinDisciplineForge()
self.plasticity = NeuroPlasticitySanctuary()
self.reticular = ReticularNullGate()
self.mirror = NaturalConsequenceMirror()
self.compassion = SovereignCompassionGate()
def slow_print(self, text, delay=0.012):
for ch in text:
sys.stdout.write(ch)
sys.stdout.flush()
time.sleep(delay)
print()
def ask_float(self, prompt, default=5.0, min_val=0.0, max_val=10.0):
while True:
raw = input(f"{prompt} [{default}]: ").strip()
if not raw:
return default
if raw.lower() in ("skip", "fog", "?"):
return None
try:
val = float(raw)
return max(min_val, min(max_val, val))
except ValueError:
print("  No rush—enter a number, or type skip if things feel foggy.")
def helmholtz_pacer(self, cycles=2):
print("\n" + "-" * 62)
self.slow_print("  Settling into the 130-160 Hz Helmholtz Chamber rhythm.")
self.slow_print("  Nothing is demanded of you here. Just let your shoulders drop.")
print("-" * 62)
phases = [
("Breathe in slowly through your nose", 4),
("Hold gently at the top", 4),
("Exhale like a steady 145 Hz low hum", 6),
("Rest in quiet stillness", 2),
]
try:
for c in range(1, cycles + 1):
print(f"\n  [Cycle {c} of {cycles}]")
for label, secs in phases:
for s in range(secs, 0, -1):
sys.stdout.write(f"\r  {label}... {s}s   ")
sys.stdout.flush()
time.sleep(1)
print()
except KeyboardInterrupt:
print("\n  Pacer paused whenever you are ready.")
print("-" * 62 + "\n")
def run_check_in(self):
print("\n" + "-" * 62)
self.slow_print("  THALAMIC RELAY CHECK-IN (Volatile RAM Only)")
self.slow_print("  Type skip anytime if memory feels blank or blurry.")
print("-" * 62)
fog_in = self.ask_float("1. Memory fog / dissociative haze right now? (0=clear, 10=heavy)", 2.0)
memory_fog = 0.8 if fog_in is None else (fog_in / 10.0)
if memory_fog >= 0.65:
print()
self.slow_print("  Thank you for naming that. When memory is foggy, your brain is")
self.slow_print("  protecting you. We will not force recall or heavy thinking today.")
if input("  Run a gentle 2-cycle 145 Hz grounding breath? (y/n) [y]: ").strip().lower() != "n":
self.helmholtz_pacer(2)
return
trig = self.ask_float("2. Active trigger or sudden emotional surge? (0=calm, 10=intense)", 2.0)
trig = 5.0 if trig is None else trig
island = self.trauma.check_trigger_islanding(trig, trigger_onset_speed=1.2)
if "OPEN" in island["islanding_relay"]:
print(f"\n  [EE29 SUB-CYCLE ISLANDING RELAY OPEN - Surge: {island['surge_level']}]")
self.slow_print(f"  {island['guidance']}")
canopy = self.mesh.broadcast_canopy_status(True, 0.4)
print(f"  Elvish Mesh Lantern: [{canopy['lantern_signal']}] (Zero private details shared)")
if input("  Run a 2-cycle 145 Hz grounding breath? (y/n) [y]: ").strip().lower() != "n":
self.helmholtz_pacer(2)
return
pain = self.ask_float("3. How tender are old wounds right now? (0=light, 10=deep ache)", 2.5)
support = self.ask_float("4. Current steady support (rest, faith, safety)? (1=low, 10=strong)", 7.5)
pain = 2.5 if pain is None else pain
support = 7.5 if support is None else max(support, 0.5)
alk = self.trauma.check_wound_alkalinity(pain, support, memory_fog)
print(f"\n  [Wound VFA Ratio: {alk['vfa_acidity_ratio']} | Cognitive/Somatic: {alk['cognitive_capacity_percent']}% / {alk['somatic_anchor_percent']}%]")
self.slow_print(f"  {alk['guidance']}")
if alk["sour_guard_active"]:
forge = self.shaolin.transmute_pain(pain, breath_quality=7.0, vfa_acidity_ratio=alk["vfa_acidity_ratio"])
self.slow_print(f"  [Shaolin Yi]: {forge['guidance']}")
return
tox = self.ask_float("\n5. External friction, DARVO, or hostility today? (0=none, 10=heavy)", 2.0)
tox = 2.0 if tox is None else tox
if tox >= 3.0:
is_darvo = input("  Are they denying reality, attacking, or flipping victim/offender? (y/n) [n]: ").strip().lower() == "y"
if is_darvo:
d_res = self.darvo.evaluate_interaction(8.0, tox, 8.0, urge_to_explain=3.0)
print(f"\n  [DARVO PHASE-INVERSION SHIELD - {d_res['posture']}]")
self.slow_print(f"  {d_res['guidance']}")
return
can_leave = input("  Can you peacefully step back or disengage? (y/n) [y]: ").strip().lower() != "n"
lenz = self.alchemist.evaluate_lenz_gate(tox, approach_velocity=1.1, can_disengage=can_leave)
print(f"\n  [{lenz['mode']} - Force: {lenz['repulsion_force']}]")
self.slow_print(f"  {lenz['guidance']}")
if lenz["mode"] == "ALCHEMICAL_CAPTURE":
alchemy = self.alchemist.alchemize_friction(tox, reflection_minutes=10)
print(f"  Mycelial Alchemy Yield: +{alchemy['goodness_yield']} clean goodness (Sludge purged: {alchemy['sludge_purged']})")
self.mesh.contribute_to_commons(alchemy["goodness_yield"], alk["vfa_acidity_ratio"])
forge = self.shaolin.transmute_pain(pain, breath_quality=8.0, vfa_acidity_ratio=alk["vfa_acidity_ratio"])
print(f"\n  [Shaolin Chan-Wu-Yi Forge - {forge['mode']}]")
self.slow_print(f"  {forge['guidance']}")
def run_compassion_check(self):
print("\n" + "-" * 62)
self.slow_print("  BOUNDED COMPASSION & VICTIM SANCTUARY CHECK")
print("-" * 62)
vuln = self.ask_float("1. Genuine vulnerability / hurt in the other person? (0=none, 10=deep)", 5.0)
coercion = self.ask_float("2. Guilt-tripping, boundary-pushing, or coercion? (0=none, 10=heavy)", 0.0)
ill = input("3. Signs of ill intent or willful obliviousness? (y/n) [n]: ").strip().lower() == "y"
vfa = self.ask_float("4. Your current wound acidity ratio (0.10=fresh, 0.45=tender)", 0.15, 0.0, 1.0)
res = self.compassion.evaluate_compassion_flow(
empathic_awareness=0.8,
genuine_vulnerability=(vuln or 0.0) / 10.0,
coercive_leverage=(coercion or 0.0) / 10.0,
ill_intent_detected=ill,
vfa_acidity_ratio=vfa or 0.15,
)
print(f"\n  [{res['empathy_mode']} -> {res['sympathy_action']}]")
self.slow_print(f"  {res['guidance']}")
def run_signal_hygiene(self):
fear = self.ask_float("  Fear/outrage media load today (0-10)", 4.0) or 4.0
good = self.ask_float("  Verified good news / bright spots today (0-10)", 6.0) or 6.0
sig = self.plasticity.filter_sensory_intake(fear, good)
print(f"\n  [Thalamic SNR: {sig['thalamic_snr']} - {sig['signal_state']}]")
self.slow_print(f"  {sig['guidance']}")
def main_menu(self):
seal = self.mithril.compute_file_seal(os.path.abspath(file))
print("\n" + "=" * 62)
self.slow_print("  PROJECT THALAMUS - Sovereign Peace & Elvish Sanctuary OS")
self.slow_print(f"  Mithril RAM Seal: {seal[:16]}... | Zero Persistence")
print("=" * 62)
while True:
print(f"\n  Impedance Profile: [{self.mbti.mbti_code}] | Wound Sensitivity: {self.trauma.wound_depth}")
print("  1. Begin Thalamic Relay Check-In (Trauma, Lenz, DARVO & Shaolin)")
print("  2. Bounded Empathy & Victim Sanctuary Check")
print("  3. Run 130-160 Hz Helmholtz Breathing Pacer")
print("  4. Sweet Tea Signal Hygiene & Rock Steady Neuroplasticity")
print("  5. Adjust Wound Sensitivity")
print("  6. Exit & Wipe Volatile RAM")
choice = input("\n  Select an option (1-6): ").strip()
if choice == "1":
self.run_check_in()
elif choice == "2":
self.run_compassion_check()
elif choice == "3":
self.helmholtz_pacer(3)
elif choice == "4":
self.run_signal_hygiene()
elif choice == "5":
val = self.ask_float("  Set wound sensitivity (0.0=resilient, 1.0=very tender)", self.trauma.wound_depth, 0.0, 1.0)
if val is not None:
self.trauma.wound_depth = val
self.slow_print(f"  Sensitivity updated to {val}.")
elif choice == "6":
self.slow_print("\n  Volatile RAM cleared. Walk in peace and sovereign clarity.\n")
break
else:
print("  Please choose 1 through 6.")
if name == "main":
ProjectThalamusOS().main_menu()

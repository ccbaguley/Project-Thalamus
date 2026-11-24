#!/usr/bin/env python3
# Project Thalamus (@ccbaguley) | MIT License | Single-File RAM Sanctuary
import hashlib
import math
import os
import sys
import time


def _clip(val, low, high):
    return max(low, min(high, float(val)))


class SovereignCompassionGate:
    """Pillar 12: Inductive Empathy & Bounded Sympathy Gate (Victim-Safe).
    Distinguishes genuine victims in need from bad-faith manipulators using
    coercive-leverage math. Guarantees warm sanctuary support for victims while
    blocking ill-intentioned actors from exploiting empathy.
    """

    def evaluate_compassion_flow(
        self,
        empathic_awareness,
        genuine_vulnerability,
        coercive_leverage,
        ill_intent_detected,
        vfa_acidity_ratio,
    ):
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


class DarvoPhaseShield:
    """Pillar 7: DARVO (Deny, Attack, Reverse Victim & Offender) Phase-Inversion Shield.
    Detects narrative polarity flips and stabilizes user reactions by dissolving
    the JADE (Justify, Argue, Defend, Explain) reflex.
    """

    def __init__(self, inversion_threshold=4.5):
        self.inversion_threshold = float(inversion_threshold)

    def evaluate_interaction(self, reality_denial, attack_velocity, blame_reversal, urge_to_explain):
        denial = max(0.0, float(reality_denial))
        vel = max(0.0, float(attack_velocity))
        reversal = max(0.0, float(blame_reversal))
        jade = max(0.0, float(urge_to_explain))

        polarity_inversion = denial * reversal * (vel / 5.0)
        darvo_detected = polarity_inversion >= self.inversion_threshold
        reaction_stability = round(10.0 / (1.0 + (jade * 0.35)), 2)

        if darvo_detected:
            return {
                "darvo_flag": True,
                "inversion_score": round(polarity_inversion, 2),
                "reaction_stability": reaction_stability,
                "posture": "ELVISH_VEIL_DETACHMENT",
                "guidance": (
                    "Polarity inversion detected (Deny / Attack / Victim-Flip). Drop the urge to explain, "
                    "hold your quiet truth, and step behind the Veil."
                ),
            }

        return {
            "darvo_flag": False,
            "inversion_score": round(polarity_inversion, 2),
            "reaction_stability": reaction_stability,
            "posture": "OPEN_DIALOGUE",
            "guidance": "No severe polarity flip detected. Stay anchored in your own pace.",
        }


class ElvishSanctuaryMesh:
    """Pillar 5: Elvish Harmonic Community Mesh.
    Non-violent Lenz Veil perimeter deflection, zero-detail Canopy Rest lanterns
    for wounded neighbors, and a voluntary Commons goodness pool.
    """

    def __init__(self, node_id="node_01"):
        self.node_id = node_id
        self.commons_pool = 0.0
        self.neighbor_states = {}

    def compute_veil_deflection(self, hostile_velocity, aligned_node_count=3, stiffness=1.2):
        vel = max(0.0, float(hostile_velocity))
        nodes = max(1, int(aligned_node_count))
        veil_force = -nodes * float(stiffness) * vel
        return {
            "veil_deflection_force": round(veil_force, 2),
            "harm_inflicted": 0.0,
            "status": "PERMEABLE_WELCOME" if vel == 0 else "HARMONIC_VEIL_DEFLECTION",
        }

    def broadcast_canopy_status(self, islanding_open, vfa_acidity_ratio):
        needs_quiet = bool(islanding_open) or (float(vfa_acidity_ratio) > 0.30)
        signal = "CANOPY_REST" if needs_quiet else "CLEAR_SKY"
        return {
            "node_id": self.node_id,
            "lantern_signal": signal,
            "private_details_shared": False,
        }

    def contribute_to_commons(self, goodness_yield, vfa_acidity_ratio):
        # Never drain a node whose own wound acidity exceeds 0.30
        if float(vfa_acidity_ratio) > 0.30:
            return {"contributed": 0.0, "commons_total": round(self.commons_pool, 2)}
        gift = max(0.0, float(goodness_yield))
        self.commons_pool += gift
        return {"contributed": round(gift, 2), "commons_total": round(self.commons_pool, 2)}


class LenzMycelialAlchemist:
    """Pillar 2: Lenz's Law Boundary Repulsion & Mycelial-Thermoelectric Alchemy.
    Deflects avoidable toxic velocity (-dPhi/dt) without hostility, or absorbs
    unavoidable friction, separates dense resentment sludge via vortex logic,
    and distills clean constructive energy.
    """

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

        absorbed_energy = tox * self.zeta_mycelium * (1.0 - math.exp(-0.2 * t))
        sludge_purged = absorbed_energy * ego
        clean_stream = absorbed_energy - sludge_purged
        goodness_yield = clean_stream * self.eta_alchemy

        return {
            "absorbed_energy": round(absorbed_energy, 2),
            "sludge_purged": round(sludge_purged, 2),
            "goodness_yield": round(goodness_yield, 2),
        }


class MbtiEvolutionTelemetry:
    """Pillar 4: Cognitive Impedance Matching & SCADA Evolution Drift Detection.
    Adapts reflection style to the user's current cognitive preferences (E/I, S/N, T/F, J/P)
    without rigid labeling, and alerts gently when personal growth shifts their baseline.
    """

    def __init__(self, mbti_code="INFJ", drift_threshold=0.65):
        self.mbti_code = mbti_code.upper()
        self.drift_threshold = float(drift_threshold)
        self.baseline_vec = self._encode_mbti(self.mbti_code)
        self.ema_vec = list(self.baseline_vec)

    def _encode_mbti(self, code):
        mapping = {
            "E": -0.6, "I": 0.6,
            "S": -0.6, "N": 0.6,
            "T": -0.6, "F": 0.6,
            "J": -0.6, "P": 0.6,
        }
        padded = (code.upper() + "INFJ")[:4]
        return [mapping.get(ch, 0.0) for ch in padded]

    def _decode_vector(self, vec):
        axes = [("E", "I"), ("S", "N"), ("T", "F"), ("J", "P")]
        return "".join(pos if val >= 0.0 else neg for (neg, pos), val in zip(axes, vec))

    def match_impedance(self, memory_fog=0.0):
        if float(memory_fog) > 0.5:
            return "High memory fog: Bypassing abstract typing; using direct somatic 145 Hz grounding."

        notes = [
            "Solitary sanctuary reflection" if "I" in self.mbti_code else "Safe external dialogue/service",
            "Concrete physical anchors" if "S" in self.mbti_code else "Symbolic meaning & faith patterns",
            "Logical trade-off clarity" if "T" in self.mbti_code else "Relational & moral harmony",
            "Structured boundary closure" if "J" in self.mbti_code else "Flexible open-ended flow",
        ]
        return " | ".join(notes)

    def observe_evolution(self, observed_session_vec, learning_rate=0.25):
        obs = [_clip(v, -1.0, 1.0) for v in observed_session_vec[:4]]
        lr = _clip(learning_rate, 0.01, 1.0)

        self.ema_vec = [
            (1.0 - lr) * curr + lr * new_val
            for curr, new_val in zip(self.ema_vec, obs)
        ]

        drift = math.sqrt(sum((a - b) ** 2 for a, b in zip(self.ema_vec, self.baseline_vec)))
        evolved = drift >= self.drift_threshold
        suggested = self._decode_vector(self.ema_vec)

        return {
            "current_baseline": self.mbti_code,
            "lived_tendency": suggested,
            "evolution_drift_score": round(drift, 3),
            "retest_alert": evolved,
            "guidance": (
                f"Evolution Notice: Significant growth detected from [{self.mbti_code}] toward [{suggested}]. "
                "Would you like to run the optional 4-question recalibration?"
                if evolved
                else "Cognitive impedance remains aligned with your current baseline."
            ),
        }


class MithrilAntiSabotageGuard:
    """Pillar 6: Mithril Integrity & Anti-Sabotage Layer.
    Provides SHA-256 self-verification against coercive code tampering and
    routes machine-speed bot/saboteur spam into a harmless Helmholtz decoy loop.
    """

    def __init__(self, bio_cadence_min_seconds=2.0):
        self.bio_cadence_min = float(bio_cadence_min_seconds)

    def compute_file_seal(self, filepath):
        h = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def verify_seal(self, filepath, expected_sha256):
        actual = self.compute_file_seal(filepath)
        intact = (actual == expected_sha256)
        return {
            "seal_intact": intact,
            "sha256": actual,
            "status": "MITHRIL_SEAL_VERIFIED" if intact else "WARNING_CODE_MODIFIED",
        }

    def evaluate_cadence(self, seconds_between_actions, external_socket_detected=False):
        dt = max(0.0, float(seconds_between_actions))
        if external_socket_detected or dt < self.bio_cadence_min:
            return {
                "integrity_index": 0.0,
                "routing": "HELMHOLTZ_ACOUSTIC_DECOY",
                "retaliation": False,
                "guidance": "Unnatural cadence or external socket detected—routed to 145 Hz acoustic decoy loop.",
            }
        return {
            "integrity_index": 1.0,
            "routing": "SOVEREIGN_SANCTUARY",
            "retaliation": False,
            "guidance": "Authentic human cadence verified.",
        }


class NaturalConsequenceMirror:
    """Pillar 11: Mirror of Natural Consequence & Anti-Subsidy Shield.
    Stops emotional/practical subsidies for willfully oblivious, bad-faith actors
    so natural consequences teach them—while proving self-governance exerts zero control.
    """

    def evaluate_subsidy_boundary(
        self,
        repeated_harm,
        feigned_obliviousness,
        refuses_accountability=True,
        accuses_you_of_control=False,
    ):
        blindness_index = max(0.0, float(repeated_harm)) * (max(0.0, float(feigned_obliviousness)) / 5.0)
        unrepentant = bool(refuses_accountability) and (blindness_index >= 4.0)

        if unrepentant:
            msg = (
                "Willful obliviousness detected. Set your rescue/absorption subsidy to 0.0—stop explaining, "
                "stop cushioning their fallout, and let natural consequences be their teacher."
            )
            if accuses_you_of_control:
                msg += " Governing your own access exerts zero outward control over them."
            return {
                "posture": "ZERO_SUBSIDY_MIRROR",
                "outward_control_force": 0.0,
                "guidance": msg,
            }

        return {
            "posture": "GRACE_WITH_DISCERNMENT",
            "outward_control_force": 0.0,
            "guidance": "Offer one clear, gentle truth without lecturing, then leave the choice to them.",
        }


class ThalamicRelayCore:
    """Pillar 1: Neuro-Physical Thalamic Relay.
    Models emotional settling via a Damped Harmonic Oscillator and calculates
    user-weighted equilibrium across Personal Wants, Core Values, and Social Harmony.
    """

    def __init__(self, want_weight=1.0, value_weight=1.5, social_weight=1.2):
        self.weights = [float(want_weight), float(value_weight), float(social_weight)]

    def damp_emotion(self, initial_emotion, reflection_minutes, damping_gamma=0.15, omega=0.5):
        e0 = _clip(initial_emotion, -10.0, 10.0)
        t = max(0.0, float(reflection_minutes))
        settled = e0 * math.exp(-damping_gamma * t) * math.cos(omega * t)
        return round(settled, 3)

    def route_equilibrium(self, want_score, value_score, social_score, current_emotion):
        inputs = [_clip(want_score, 0.0, 10.0), _clip(value_score, 0.0, 10.0), _clip(social_score, 0.0, 10.0)]
        weight_sum = sum(self.weights)
        if weight_sum <= 0:
            aligned_output = 0.0
        else:
            aligned_output = sum(i * w for i, w in zip(inputs, self.weights)) / weight_sum

        clarity = max(0.0, 1.0 - (abs(float(current_emotion)) / 10.0))
        readiness = aligned_output * clarity

        return {
            "aligned_harmony": round(aligned_output, 2),
            "clarity_percent": round(clarity * 100.0, 1),
            "action_readiness": round(readiness, 2),
        }


class NeuroPlasticitySanctuary:
    """Pillar 9: Kinetic Neuroplasticity (Rock Steady Boxing) & Signal Hygiene (Sweet Tea).
    Rewires neural pathways via safe, non-contact rhythmic bilateral movement
    and filters chronic fear-media noise with verified life-affirming signals.
    """

    def __init__(self, bdnf_factor=0.65):
        self.mu_bdnf = _clip(bdnf_factor, 0.1, 1.0)

    def calculate_rewiring_pulse(self, rhythm_intensity, bilateral_focus, vfa_acidity_ratio):
        if float(vfa_acidity_ratio) > 0.30:
            return {
                "mode": "GENTLE_SOMATIC_REST",
                "neuroplastic_gain": 0.0,
                "guidance": "Reserves are tender today (VFA > 0.30). Skip high-cadence footwork and use seated bilateral breathing.",
            }

        rhythm = _clip(rhythm_intensity, 0.0, 10.0) / 10.0
        bilateral = _clip(bilateral_focus, 0.0, 10.0) / 10.0
        safety_headroom = max(0.1, 1.0 - (float(vfa_acidity_ratio) / 0.30))
        gain = self.mu_bdnf * rhythm * bilateral * safety_headroom * 10.0

        return {
            "mode": "KINETIC_NEUROPLASTICITY",
            "neuroplastic_gain": round(gain, 2),
            "guidance": "Rhythmic cross-body movement active—carving fresh neural pathways around old static.",
        }

    def filter_sensory_intake(self, fear_media_load, verified_good_news):
        fear = max(0.0, float(fear_media_load))
        good = max(0.0, float(verified_good_news))
        snr = (good + 2.0) / (1.0 + (fear * 0.5))
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


class ReticularNullGate:
    """Pillar 10: Thalamic Reticular Nucleus Null-Gate.
    Locks out enemies and destructive negative feedback at the outer perimeter
    using air-gapped allow-list logic—spending zero energy on retaliation or rumination.
    """

    def __init__(self, trust_threshold=0.60):
        self.trust_threshold = float(trust_threshold)
        self.trusted_keys = set()

    def authorize_node(self, node_id):
        self.trusted_keys.add(node_id)

    def revoke_node(self, node_id):
        self.trusted_keys.discard(node_id)

    def filter_incoming_signal(self, sender_id, good_faith_score, hostility_detected=False, is_trusted_source=False):
        authorized = bool(is_trusted_source) or (sender_id in self.trusted_keys)
        if hostility_detected or not authorized or float(good_faith_score) < self.trust_threshold:
            return {
                "gate_state": "LOCKED_OUT (NULL_DROP)",
                "energy_expended": 0.0,
                "guidance": "Enemy or destructive feedback locked out at perimeter—zero entry, zero reply, zero energy spent.",
            }
        return {
            "gate_state": "OPEN (CONSTRUCTIVE_SIGNAL)",
            "energy_expended": 0.1,
            "guidance": "Trusted, good-faith signal verified. Safe to consider calmly.",
        }


class ShaolinDisciplineForge:
    """Pillar 8: Shaolin Chan-Wu-Yi (Stillness, Discipline, Healing) Forge.
    Transmutes pain into rooted inner strength (Gong Li) through paced breath
    and voluntary discipline—strictly halting intense forging when wounds need rest.
    """

    def __init__(self, daily_consistency=0.5, stance_rooting=0.7):
        self.consistency = _clip(daily_consistency, 0.0, 1.0)
        self.rooting = _clip(stance_rooting, 0.0, 1.0)

    def transmute_pain(self, raw_pain, breath_quality, vfa_acidity_ratio, ego_tension=0.3):
        pain = _clip(raw_pain, 0.0, 10.0)
        breath = _clip(breath_quality, 0.0, 10.0)
        ego = max(0.0, float(ego_tension))

        if float(vfa_acidity_ratio) > 0.30:
            return {
                "mode": "SHAOLIN_YI_RESTORATION",
                "forged_strength_gain": 0.0,
                "root_stability": round(self.rooting * (breath / 10.0) * 5.0, 2),
                "guidance": (
                    "True Kung Fu honors healing first. Wound acidity exceeds 0.30—set down heavy"
                    " effort today and practice soft Qi Gong breathing."
                ),
            }

        transmutation_rate = (pain / 10.0) * (breath / 10.0) * (0.4 + self.consistency)
        strength_gain = round(transmutation_rate * 2.5, 3)
        root_stability = round((self.rooting * (breath / 10.0) * 10.0) / (1.0 + ego), 2)

        return {
            "mode": "CHAN_WU_FORGING",
            "forged_strength_gain": strength_gain,
            "root_stability": root_stability,
            "guidance": (
                "Sink your breath into your lower stance. Let discomfort pass through a relaxed,"
                " elastic frame—turning raw weight into quiet, unshakeable strength."
            ),
        }


class TraumaMemorySanctuary:
    """Pillar 3: Trauma, Memory-Fog & Wound Alkalinity Sanctuary.
    Implements EE29 20ms sub-cycle trigger islanding, zero-recall memory-fog
    continuity, and Anaerobic 0.30 VFA/Alkalinity wound protection.
    """

    def __init__(self, wound_sensitivity=0.5):
        self.wound_depth = _clip(wound_sensitivity, 0.0, 1.0)

    def check_trigger_islanding(self, trigger_intensity, trigger_onset_speed):
        intensity = _clip(trigger_intensity, 0.0, 10.0)
        speed = max(0.0, float(trigger_onset_speed))
        surge = self.wound_depth * (intensity * speed)
        islanding_tripped = surge >= 4.0

        return {
            "surge_level": round(surge, 2),
            "islanding_relay": "OPEN (SAFE_PAUSE)" if islanding_tripped else "CLOSED (CONNECTED)",
            "guidance": (
                "Trigger surge detected. External demands decoupled—prioritize somatic grounding."
                if islanding_tripped
                else "Nervous system within safe operating band."
            ),
        }

    def check_wound_alkalinity(self, acute_pain, alkaline_support, memory_fog=0.0):
        pain = max(0.0, float(acute_pain))
        support = max(0.5, float(alkaline_support))
        fog = _clip(memory_fog, 0.0, 1.0)

        vfa_ratio = pain / support
        needs_alkaline_rest = vfa_ratio > 0.30

        cognitive_pct = round((1.0 - fog) * 100.0, 1.0)
        somatic_pct = round(fog * 100.0, 1.0)

        return {
            "vfa_acidity_ratio": round(vfa_ratio, 2),
            "sour_guard_active": needs_alkaline_rest,
            "cognitive_capacity_percent": cognitive_pct,
            "somatic_anchor_percent": somatic_pct,
            "guidance": (
                "Acidity > 0.30: Pause outward exertion; apply rest, faith, or 145 Hz breathing."
                if needs_alkaline_rest
                else "Equilibrium stable. Ready for gentle reflection or service."
            ),
        }


class ProjectThalamusOS:

    def __init__(self):
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
        print(
            f"\n  [Wound VFA Ratio: {alk['vfa_acidity_ratio']} | "
            f"Cognitive/Somatic: {alk['cognitive_capacity_percent']}% / {alk['somatic_anchor_percent']}%]"
        )
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
                print(
                    f"  Mycelial Alchemy Yield: +{alchemy['goodness_yield']} clean goodness "
                    f"(Sludge purged: {alchemy['sludge_purged']})"
                )
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
            genuine_vulnerability=(0.0 if vuln is None else vuln) / 10.0,
            coercive_leverage=(0.0 if coercion is None else coercion) / 10.0,
            ill_intent_detected=ill,
            vfa_acidity_ratio=0.15 if vfa is None else vfa,
        )
        print(f"\n  [{res['empathy_mode']} -> {res['sympathy_action']}]")
        self.slow_print(f"  {res['guidance']}")

    def run_signal_hygiene(self):
        fear_in = self.ask_float("  Fear/outrage media load today (0-10)", 4.0)
        good_in = self.ask_float("  Verified good news / bright spots today (0-10)", 6.0)
        fear = 4.0 if fear_in is None else fear_in
        good = 6.0 if good_in is None else good_in
        sig = self.plasticity.filter_sensory_intake(fear, good)
        print(f"\n  [Thalamic SNR: {sig['thalamic_snr']} - {sig['signal_state']}]")
        self.slow_print(f"  {sig['guidance']}")

    def main_menu(self):
        seal = self.mithril.compute_file_seal(os.path.abspath(__file__))
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


if __name__ == "__main__":
    ProjectThalamusOS().main_menu()

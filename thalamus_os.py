#!/usr/bin/env python3
"""Project Thalamus — Sovereign Neuro-Physical, Trauma-Informed & Elvish Sanctuary CLI.

License: MIT
Architecture: 100% Local RAM | Zero External Dependencies | Zero Behavior Modification
"""

import os
import sys
import time

from thalamus_core.compassion_gate import SovereignCompassionGate
from thalamus_core.darvo_shield import DarvoPhaseShield
from thalamus_core.elvish_mesh import ElvishSanctuaryMesh
from thalamus_core.lenz_alchemy import LenzMycelialAlchemist
from thalamus_core.mbti_telemetry import MbtiEvolutionTelemetry
from thalamus_core.mithril_guard import MithrilAntiSabotageGuard
from thalamus_core.natural_mirror import NaturalConsequenceMirror
from thalamus_core.neuro_math import ThalamicRelayCore
from thalamus_core.neuro_plasticity import NeuroPlasticitySanctuary
from thalamus_core.reticular_lockout import ReticularNullGate
from thalamus_core.shaolin_forge import ShaolinDisciplineForge
from thalamus_core.trauma_sanctuary import TraumaMemorySanctuary


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
                print(
                    "  No rush—enter a number, or type skip if things feel"
                    " foggy."
                )

    def helmholtz_pacer(self, cycles=2):
        print("\n" + "-" * 62)
        self.slow_print(
            "  Settling into the 130-160 Hz Helmholtz Chamber rhythm."
        )
        self.slow_print(
            "  Nothing is demanded of you here. Just let your shoulders drop."
        )
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
        self.slow_print(
            "  Type skip anytime if memory feels blank or blurry."
        )
        print("-" * 62)

        fog_in = self.ask_float(
            "1. Memory fog / dissociative haze right now? (0=clear, 10=heavy)",
            2.0,
        )
        memory_fog = 0.8 if fog_in is None else (fog_in / 10.0)

        if memory_fog >= 0.65:
            print()
            self.slow_print(
                "  Thank you for naming that. When memory is foggy, your brain"
                " is"
            )
            self.slow_print(
                "  protecting you. We will not force recall or heavy thinking"
                " today."
            )
            if (
                input(
                    "  Run a gentle 2-cycle 145 Hz grounding breath? (y/n) [y]: "
                )
                .strip()
                .lower()
                != "n"
            ):
                self.helmholtz_pacer(2)
            return

        trig = self.ask_float(
            "2. Active trigger or sudden emotional surge? (0=calm, 10=intense)",
            2.0,
        )
        trig = 5.0 if trig is None else trig
        island = self.trauma.check_trigger_islanding(
            trig, trigger_onset_speed=1.2
        )

        if "OPEN" in island["islanding_relay"]:
            print(
                "\n  [EE29 SUB-CYCLE ISLANDING RELAY OPEN - Surge:"
                f" {island['surge_level']}]"
            )
            self.slow_print(f"  {island['guidance']}")
            canopy = self.mesh.broadcast_canopy_status(True, 0.4)
            print(
                f"  Elvish Mesh Lantern: [{canopy['lantern_signal']}] (Zero"
                " private details shared)"
            )
            if (
                input(
                    "  Run a 2-cycle 145 Hz grounding breath? (y/n) [y]: "
                )
                .strip()
                .lower()
                != "n"
            ):
                self.helmholtz_pacer(2)
            return

        pain = self.ask_float(
            "3. How tender are old wounds right now? (0=light, 10=deep ache)",
            2.5,
        )
        support = self.ask_float(
            "4. Current steady support (rest, faith, safety)? (1=low,"
            " 10=strong)",
            7.5,
        )
        pain = 2.5 if pain is None else pain
        support = 7.5 if support is None else max(support, 0.5)

        alk = self.trauma.check_wound_alkalinity(pain, support, memory_fog)
        print(
            f"\n  [Wound VFA Ratio: {alk['vfa_acidity_ratio']} |"
            f" Cognitive/Somatic: {alk['cognitive_capacity_percent']}% /"
            f" {alk['somatic_anchor_percent']}%]"
        )
        self.slow_print(f"  {alk['guidance']}")

        if alk["sour_guard_active"]:
            forge = self.shaolin.transmute_pain(
                pain,
                breath_quality=7.0,
                vfa_acidity_ratio=alk["vfa_acidity_ratio"],
            )
            self.slow_print(f"  [Shaolin Yi]: {forge['guidance']}")
            return

        tox = self.ask_float(
            "\n5. External friction, DARVO, or hostility today? (0=none,"
            " 10=heavy)",
            2.0,
        )
        tox = 2.0 if tox is None else tox

        if tox >= 3.0:
            is_darvo = (
                input(
                    "  Are they denying reality, attacking, or flipping"
                    " victim/offender? (y/n) [n]: "
                )
                .strip()
                .lower()
                == "y"
            )
            if is_darvo:
                d_res = self.darvo.evaluate_interaction(
                    8.0, tox, 8.0, urge_to_explain=3.0
                )
                print(
                    f"\n  [DARVO PHASE-INVERSION SHIELD - {d_res['posture']}]"
                )
                self.slow_print(f"  {d_res['guidance']}")
                return

            can_leave = (
                input(
                    "  Can you peacefully step back or disengage? (y/n) [y]: "
                )
                .strip()
                .lower()
                != "n"
            )
            lenz = self.alchemist.evaluate_lenz_gate(
                tox, approach_velocity=1.1, can_disengage=can_leave
            )
            print(f"\n  [{lenz['mode']} - Force: {lenz['repulsion_force']}]")
            self.slow_print(f"  {lenz['guidance']}")

            if lenz["mode"] == "ALCHEMICAL_CAPTURE":
                alchemy = self.alchemist.alchemize_friction(
                    tox, reflection_minutes=10
                )
                print(
                    "  Mycelial Alchemy Yield:"
                    f" +{alchemy['goodness_yield']} clean goodness (Sludge"
                    f" purged: {alchemy['sludge_purged']})"
                )
                self.mesh.contribute_to_commons(
                    alchemy["goodness_yield"], alk["vfa_acidity_ratio"]
                )

        forge = self.shaolin.transmute_pain(
            pain, breath_quality=8.0, vfa_acidity_ratio=alk["vfa_acidity_ratio"]
        )
        print(f"\n  [Shaolin Chan-Wu-Yi Forge - {forge['mode']}]")
        self.slow_print(f"  {forge['guidance']}")

    def run_compassion_check(self):
        print("\n" + "-" * 62)
        self.slow_print("  BOUNDED COMPASSION & VICTIM SANCTUARY CHECK")
        print("-" * 62)
        vuln = self.ask_float(
            "1. Genuine vulnerability / hurt in the other person? (0=none,"
            " 10=deep)",
            5.0,
        )
        coercion = self.ask_float(
            "2. Guilt-tripping, boundary-pushing, or coercion? (0=none,"
            " 10=heavy)",
            0.0,
        )
        ill = (
            input(
                "3. Signs of ill intent or willful obliviousness? (y/n) [n]: "
            )
            .strip()
            .lower()
            == "y"
        )
        vfa = self.ask_float(
            "4. Your current wound acidity ratio (0.10=fresh, 0.45=tender)",
            0.15,
            0.0,
            1.0,
        )

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
good = (
self.ask_float("  Verified good news / bright spots today (0-10)", 6.0)
or 6.0
)
sig = self.plasticity.filter_sensory_intake(fear, good)
print(f"\n  [Thalamic SNR: {sig['thalamic_snr']} - {sig['signal_state']}]")
self.slow_print(f"  {sig['guidance']}")
def main_menu(self):
seal = self.mithril.compute_file_seal(os.path.abspath(file))
print("\n" + "=" * 62)
self.slow_print(
"  PROJECT THALAMUS - Sovereign Peace & Elvish Sanctuary OS"
)
self.slow_print(f"  Mithril RAM Seal: {seal[:16]}... | Zero Persistence")
print("=" * 62)
while True:
print(
f"\n  Impedance Profile: [{self.mbti.mbti_code}] | Wound"
f" Sensitivity: {self.trauma.wound_depth}"
)
print(
"  1. Begin Thalamic Relay Check-In (Trauma, Lenz, DARVO &"
" Shaolin)"
)
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
val = self.ask_float(
"  Set wound sensitivity (0.0=resilient, 1.0=very tender)",
self.trauma.wound_depth,
0.0,
1.0,
)
if val is not None:
self.trauma.wound_depth = val
self.slow_print(f"  Sensitivity updated to {val}.")
elif choice == "6":
self.slow_print(
"\n  Volatile RAM cleared. Walk in peace and sovereign"
" clarity.\n"
)
break
else:
print("  Please choose 1 through 6.")
if name == "main":
ProjectThalamusOS().main_menu()

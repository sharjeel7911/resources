"""
Animation 4: GRU vs LSTM side-by-side — same input, watch both
architectures process it and compare the results.
"""
from manim import *
import numpy as np

PRIMARY = "#0A2540"
SECONDARY = "#635BFF"
ACCENT = "#00D4FF"
SUCCESS = "#32D583"
WARNING = "#FFC107"
DANGER = "#DC3545"


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class GRUvsLSTM(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ── Title ──
        title = Text("GRU vs LSTM: Same Input, Different Paths", font_size=36, color=PRIMARY, weight=BOLD)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP, buff=0.15))

        # ── Input display ──
        input_box = VGroup(
            Text("Input:", font_size=18, color=PRIMARY),
            MathTex(r"h_{t-1} = [0.5, -0.3]", font_size=20, color=SECONDARY),
            MathTex(r"x_t = [1.0, 0.5]", font_size=20, color=ACCENT),
        ).arrange(RIGHT, buff=0.5).next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(input_box))

        # ── Two columns ──
        lstm_title = Text("LSTM", font_size=28, color=DANGER, weight=BOLD).move_to([-3.2, 1.5, 0])
        gru_title = Text("GRU", font_size=28, color=SUCCESS, weight=BOLD).move_to([3.2, 1.5, 0])
        divider = DashedLine(
            start=[0, 1.8, 0], end=[0, -3.5, 0],
            color=ManimColor(PRIMARY), dash_length=0.1, stroke_opacity=0.3,
        )
        self.play(Write(lstm_title), Write(gru_title), Create(divider))

        # ── LSTM side ──
        lstm_steps = [
            (r"f_t = \sigma(\ldots) = [0.62, 0.64]", "Forget gate", DANGER),
            (r"i_t = \sigma(\ldots) = [0.62, 0.64]", "Input gate", SUCCESS),
            (r"\tilde{C}_t = \tanh(\ldots) = [0.45, 0.52]", "Candidate", ACCENT),
            (r"o_t = \sigma(\ldots) = [0.62, 0.64]", "Output gate", SECONDARY),
            (r"C_t = [0.78, 0.20]", "Cell state update", WARNING),
            (r"h_t = [0.40, 0.13]", "Hidden state", SECONDARY),
        ]

        # ── GRU side ──
        gru_steps = [
            (r"r_t = \sigma(\ldots) = [0.62, 0.64]", "Reset gate", DANGER),
            (r"z_t = \sigma(\ldots) = [0.62, 0.64]", "Update gate", SUCCESS),
            (r"\tilde{h}_t = \tanh(\ldots) = [0.42, 0.45]", "Candidate", ACCENT),
            (r"h_t = [0.47, -0.03]", "Hidden state", SECONDARY),
        ]

        y_start = 0.8
        y_step = 0.6

        lstm_mobjects = []
        gru_mobjects = []

        # Animate LSTM and GRU steps interleaved
        max_steps = max(len(lstm_steps), len(gru_steps))

        for step in range(max_steps):
            anims = []

            # LSTM step
            if step < len(lstm_steps):
                eq_str, label_str, col = lstm_steps[step]
                y_pos = y_start - step * y_step

                label = Text(label_str, font_size=13, color=col, weight=BOLD).move_to(
                    [-4.8, y_pos + 0.12, 0]
                )
                eq = MathTex(eq_str, font_size=17, color=PRIMARY).move_to([-2.8, y_pos - 0.12, 0])

                # Gate icon (small circle)
                icon = Circle(
                    radius=0.12, color=col, fill_color=col, fill_opacity=0.3, stroke_width=2,
                ).move_to([-5.5, y_pos, 0])

                lstm_mobjects.extend([label, eq, icon])
                anims.extend([FadeIn(icon), Write(label), Write(eq)])

            # GRU step
            if step < len(gru_steps):
                eq_str, label_str, col = gru_steps[step]
                y_pos = y_start - step * y_step

                label = Text(label_str, font_size=13, color=col, weight=BOLD).move_to(
                    [1.7, y_pos + 0.12, 0]
                )
                eq = MathTex(eq_str, font_size=17, color=PRIMARY).move_to([3.7, y_pos - 0.12, 0])

                icon = Circle(
                    radius=0.12, color=col, fill_color=col, fill_opacity=0.3, stroke_width=2,
                ).move_to([1.0, y_pos, 0])

                gru_mobjects.extend([label, eq, icon])
                anims.extend([FadeIn(icon), Write(label), Write(eq)])

            self.play(*anims, run_time=0.8)
            self.wait(0.3)

        self.wait(1)

        # ── Comparison boxes ──
        lstm_result = MathTex(
            r"h_t^{\text{LSTM}} = [0.40, 0.13]",
            font_size=26, color=DANGER,
        ).move_to([-3.2, -2.8, 0])
        gru_result = MathTex(
            r"h_t^{\text{GRU}} = [0.47, -0.03]",
            font_size=26, color=SUCCESS,
        ).move_to([3.2, -2.8, 0])

        lstm_box = SurroundingRectangle(lstm_result, color=DANGER, buff=0.12, stroke_width=2.5)
        gru_box = SurroundingRectangle(gru_result, color=SUCCESS, buff=0.12, stroke_width=2.5)

        self.play(
            Write(lstm_result), Create(lstm_box),
            Write(gru_result), Create(gru_box),
            run_time=1,
        )
        self.wait(1)

        # ── Stats comparison ──
        stats = VGroup(
            Text("LSTM: 4 gates, 2 states, more control", font_size=16, color=DANGER),
            Text("GRU:  2 gates, 1 state, faster training", font_size=16, color=SUCCESS),
            Text("Same building blocks: sigmoid + tanh + matrix multiply", font_size=16, color=SECONDARY),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to([0, -3.5, 0])

        for s in stats:
            self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(3)

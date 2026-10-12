"""
Animation 1: RNN Forward Pass — watch the hidden state evolve word by word.
Processes "I like AI" and shows the matrix math at each step.
"""
from manim import *
import numpy as np

# Branding colours
PRIMARY = "#0A2540"
SECONDARY = "#635BFF"
ACCENT = "#00D4FF"
SUCCESS = "#32D583"
WARNING = "#FFC107"
DANGER = "#DC3545"


class RNNForwardPass(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ── Title ──
        title = Text("RNN Forward Pass", font_size=44, color=PRIMARY, weight=BOLD)
        subtitle = Text(
            'Processing "I  like  AI" one word at a time',
            font_size=24, color=SECONDARY,
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── Constants ──
        words = ["I", "like", "AI"]
        embeddings = [
            np.array([0.2, -0.1, 0.4]),
            np.array([0.8, 0.6, 0.3]),
            np.array([0.5, 0.4, 0.2]),
        ]
        W = np.array([[0.1, 0.2, 0.3], [0.4, 0.1, 0.2], [0.3, 0.4, 0.1]])
        U = np.array([[0.2, 0.1, 0.3], [0.1, 0.3, 0.2], [0.3, 0.2, 0.1]])
        b = np.array([0.1, 0.1, 0.1])
        h = np.zeros(3)

        # ── Build the unrolled RNN diagram ──
        cells = []
        cell_labels = []
        arrows_horiz = []
        input_arrows = []
        input_labels = []
        output_labels = []

        for i in range(3):
            x_pos = (i - 1) * 4.2
            # Cell box
            cell = RoundedRectangle(
                corner_radius=0.15, width=1.8, height=1.2,
                color=SECONDARY, fill_color=SECONDARY, fill_opacity=0.12,
                stroke_width=2.5,
            ).move_to([x_pos, 0, 0])
            cells.append(cell)

            lbl = Text("tanh", font_size=18, color=SECONDARY).move_to(cell)
            cell_labels.append(lbl)

            # Input arrow + label
            inp = Arrow(
                start=[x_pos, -2, 0], end=[x_pos, -0.7, 0],
                color=ACCENT, stroke_width=3, max_tip_length_to_length_ratio=0.15,
            )
            input_arrows.append(inp)

            word_lbl = Text(words[i], font_size=22, color=PRIMARY, weight=BOLD).move_to(
                [x_pos, -2.4, 0]
            )
            vec_str = "[" + ", ".join(f"{v:.1f}" for v in embeddings[i]) + "]"
            vec_lbl = Text(vec_str, font_size=14, color=ACCENT).next_to(word_lbl, DOWN, buff=0.15)
            input_labels.append(VGroup(word_lbl, vec_lbl))

            # Output label (hidden state) — placeholder, will be updated
            h_lbl = Text("h? = [?, ?, ?]", font_size=14, color=SUCCESS).move_to(
                [x_pos, 1.2, 0]
            )
            output_labels.append(h_lbl)

            # Horizontal arrow between cells
            if i > 0:
                arr = Arrow(
                    start=[(i - 2) * 4.2 + 0.95, 0, 0],
                    end=[x_pos - 0.95, 0, 0],
                    color=WARNING, stroke_width=3, max_tip_length_to_length_ratio=0.12,
                )
                arrows_horiz.append(arr)

        # h_0 label
        h0_lbl = Text("h₀ = [0, 0, 0]", font_size=16, color=ManimColor(PRIMARY)).move_to(
            [-1 * 4.2 - 1.8, 0, 0]
        )

        # Draw static structure
        self.play(
            *[Create(c) for c in cells],
            *[Write(l) for l in cell_labels],
            *[GrowArrow(a) for a in input_arrows],
            *[FadeIn(l) for l in input_labels],
            *[GrowArrow(a) for a in arrows_horiz],
            FadeIn(h0_lbl),
            run_time=2,
        )
        self.wait(0.5)

        # ── Equation at bottom ──
        eq = MathTex(
            r"h_t = \tanh(W_x \, x_t + W_h \, h_{t-1} + b)",
            font_size=30, color=PRIMARY,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(eq))
        self.wait(1)

        # ── Animate each step ──
        for step in range(3):
            x_pos = (step - 1) * 4.2

            # Highlight current cell
            highlight = cells[step].copy().set_stroke(color=WARNING, width=5)
            self.play(Create(highlight), run_time=0.4)

            # Compute
            z = W @ embeddings[step] + U @ h + b
            h_new = np.tanh(z)

            # Show computation
            z_str = "[" + ", ".join(f"{v:.2f}" for v in z) + "]"
            h_str = "[" + ", ".join(f"{v:.2f}" for v in h_new) + "]"

            comp_line1 = Text(
                f"z = Wx·x + Wh·h + b = {z_str}",
                font_size=16, color=PRIMARY,
            ).move_to([x_pos, 1.8, 0])
            comp_line2 = Text(
                f"h{step+1} = tanh(z) = {h_str}",
                font_size=16, color=SUCCESS, weight=BOLD,
            ).next_to(comp_line1, DOWN, buff=0.15)

            self.play(FadeIn(comp_line1, shift=DOWN * 0.2), run_time=0.6)
            self.wait(0.5)
            self.play(FadeIn(comp_line2, shift=DOWN * 0.2), run_time=0.6)

            # Update the output label
            new_h_lbl = Text(
                f"h{step+1} = {h_str}", font_size=15, color=SUCCESS, weight=BOLD,
            ).move_to([x_pos, 1.2, 0])
            self.play(
                FadeOut(output_labels[step]),
                FadeIn(new_h_lbl),
                run_time=0.4,
            )
            output_labels[step] = new_h_lbl

            h = h_new
            self.wait(1)

            # Clean computation text, keep highlight fading
            self.play(
                FadeOut(comp_line1), FadeOut(comp_line2),
                highlight.animate.set_stroke(opacity=0),
                run_time=0.5,
            )

        # ── Final message ──
        final = Text(
            "h₃ encodes the entire sentence → use for classification",
            font_size=24, color=SECONDARY, weight=BOLD,
        ).to_edge(UP, buff=0.3)
        box = SurroundingRectangle(output_labels[2], color=SUCCESS, buff=0.15, stroke_width=3)
        self.play(Write(final), Create(box))
        self.wait(3)

"""
Animation 2: Vanishing Gradient Problem — watch the gradient shrink
as it propagates backward through time steps.
"""
from manim import *
import numpy as np

PRIMARY = "#0A2540"
SECONDARY = "#635BFF"
ACCENT = "#00D4FF"
SUCCESS = "#32D583"
WARNING = "#FFC107"
DANGER = "#DC3545"


class VanishingGradient(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        n_steps = 8

        # ── Title ──
        title = Text("The Vanishing Gradient Problem", font_size=40, color=PRIMARY, weight=BOLD)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP, buff=0.25))

        # ── Build chain of RNN cells ──
        cells = []
        labels = []
        h_labels = []
        for i in range(n_steps):
            x_pos = (i - (n_steps - 1) / 2) * 1.5
            cell = RoundedRectangle(
                corner_radius=0.1, width=0.9, height=0.7,
                color=SECONDARY, fill_color=SECONDARY, fill_opacity=0.1,
                stroke_width=2,
            ).move_to([x_pos, 0, 0])
            cells.append(cell)
            lbl = MathTex(f"h_{{{i}}}", font_size=22, color=PRIMARY).move_to(cell)
            labels.append(lbl)

            word_idx = i
            h_lbl = MathTex(f"x_{{{i}}}", font_size=18, color=ACCENT).next_to(cell, DOWN, buff=0.3)
            h_labels.append(h_lbl)

        # Arrows between cells
        arrows = []
        for i in range(n_steps - 1):
            x1 = (i - (n_steps - 1) / 2) * 1.5 + 0.5
            x2 = (i + 1 - (n_steps - 1) / 2) * 1.5 - 0.5
            arr = Arrow(
                start=[x1, 0, 0], end=[x2, 0, 0],
                color=PRIMARY, stroke_width=2, max_tip_length_to_length_ratio=0.2,
                buff=0,
            )
            arrows.append(arr)

        # Input arrows
        input_arrows = []
        for i in range(n_steps):
            x_pos = (i - (n_steps - 1) / 2) * 1.5
            arr = Arrow(
                start=[x_pos, -1.2, 0], end=[x_pos, -0.4, 0],
                color=ACCENT, stroke_width=1.5, max_tip_length_to_length_ratio=0.2,
            )
            input_arrows.append(arr)

        self.play(
            *[Create(c) for c in cells],
            *[Write(l) for l in labels],
            *[GrowArrow(a) for a in arrows],
            *[GrowArrow(a) for a in input_arrows],
            *[Write(l) for l in h_labels],
            run_time=1.5,
        )
        self.wait(0.5)

        # ── Sentence below ──
        sentence = Text(
            '"Despite the cat\'s initial fear, the dog became its best friend"',
            font_size=16, color=PRIMARY,
        ).next_to(h_labels[-1], DOWN, buff=0.6).move_to([0, -2.2, 0])
        self.play(FadeIn(sentence))
        self.wait(1)

        # ── Loss at the end ──
        loss_lbl = MathTex(r"\mathcal{L}", font_size=32, color=DANGER).next_to(
            cells[-1], UP, buff=0.5
        )
        loss_arrow = Arrow(
            start=cells[-1].get_top() + UP * 0.05,
            end=loss_lbl.get_bottom() + DOWN * 0.05,
            color=DANGER, stroke_width=2,
        )
        self.play(Write(loss_lbl), GrowArrow(loss_arrow))
        self.wait(0.5)

        # ── Show gradient formula ──
        grad_eq = MathTex(
            r"\frac{\partial \mathcal{L}}{\partial h_k}",
            r"= \prod_{i=k+1}^{t}",
            r"W_h^\top \cdot \text{diag}(\tanh'(z_i))",
            font_size=24, color=PRIMARY,
        ).move_to([0, -3, 0])
        self.play(Write(grad_eq))
        self.wait(1.5)

        # ── Animate gradient flowing backward ──
        info_text = Text(
            "Gradient flows backward from loss...",
            font_size=20, color=SECONDARY,
        ).to_edge(DOWN, buff=0.15)
        self.play(Write(info_text))

        # Create gradient "pulse" that shrinks
        W_norm = 0.65  # < 1 → vanishing
        gradient_magnitude = 1.0

        grad_circles = []
        mag_labels = []

        for i in range(n_steps - 1, -1, -1):
            x_pos = (i - (n_steps - 1) / 2) * 1.5
            radius = max(0.08, 0.4 * gradient_magnitude)
            opacity = max(0.1, gradient_magnitude)

            # Gradient circle on top of cell
            circ = Circle(
                radius=radius,
                color=DANGER, fill_color=DANGER,
                fill_opacity=opacity, stroke_width=0,
            ).move_to([x_pos, 0.8, 0])

            mag_text = Text(
                f"{gradient_magnitude:.2f}",
                font_size=max(10, int(16 * gradient_magnitude + 4)),
                color=DANGER,
            ).next_to(circ, UP, buff=0.08)

            if i == n_steps - 1:
                self.play(GrowFromCenter(circ), FadeIn(mag_text), run_time=0.5)
            else:
                self.play(GrowFromCenter(circ), FadeIn(mag_text), run_time=0.3)

            grad_circles.append(circ)
            mag_labels.append(mag_text)

            gradient_magnitude *= W_norm

        self.wait(0.5)

        # Update info text
        vanish_msg = Text(
            "Gradient nearly vanished! Early words have almost no influence.",
            font_size=20, color=DANGER, weight=BOLD,
        ).to_edge(DOWN, buff=0.15)
        self.play(FadeOut(info_text), Write(vanish_msg))

        # Highlight first cell's tiny gradient
        tiny_box = SurroundingRectangle(
            VGroup(grad_circles[-1], mag_labels[-1]),
            color=DANGER, stroke_width=3, buff=0.1,
        )
        self.play(Create(tiny_box))
        self.wait(2)

        # ── Contrast: exploding case ──
        self.play(
            *[FadeOut(c) for c in grad_circles],
            *[FadeOut(l) for l in mag_labels],
            FadeOut(tiny_box), FadeOut(vanish_msg),
            run_time=0.8,
        )

        explode_msg = Text(
            "Now with ||W_h|| > 1 → Exploding gradients!",
            font_size=20, color=WARNING, weight=BOLD,
        ).to_edge(DOWN, buff=0.15)
        self.play(Write(explode_msg))

        gradient_magnitude = 1.0
        W_norm_explode = 1.5

        for i in range(n_steps - 1, max(n_steps - 6, -1), -1):
            x_pos = (i - (n_steps - 1) / 2) * 1.5
            radius = min(0.6, 0.15 * gradient_magnitude)
            opacity = min(1.0, 0.3 + 0.1 * gradient_magnitude)

            circ = Circle(
                radius=radius,
                color=WARNING, fill_color=WARNING,
                fill_opacity=opacity, stroke_width=0,
            ).move_to([x_pos, 0.8, 0])

            mag_text = Text(
                f"{gradient_magnitude:.1f}",
                font_size=min(24, int(12 + 3 * gradient_magnitude)),
                color=WARNING, weight=BOLD,
            ).next_to(circ, UP, buff=0.08)

            self.play(GrowFromCenter(circ), FadeIn(mag_text), run_time=0.3)
            gradient_magnitude *= W_norm_explode

        self.wait(1)

        # Final takeaway
        takeaway = Text(
            "LSTM solves this with additive cell state updates",
            font_size=24, color=SUCCESS, weight=BOLD,
        ).move_to([0, -3, 0])
        self.play(FadeOut(grad_eq), Write(takeaway))
        self.wait(3)

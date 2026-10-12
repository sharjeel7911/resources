"""
Animation 3: LSTM Gate Mechanism — show how each gate filters
information through the cell, with concrete numbers.
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


class LSTMGates(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ── Title ──
        title = Text("LSTM: How Gates Control Memory", font_size=40, color=PRIMARY, weight=BOLD)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.2))

        # ── Cell state as conveyor belt ──
        belt_y = 1.8
        belt = Arrow(
            start=[-6, belt_y, 0], end=[6, belt_y, 0],
            color=SUCCESS, stroke_width=6, max_tip_length_to_length_ratio=0.03,
        )
        belt_label = Text("Cell State (memory conveyor belt)", font_size=18, color=SUCCESS).next_to(
            belt, UP, buff=0.1
        )

        ct_old = MathTex(
            r"C_{t-1} = \begin{bmatrix} 0.80 \\ -0.20 \end{bmatrix}",
            font_size=22, color=PRIMARY,
        ).move_to([-5, belt_y - 0.5, 0])

        self.play(GrowArrow(belt), Write(belt_label), FadeIn(ct_old))
        self.wait(1)

        # ── PHASE 1: Forget Gate ──
        phase1_title = Text("Step 1: Forget Gate", font_size=28, color=DANGER, weight=BOLD).move_to(
            [0, 0.5, 0]
        )
        self.play(Write(phase1_title))

        # Forget gate values
        ft_vals = np.array([0.62, 0.64])
        forget_text = VGroup(
            MathTex(r"f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)", font_size=20, color=PRIMARY),
            MathTex(
                r"= \begin{bmatrix} 0.62 \\ 0.64 \end{bmatrix}",
                font_size=22, color=DANGER,
            ),
        ).arrange(RIGHT, buff=0.3).move_to([0, -0.3, 0])
        self.play(Write(forget_text))
        self.wait(0.5)

        # Show filtering
        filter_text = Text(
            '"Keep 62% of dim 1, keep 64% of dim 2"',
            font_size=18, color=DANGER,
        ).move_to([0, -1.1, 0])
        self.play(FadeIn(filter_text))

        # Visualize bars
        bar_group = VGroup()
        for i, (val, old_val, dim_name) in enumerate(
            zip(ft_vals, [0.80, -0.20], ["dim 1", "dim 2"])
        ):
            x_base = -2.5 + i * 5
            y_base = -2.2

            # Old value bar
            old_bar = Rectangle(
                width=0.6, height=abs(old_val) * 2,
                color=PRIMARY, fill_color=PRIMARY, fill_opacity=0.3,
                stroke_width=1,
            ).move_to([x_base - 0.5, y_base + abs(old_val), 0])

            # Kept portion
            kept = old_val * val
            kept_bar = Rectangle(
                width=0.6, height=abs(kept) * 2,
                color=SUCCESS, fill_color=SUCCESS, fill_opacity=0.6,
                stroke_width=1,
            ).move_to([x_base + 0.5, y_base + abs(kept), 0])

            old_lbl = Text(f"{old_val:.2f}", font_size=14, color=PRIMARY).next_to(old_bar, UP, buff=0.05)
            kept_lbl = Text(f"{kept:.2f}", font_size=14, color=SUCCESS).next_to(kept_bar, UP, buff=0.05)
            dim_lbl = Text(dim_name, font_size=14, color=PRIMARY).move_to([x_base, y_base - 0.3, 0])
            times_lbl = MathTex(r"\times " + f"{val:.2f}", font_size=18, color=DANGER).move_to(
                [x_base, y_base + 0.8, 0]
            )

            grp = VGroup(old_bar, old_lbl, kept_bar, kept_lbl, dim_lbl, times_lbl)
            bar_group.add(grp)

        self.play(FadeIn(bar_group), run_time=1.5)
        self.wait(2)

        # Clean
        self.play(
            FadeOut(phase1_title), FadeOut(forget_text),
            FadeOut(filter_text), FadeOut(bar_group),
            run_time=0.6,
        )

        # ── PHASE 2: Input Gate ──
        phase2_title = Text(
            "Step 2: Input Gate + Candidate", font_size=28, color=SUCCESS, weight=BOLD,
        ).move_to([0, 0.5, 0])
        self.play(Write(phase2_title))

        it_vals = np.array([0.62, 0.64])
        ct_cand = np.array([0.45, 0.52])

        input_text = VGroup(
            MathTex(r"i_t = \sigma(\ldots) = \begin{bmatrix}0.62\\0.64\end{bmatrix}", font_size=20, color=SUCCESS),
            MathTex(r"\tilde{C}_t = \tanh(\ldots) = \begin{bmatrix}0.45\\0.52\end{bmatrix}", font_size=20, color=ACCENT),
        ).arrange(RIGHT, buff=0.8).move_to([0, -0.3, 0])
        self.play(Write(input_text))
        self.wait(0.5)

        new_info = MathTex(
            r"i_t \odot \tilde{C}_t = \begin{bmatrix}0.28\\0.33\end{bmatrix}",
            font_size=24, color=SUCCESS,
        ).move_to([0, -1.3, 0])
        new_label = Text('"New information to add"', font_size=18, color=SUCCESS).next_to(
            new_info, DOWN, buff=0.2
        )
        self.play(Write(new_info), FadeIn(new_label))
        self.wait(2)

        self.play(
            FadeOut(phase2_title), FadeOut(input_text),
            FadeOut(new_info), FadeOut(new_label),
            run_time=0.6,
        )

        # ── PHASE 3: Cell Update ──
        phase3_title = Text(
            "Step 3: Update Cell State", font_size=28, color=SECONDARY, weight=BOLD,
        ).move_to([0, 0.5, 0])
        self.play(Write(phase3_title))

        update_eq = MathTex(
            r"C_t",
            r"= f_t \odot C_{t-1}",
            r"+ i_t \odot \tilde{C}_t",
            font_size=26, color=PRIMARY,
        ).move_to([0, -0.2, 0])
        update_eq[1].set_color(DANGER)
        update_eq[2].set_color(SUCCESS)
        self.play(Write(update_eq))
        self.wait(0.5)

        # Numbers
        nums = MathTex(
            r"= \begin{bmatrix}0.50\\-0.13\end{bmatrix}",
            r"+ \begin{bmatrix}0.28\\0.33\end{bmatrix}",
            r"= \begin{bmatrix}0.78\\0.20\end{bmatrix}",
            font_size=24, color=PRIMARY,
        ).move_to([0, -1.2, 0])
        nums[0].set_color(DANGER)
        nums[1].set_color(SUCCESS)
        nums[2].set_color(SECONDARY)

        self.play(Write(nums[0]), run_time=0.5)
        self.wait(0.3)
        self.play(Write(nums[1]), run_time=0.5)
        self.wait(0.3)
        self.play(Write(nums[2]), run_time=0.5)

        # Update conveyor belt
        ct_new = MathTex(
            r"C_t = \begin{bmatrix}0.78\\0.20\end{bmatrix}",
            font_size=22, color=SECONDARY,
        ).move_to([3, belt_y - 0.5, 0])
        self.play(FadeIn(ct_new, shift=RIGHT * 0.5))
        self.wait(1)

        # Insight
        insight = Text(
            "dim 1: 0.80 → 0.78 (kept!)   dim 2: -0.20 → +0.20 (shifted!)",
            font_size=18, color=SECONDARY,
        ).move_to([0, -2.2, 0])
        self.play(Write(insight))
        self.wait(2)

        self.play(
            FadeOut(phase3_title), FadeOut(update_eq), FadeOut(nums), FadeOut(insight),
            run_time=0.6,
        )

        # ── PHASE 4: Output Gate ──
        phase4_title = Text(
            "Step 4: Output Gate → Hidden State",
            font_size=28, color=SECONDARY, weight=BOLD,
        ).move_to([0, 0.5, 0])
        self.play(Write(phase4_title))

        out_eq = MathTex(
            r"h_t = o_t \odot \tanh(C_t)",
            r"= \begin{bmatrix}0.62\\0.64\end{bmatrix}",
            r"\odot \begin{bmatrix}0.65\\0.20\end{bmatrix}",
            r"= \begin{bmatrix}0.40\\0.13\end{bmatrix}",
            font_size=24, color=PRIMARY,
        ).move_to([0, -0.5, 0])
        out_eq[3].set_color(SECONDARY)

        self.play(Write(out_eq), run_time=2)
        self.wait(1)

        final_msg = Text(
            "h_t = [0.40, 0.13] is the contextual embedding for this time step",
            font_size=20, color=SECONDARY, weight=BOLD,
        ).move_to([0, -1.5, 0])
        box = SurroundingRectangle(out_eq[3], color=SUCCESS, buff=0.1, stroke_width=3)
        self.play(Write(final_msg), Create(box))
        self.wait(1)

        # Key takeaway
        takeaway = Text(
            "Every gate is just sigmoid(matrix × vector). No magic — just arithmetic!",
            font_size=22, color=SUCCESS, weight=BOLD,
        ).move_to([0, -2.5, 0])
        self.play(Write(takeaway))
        self.wait(3)

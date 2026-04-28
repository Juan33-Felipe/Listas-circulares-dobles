import math
import tkinter as tk

class ClockDrawer:
    def __init__(self, canvas, radius, center_x, center_y, positions_list):
        self.canvas = canvas
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.positions = positions_list

    def draw_face(self, colors):
        self.canvas.delete("face")
        
        self.canvas.create_oval(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            fill=colors["clock_bg"], outline=colors["clock_border"], width=4, tags="face"
        )

        curr = self.positions.head
        if not curr: return

        while True:
            is_hour = (curr.value % 5 == 0)
            tick_length = 15 if is_hour else 7
            width = 3 if is_hour else 1

            outer_x = self.center_x + self.radius * math.cos(curr.angle)
            outer_y = self.center_y + self.radius * math.sin(curr.angle)
            inner_x = self.center_x + (self.radius - tick_length) * math.cos(curr.angle)
            inner_y = self.center_y + (self.radius - tick_length) * math.sin(curr.angle)

            self.canvas.create_line(inner_x, inner_y, outer_x, outer_y, 
                                    fill=colors["ticks"], width=width, tags="face")

            if is_hour:
                num_radius = self.radius - 30
                num_x = self.center_x + num_radius * math.cos(curr.angle)
                num_y = self.center_y + num_radius * math.sin(curr.angle)
                
                hour_num = curr.value // 5
                if hour_num == 0: 
                    hour_num = 12
                
                self.canvas.create_text(num_x, num_y, text=str(hour_num), 
                                        font=("Helvetica", 12, "bold"), fill=colors["text"], tags="face")

            curr = curr.next
            if curr == self.positions.head:
                break

    def draw_hands(self, s, m, h, colors):
        self.canvas.delete("hands")
        
        sec_node = self.positions.get_node(s)
        min_node = self.positions.get_node(m)
        hour_index = (h * 5) + (m // 12)
        hour_node = self.positions.get_node(hour_index)

        if hour_node:
            h_length = self.radius * 0.5
            hx = self.center_x + h_length * math.cos(hour_node.angle)
            hy = self.center_y + h_length * math.sin(hour_node.angle)
            self.canvas.create_line(self.center_x, self.center_y, hx, hy, 
                                    width=6, fill=colors["hour_hand"], capstyle=tk.ROUND, tags="hands")

        if min_node:
            m_length = self.radius * 0.75
            mx = self.center_x + m_length * math.cos(min_node.angle)
            my = self.center_y + m_length * math.sin(min_node.angle)
            self.canvas.create_line(self.center_x, self.center_y, mx, my, 
                                    width=4, fill=colors["min_hand"], capstyle=tk.ROUND, tags="hands")

        if sec_node:
            s_length = self.radius * 0.9
            sx = self.center_x + s_length * math.cos(sec_node.angle)
            sy = self.center_y + s_length * math.sin(sec_node.angle)
            self.canvas.create_line(self.center_x, self.center_y, sx, sy, 
                                    width=2, fill=colors["sec_hand"], capstyle=tk.ROUND, tags="hands")

        self.canvas.create_oval(self.center_x - 6, self.center_y - 6, 
                                self.center_x + 6, self.center_y + 6, 
                                fill=colors["sec_hand"], outline=colors["clock_bg"], width=2, tags="hands")

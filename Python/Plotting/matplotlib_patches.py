import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat


class PersonPatch(pat.Circle):
    """
        This class combines many patches to make a custom patch
        The best way to reproduce such a thing is to read the
        source code for all patches you plan on combining.
        Also make use of ratios as often as possible to maintain
        proportionality between patches of different sizes"""
    cz = 0
    def __init__(self, xy, d, color=None, linewidth=None, edgecolor=None,
                 *args, **kwargs):
        super().__init__(xy, 0.0, linewidth=None, edgecolor=None)
        # self.set_edgecolor(edgecolor)
        xy_head = np.array(xy) + np.array([0, d*0.15])
        r_head = 0.5 * (d/2)
        # fill
        self.head = pat.Circle(xy_head,
                               r_head,
                               fill=True,
                               facecolor=color,
                               edgecolor=None,
                               linewidth=None,
                               zorder=1 + PersonPatch.cz)

        wh_neck = np.array([r_head*0.8, r_head * 0.25])
        xy_neck = xy_head + np.array([0, -r_head]) - wh_neck / 2
        self.neck = pat.Rectangle(xy_neck,
                                  wh_neck[0],
                                  wh_neck[1],
                                  fill=True,
                                  facecolor=color,
                                  edgecolor=None,
                                  linewidth=None,
                                  zorder=1 + PersonPatch.cz)

        wh_body = np.array([d*0.8, d/5])
        xy_body = xy + np.array([-wh_body[0]/2, wh_body[1]*0.5-d/2])
        top_left_body = xy_body + np.array([0, wh_body[1]])
        top_right_body = xy_body + wh_body
        self.body = pat.Rectangle(xy_body,
                                  wh_body[0],
                                  wh_body[1],
                                  fill=True,
                                  facecolor=color,
                                  edgecolor=None,
                                  linewidth=None,
                                  zorder=1 + PersonPatch.cz)

        r_shoulder = r_head * 0.3
        xy_l_shoulder = top_left_body + np.array([r_shoulder, 0])
        xy_r_shoulder = top_right_body + np.array([-r_shoulder, 0])
        self.l_shoulder = pat.Circle(xy_l_shoulder,
                                     r_shoulder,
                                     fill=True,
                                     facecolor=color,
                                     edgecolor=None,
                                     linewidth=None,
                                     zorder=1 + PersonPatch.cz)
        self.r_shoulder = pat.Circle(xy_r_shoulder,
                                     r_shoulder,
                                     fill=True,
                                     facecolor=color,
                                     edgecolor=None,
                                     linewidth=None,
                                     zorder=1 + PersonPatch.cz)
        xy_upper_body = xy_l_shoulder
        wh_upper_body = np.array([wh_body[0] - r_shoulder * 2, r_shoulder])
        self.upper_body = pat.Rectangle(xy_upper_body,
                                        wh_upper_body[0],
                                        wh_upper_body[1],
                                        fill=True,
                                        facecolor=color,
                                        edgecolor=None,
                                        linewidth=None,
                                        zorder=1 + PersonPatch.cz)

        self.head_l = pat.Circle(xy_head,
                               r_head,
                               fill=True,
                               facecolor=color,
                               edgecolor=edgecolor,
                               linewidth=linewidth,
                               zorder=PersonPatch.cz)
        self.neck_l = pat.Rectangle(xy_neck,
                                  wh_neck[0],
                                  wh_neck[1],
                                  fill=True,
                                  facecolor=color,
                                  edgecolor=edgecolor,
                                  linewidth=linewidth,
                                  zorder=PersonPatch.cz)
        self.body_l = pat.Rectangle(xy_body,
                                  wh_body[0],
                                  wh_body[1],
                                  fill=True,
                                  facecolor=color,
                                  edgecolor=edgecolor,
                                  linewidth=linewidth,
                                  zorder=PersonPatch.cz)
        self.l_shoulder_l = pat.Circle(xy_l_shoulder,
                                     r_shoulder,
                                     fill=True,
                                     facecolor=color,
                                     edgecolor=edgecolor,
                                     linewidth=linewidth,
                                     zorder=PersonPatch.cz)
        self.r_shoulder_l = pat.Circle(xy_r_shoulder,
                                     r_shoulder,
                                     fill=True,
                                     facecolor=color,
                                     edgecolor=edgecolor,
                                     linewidth=linewidth,
                                     zorder=PersonPatch.cz)
        self.upper_body_l = pat.Rectangle(xy_upper_body,
                                        wh_upper_body[0],
                                        wh_upper_body[1],
                                        fill=True,
                                        facecolor=color,
                                        edgecolor=edgecolor,
                                        linewidth=linewidth,
                                        zorder=PersonPatch.cz)
        self.xy_init = xy

    def add_to_ax(self, ax):
        ax.add_patch(self)
        ax.add_patch(self.head)
        ax.add_patch(self.neck)
        ax.add_patch(self.body)
        ax.add_patch(self.l_shoulder)
        ax.add_patch(self.r_shoulder)
        ax.add_patch(self.upper_body)
        ax.add_patch(self.head_l)
        ax.add_patch(self.neck_l)
        ax.add_patch(self.body_l)
        ax.add_patch(self.l_shoulder_l)
        ax.add_patch(self.r_shoulder_l)
        ax.add_patch(self.upper_body_l)

    def translate(self, dx, dy):
        self._center = self.center + [dx, dy]
        self.head._center = self.head._center + [dx, dy]
        self.neck._center = self.neck._center + [dx, dy]
        self.body._center = self.body._center + [dx, dy]
        self.l_shoulder._center = self.l_shoulder._center + [dx, dy]
        self.r_shoulder._center = self.r_shoulder._center + [dx, dy]
        self.upper_body._center = self.upper_body._center + [dx, dy]

    def set_xy(self, new_xy):
        new_xy = np.array(new_xy)
        self._center = new_xy
        self.head._center = self.head + new_xy
        self.neck._center = self.neck + new_xy
        self.bdoy._center = self.body + new_xy
        self.l_shoulder._center = self.l_shoulder + new_xy
        self.r_shoulder._center = self.r_shoulder + new_xy
        self.upper_body._center = self.upper_body + new_xy
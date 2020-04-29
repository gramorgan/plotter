from plot import Plot


def main(p: Plot):
    p.setup()
    p.goto(20, 70)
    p.lineto(20, 30)
    p.arcto(30, 20, 90)
    p.lineto(70, 20)
    p.arcto(80, 30, 90)
    p.lineto(80, 70)
    p.arcto(70, 80, 90)
    p.lineto(30, 80)
    p.arcto(20, 70, 90)
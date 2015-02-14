import graph;
unitsize(1mm);

/* Parameters */
int count = 50;
real g = 9.81;
real speed = 100;

/* Axis */
xlimits(0, 1019); ylimits(0, 520);
yequals(pic=currentpicture, L="$x$",y=0,
    ticks=Ticks(Step=50, step=10, end=false),
    arrow=Arrow(HookHead));
xequals(pic=currentpicture, L="$y$",x=0,
    ticks=Ticks(Step=50, step=10, end=false),
    arrow=Arrow(HookHead));

/* Functions */
real alpha = 0;
real t(real x) {
    return -g * x^2 / (2 * speed^2 * cos(alpha)^2) + tan(alpha) * x;
}
real f(real x) {
    return -g * x^2 / (2 * speed^2) + speed^2 / (2*g);
}

/* Graphing */
real zero(real a) {
    return speed^2 * cos(a) * (sin(a) + sqrt(sin(a)^2+2*g/speed^2)) / g;
}

draw(graph(f, 0, 1019), blue);
for(int i = 1; i <= count; ++i) {
    alpha = i * pi / (2*(count + 1));
    draw(graph(t, 0, zero(alpha)), red);
}


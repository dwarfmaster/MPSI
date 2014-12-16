/* Asymptote code for drawing the sierpinski fractal */
unitsize(10cm);

/* Number of iterations */
int count = 7;

/* The three beginning points */
pair p1 = (0,0);
pair p2 = (1,0);
pair p3 = (.5,sqrt(3)/2);

/* The recursive function */
void triserp(int count, pair p11, pair p12, pair p13) {
    if(count == 0) {
        return;
    }

    pair p21 = ((p11.x + p12.x) / 2, (p11.y + p12.y) / 2);
    pair p22 = ((p11.x + p13.x) / 2, (p11.y + p13.y) / 2);
    pair p23 = ((p12.x + p13.x) / 2, (p12.y + p13.y) / 2);
    draw(p21 -- p22 -- p23 -- cycle);

    triserp(count - 1, p11, p21, p22);
    triserp(count - 1, p12, p21, p23);
    triserp(count - 1, p13, p22, p23);
}

/* The main code */
draw(p1 -- p2 -- p3 -- cycle);
triserp(count, p1, p2, p3);


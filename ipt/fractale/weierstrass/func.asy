/* Asymptote code for drawing the weierstrass function. */
unitsize(5cm);

/* Number of iterations */
int count = 4;

/* The beginning points */
pair p1 = (0,0);
pair p2 = (1,1);

/* The recursive function */
void weiestrass(int count, pair p1, pair p2) {
    if(count == 0) {
        draw(p1 -- p2);
        return;
    }

    pair pm1 = ((p2.x - p1.x)/3 + p1.x,   2*(p2.y - p1.y)/3 + p1.y);
    pair pm2 = (2*(p2.x - p1.x)/3 + p1.x, (p2.y - p1.y)/3 + p1.y);

    count -= 1;
    weiestrass(count, p1,  pm1);
    weiestrass(count, pm1, pm2);
    weiestrass(count, pm2, p2);
}

/* The main code */
weiestrass(count, p1, p2);


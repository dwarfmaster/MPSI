#!/usr/bin/perl

use strict;
use warnings;
my $double = !0;

my $output = "output.asy";
open my $out, ">:encoding(UTF-8)", $output or die "Couldn't open $output";
print $out "unitsize(10cm);\n";

my $count = 7;
my (@p1, @p2, @p3);
if(not $double) {
    @p1 = (0.0,0.0);
    @p2 = (1.0,0.0);
    @p3 = (0.5,sqrt(3)/2.0);
    triangle($out, @p1, @p2, @p3);
    triserp($out, $count, @p1, @p2, @p3);
} else {
    @p1 = (0.0,0.0);
    @p2 = (1.0,0.0);
    @p3 = (1.0,1.0);
    triangle($out, @p1, @p2, @p3);
    triserp($out, $count, @p1, @p2, @p3);
    @p1 = (0.0,0.0);
    @p2 = (0.0,1.0);
    @p3 = (1.0,1.0);
    triangle($out, @p1, @p2, @p3);
    triserp($out, $count, @p1, @p2, @p3);
};

sub triserp {
    my ($out, $count, @pts) = @_;
    return if $count == 0;

    my @pts2 = (($pts[0] + $pts[2]) / 2.0, ($pts[1] + $pts[3]) / 2.0,
                ($pts[0] + $pts[4]) / 2.0, ($pts[1] + $pts[5]) / 2.0,
                ($pts[2] + $pts[4]) / 2.0, ($pts[3] + $pts[5]) / 2.0);
    triangle($out, @pts2);

    triserp($out, $count - 1, ($pts[0], $pts[1]), ($pts2[0], $pts2[1]), ($pts2[2], $pts2[3]));
    triserp($out, $count - 1, ($pts[2], $pts[3]), ($pts2[0], $pts2[1]), ($pts2[4], $pts2[5]));
    triserp($out, $count - 1, ($pts[4], $pts[5]), ($pts2[2], $pts2[3]), ($pts2[4], $pts2[5]));
}

sub triangle {
    my ($out, @points) = @_;
    print $out "draw(($points[0],$points[1]) -- ($points[2],$points[3]));\n";
    print $out "draw(($points[0],$points[1]) -- ($points[4],$points[5]));\n";
    print $out "draw(($points[4],$points[5]) -- ($points[2],$points[3]));\n";
}

close $out;


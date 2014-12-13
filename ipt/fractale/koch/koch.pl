#!/usr/bin/perl

use strict;
use warnings;
use Math::Trig;

my $output = "output.asy";
open my $out, ">:encoding(UTF-8)", $output or die "Couldn't open $output";
print $out "unitsize(10cm);\n";

my $count = 5;
my (@p1, @p2, @p3);
@p1 = (0.0, 0.0);
@p2 = (1.0, 0.0);
@p3 = (0.5, sqrt(3)/2.0);
side($out, $count, @p1, @p2);
side($out, $count, @p2, @p3);
side($out, $count, @p3, @p1);

sub side {
    my ($out, $count, @pts) = @_;
    line($out, @pts) and return if $count == 0;

    my @pt1 = ($pts[0], $pts[1]);
    my @pt2 = (2.0*$pts[0]/3.0 + $pts[2]/3.0, 2.0*$pts[1]/3.0 + $pts[3]/3.0);
    side($out, $count - 1, @pt1, @pt2);

    @pt1 = middle(@pts);
    side($out, $count - 1, @pt2, @pt1);

    @pt2 = ($pts[0]/3.0 + 2.0*$pts[2]/3.0, $pts[1]/3.0 + 2.0*$pts[3]/3.0);
    side($out, $count - 1, @pt1, @pt2);
    side($out, $count - 1, @pt2, ($pts[2], $pts[3]));
}

sub middle {
    my @pts = @_;
    my @v = ($pts[2] - $pts[0], $pts[3] - $pts[1]);
    my @u = (0.0, 0.0);
    if($pts[0] != $pts[2]) {
        $u[1] = 1.0;
        $u[0] = ($pts[1] - $pts[3]) / ($pts[2] - $pts[0]);
    } else {
        $u[0] = 1.0;
        $u[1] = ($pts[2] - $pts[0]) / ($pts[1] - $pts[3]);
    }

    my $fact = sqrt($v[0]*$v[0] + $v[1]*$v[1]);
    $fact *= sqrt(3)/6;
    $fact /= sqrt($u[0]*$u[0] + $u[1]*$u[1]);
    $fact *= makeRight(@v, @u);

    $u[0] *= $fact;
    $u[1] *= $fact;
    $u[0] += ($pts[0] + $pts[2]) / 2.0;
    $u[1] += ($pts[1] + $pts[3]) / 2.0;
    return @u;
}

sub makeRight {
    my @vecs = @_;
    if($vecs[2] == 0) {
        if($vecs[0] * $vecs[3] < 0) {
            return 1.0;
        } else {
            return -1.0;
        }
    } elsif($vecs[0] == 0) {
        if($vecs[1] * $vecs[2] < 0) {
            return -1.0;
        } else {
            return 1.0;
        }
    } else {
        my $theta1 = atan2($vecs[1], $vecs[0]);
        my $theta2 = atan2($vecs[3], $vecs[2]);
        my $angle = $theta1 - $theta2;

        if(($angle < 0 and $angle > (-1)*pi) or ($angle > pi)) {
            return -1.0;
        } else {
            return 1.0;
        }
    }
    return 1.0;
}

sub line {
    my ($out, @points) = @_;
    print $out "draw(($points[0],$points[1]) -- ($points[2],$points[3]));\n";
}

close $out;


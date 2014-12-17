#!/usr/bin/perl

use strict;
use warnings;

### Testing data ###
my $script = "exec ../gauss.py";
my @matrix = ("test1.matrix",
    "test2.matrix",
    "test3.matrix",
    "test4.matrix",
    "test5.matrix",
    "test6.matrix",
    "test7.matrix",
    "test8.matrix",
    "test9.matrix",
    "test10.matrix",
);
my @sols = ("sol1.matrix",
    "sol2.matrix",
    "sol3.matrix",
    "sol4.matrix",
    "sol5.matrix",
    "sol6.matrix",
    "sol7.matrix",
    "sol8.matrix",
    "sol9.matrix",
    "sol10.matrix",
);
my $len = scalar @matrix;
my $success = 0;

### Main code ###
my $count = 1;
while($count <= $len) {
    if(testing($matrix[$count - 1], $sols[$count - 1])) {
        print "Test $count/$len succeeded\n";
        $success++;
    } else {
        print "Test $count/$len failed\n";
    }
    $count++;
}
print "$success/$len test succeeded\n";

### Testing code ###
sub testing {
    my ($mat, $sol) = @_;
    my @matsol = matread($sol);
    my $output = `$script $mat`;
    my @matexp = matparse($output);

    if(scalar @matsol == 0) {
        if(scalar @matexp == 0) {
            return !0;
        } else {
            return !1;
        }
    } else {
        if(scalar @matexp == 0) {
            return !1;
        } elsif(scalar @matexp != scalar @matsol) {
            return !1;
        } else {
            my $i = 0;
            while($i < scalar @matexp) {
                my $diff = abs($matexp[$i] - $matsol[$i]);
                return !1 if $diff > 0.00001;
                $i++;
            }
            return !0;
        }
    }
}

### Matrix code ###
sub matread {
    my ($path) = @_;
    my @mat;
    open FD,"<:encoding(UTF-8)",$path or warn "Couldn't open \"$path\" : $!\n";
    while(my $line = <FD>) {
        continue if $line =~ m/^\s*$/;
        my @temp = ($line =~ m/(-?\d+(\.\d+)?)/g);
        my @values;
        for my $val (@temp) {
            if(not $val =~ m/^\./) {
                @values = (@values, $val);
            }
        }
        @mat = (@mat, @values);
    }
    close FD;
    return @mat;
}

sub matparse {
    my ($text) = @_;
    my @output = split "\n", $text;
    my @mat;

    my $insol = !1;
    for my $line (@output) {
        if($insol) {
            my @temp = ($line =~ m/(-?\d+(\.\d+)?)/g);
            my @values;
            for my $val (@temp) {
                if(not $val =~ m/^\./) {
                    @values = (@values, $val);
                }
            }
            @mat = (@mat, @values);
        } elsif($line =~ m/No solution/) {
            return ();
        } elsif($line =~ m/Solution/) {
            $insol = !0;
        }
    }
    return @mat;
}


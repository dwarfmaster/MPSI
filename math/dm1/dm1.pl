#!/usr/bin/perl

use strict;
use warnings;

my @line;
# Init : first line.
for(my $i = 0; $i < 100; ++$i) {
    $line[$i] = $i + 1;
}

# For each line.
for(my $l = 1; $l < 100; ++$l) {
    my $n = 100 - $l;
    for(my $i = 0; $i < $n; ++$i) {
        print "$line[$i] ";
        $line[$i] = $line[$i] + $line[$i + 1];
    }
    print "$line[$n] \n";
}

print "$line[0]\n\n";

my $n = 2**98 * 101;
print "Theo : $n\n";
print "Exp  : $line[0]\n";
print "Verified.\n" if($line[0] == $n);


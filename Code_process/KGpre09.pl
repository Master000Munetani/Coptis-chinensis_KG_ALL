open(IN,"C:/Users/15382/Desktop/predict/head23/RAW_HERB_G_D.txt") || die "$!";
open(IN1,"C:/Users/15382/Desktop/predict/head23/predict4.txt") || die "$!";
open(OUT1,">C:/Users/15382/Desktop/predict/head23/rel_predict04.txt") || die "$!";
# open(OUT2,">C:/Users/15382/Desktop/predict/head23/pr_04_tail.txt") || die "$!";
# open(OUT3,">C:/Users/15382/Desktop/predict/head23/pr_04_rel.txt") || die "$!";

my %h1;
my %h2;
my %h11;
my %h22;
my $i=1;
my $j=1;
while(<IN>){
    chomp($_);
    if(!$_){
        next;
    }
    else  {
    my @temp=split("\t",$_);
    if(!$h1{$temp[0]})
    {
        $h1{$temp[0]}=$i;
        $h11{$i}=$temp[0];
        $i++;
        # print OUT1 $h1{$temp[0]}."\n";
    }
    
    if(!$h1{$temp[2]})
    {
        $h1{$temp[2]}=$i;
        $h11{$i}=$temp[2];
        $i++;
        # print OUT2 $h1{$temp[2]}."\n";
    }
    
    if(!$h2{$temp[1]})
    {
        $h2{$temp[1]}=$j;
        $h22{$j}=$temp[1];
        $j++;
        # print OUT3 $h2{$temp[1]}."\n";
    }
   
    }

}

close(IN);

while(<IN1>){
    chomp($_);
    if(!$_){
        next;
    }
    else  {
        my @temp = split("\t",$_);
        print OUT1 $h11{$temp[0]}."\t".$h22{$temp[1]}."\t".$h11{$temp[2]}."\n";
    }
}
close(OUT1);
# close(OUT2);
# close(OUT3);

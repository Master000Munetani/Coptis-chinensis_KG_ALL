open(IN1,"C:/Users/15382/Desktop/Disease_ID.txt") || die "$!";
open(IN2,"C:/Users/15382/Desktop/TCM_ID.txt") || die "$!";
open(IN3,"C:/Users/15382/Desktop/tcm-d.txt") || die "$!";
open(OUT1,">C:/Users/15382/Desktop/pre03_real.txt") || die "$!";
my %h1;
my %h2;

while(<IN1>){
    chomp($_);
    if(!$_){
        next;
    }
    else  {
    my @temp=split("\t",$_);
    $h1{$temp[1]}=$temp[0];
    }

}
while(<IN2>){
    chomp($_);
    if(!$_){
        next;
    }
    else  {
    my @temp=split("\t",$_);
    $h2{$temp[0]}=$temp[1];
    }

}
while(<IN3>){
    chomp($_);
    if(!$_){
        next;
    }
    else  {
    my @temp=split("\t",$_);
    # if(exists $h2{$temp[0]}){
    #     print OUT1 $h2{$temp[0]}."\t".$temp[1]."\t".$h1{$temp[2]}."\n"
    # }
    # else{
    #     print OUT1 $temp[0]."\t".$temp[1]."\t".$h1{$temp[2]}."\n"
    # }
    # # $h2{$temp[0]}=$temp[1];
    print OUT1 $h2{$temp[0]}."\t".$temp[1]."\t".$h1{$temp[2]}."\n"
    }

}
close(IN1);
close(IN2);
close(IN3);

close(OUT1);

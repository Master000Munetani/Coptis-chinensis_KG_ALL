# 筛选黄连最为君药的中成药/古籍方剂
open(IN,"C:/Users/15382/Desktop/1.txt") || die "$!";
open(OUT,">C:/Users/15382/Desktop/2.txt") || die "$!";
while(<IN>){
    chomp($_);
    if(!$_){
        next;
    }
    else  {
        my @temp = split("\t",$_);
        my $id= $temp[0];
        my $name = $temp[1];
        $_  = $temp[2];
        s/(^"|"$)//g;
        my $t1 = $_;
        my @temp1 = split(",",$t1);
        for(my $i=0;$i<@temp1;$i++){

        print OUT $id."\t".$name."\t".$temp1[$i]."\n";
        }

    }
}
close(IN);
close(OUT);

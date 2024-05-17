# "C:\Users\15382\Desktop\process\ID/gene_entrezID.txt"
use strict;
use List::MoreUtils ':all';
my %hash_en=();
my %hash_rel=();
my @arr_en=();
my @arr_rel=();
open(IN1,"C:/Users/15382/Desktop/ALL_huanglian_ALL.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/drkg-gene.txt") || die "$!";
while (<IN1>) {
    chomp($_);
    if(!$_){
        next;
    }
    else {
            my @temp1=split("\t",$_);
            push(@arr_en,$temp1[0]);
            push(@arr_en,$temp1[2]);
            push(@arr_rel,$temp1[1]);
            # my @temp_head = split("::",$temp1[0]);
            # my $head = $temp_head[0];
            # my @temp_rel = split("::",$temp1[1]);
            # my $rel = $temp_rel[0];
            # my @temp_tail = split("::",$temp1[2]);
            # my $tail = $temp_tail[0];
            # if (exists $hash_en{$head}){
            #     $hash_en{$head}+=1;
            # }
            # else  {
            #     $hash_en{$head} = 1;
            # }
            # if (exists $hash_en{$tail}){
            #     $hash_en{$tail}+=1;
            # }
            # else  {
            #     $hash_en{$tail} = 1;
            # }
            # if (exists $hash_rel{$rel}){
            #     $hash_en{$rel}+=1;
            # }
            # else  {
            #     $hash_en{$rel} = 1;
            # }
            
            
        }
}
close(IN1);
my @uniq_en = uniq(@arr_en);
# my @uniq_rel = uniq(@arr_rel);
foreach my $num (@uniq_en) {
    my @temp = split("::",$num);
    $hash_en{$temp[0]}++;
}
foreach my $num (@arr_rel) {
    $hash_rel{$num}++;
}
foreach my $key (keys %hash_en) {
    print "$key: $hash_en{$key}\n";
}
foreach my $key (keys %hash_rel) {
    print "$key: $hash_rel{$key}\n";
}
# while(my ($k,$v)=each %has){
#     print "$k => $v\n";# 结果顺序随机
# }
# close(OUT);
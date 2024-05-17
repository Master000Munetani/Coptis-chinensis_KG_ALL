# 对预测输入数据和输出数据的前处理

# ## 01 
# open(IN,"C:/Users/15382/Desktop/predict/head1/RAW_C_treat_D.txt") || die "$!";
# open(OUT1,">C:/Users/15382/Desktop/predict/head1/pr_01_head.txt") || die "$!";
# open(OUT2,">C:/Users/15382/Desktop/predict/head1/pr_01_tail.txt") || die "$!";
# my %h1;
# # my %h2;
# my %h11;
# # my %h22;
# my $i=1;
# # my $j=1;
# while(<IN>){
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#     my @temp=split("\t",$_);
#     if(!$h1{$temp[0]})
#     {
#         $h1{$temp[0]}=$i;
#         $h11{$i}=$temp[0];
#         $i++;
#         print OUT1 $h1{$temp[0]}."\n";
#     }
#     else {
#         print OUT1 $h1{$temp[0]}."\n";
#     }
#     if(!$h1{$temp[2]})
#     {
#         $h1{$temp[2]}=$i;
#         $h11{$i}=$temp[2];
#         $i++;
#         print OUT2 $h1{$temp[2]}."\n";
#     }
#     else {
#         print OUT2 $h1{$temp[2]}."\n";
#     }
    
#     }

# }

# close(IN);
# close(OUT1);
# close(OUT2);


# ## 02 
# open(IN,"C:/Users/15382/Desktop/predict/tail1/RAW_synd_D.txt") || die "$!";
# open(OUT1,">C:/Users/15382/Desktop/predict/tail1/pr_02_head.txt") || die "$!";
# open(OUT2,">C:/Users/15382/Desktop/predict/tail1/pr_02_tail.txt") || die "$!";
# open(OUT3,">C:/Users/15382/Desktop/predict/tail1/pr_02_rel.txt") || die "$!";

# my %h1;
# my %h2;
# my %h11;
# my %h22;
# my $i=1;
# my $j=1;
# while(<IN>){
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#     my @temp=split("\t",$_);
#     if(!$h1{$temp[0]})
#     {
#         $h1{$temp[0]}=$i;
#         $h11{$i}=$temp[0];
#         $i++;
#         print OUT1 $h1{$temp[0]}."\n";
#     }
#     else {
#         print OUT1 $h1{$temp[0]}."\n";
#     }
#     if(!$h1{$temp[2]})
#     {
#         $h1{$temp[2]}=$i;
#         $h11{$i}=$temp[2];
#         $i++;
#         print OUT2 $h1{$temp[2]}."\n";
#     }
#     else {
#         print OUT2 $h1{$temp[2]}."\n";
#     }
#     if(!$h2{$temp[1]})
#     {
#         $h2{$temp[1]}=$j;
#         $h22{$i}=$temp[1];
#         $j++;
#         print OUT3 $h2{$temp[1]}."\n";
#     }
#     else {
#         print OUT3 $h2{$temp[1]}."\n";
#     }
#     }

# }

# close(IN);
# close(OUT1);
# close(OUT2);
# close(OUT3);

# 03 
# open(IN,"C:/Users/15382/Desktop/predict/tail2/RAW_TCM_D.txt") || die "$!";
# open(OUT1,">C:/Users/15382/Desktop/predict/tail2/pr_03_head.txt") || die "$!";
# open(OUT2,">C:/Users/15382/Desktop/predict/tail2/pr_03_tail.txt") || die "$!";
# open(OUT3,">C:/Users/15382/Desktop/predict/tail2/pr_03_rel.txt") || die "$!";

# my %h1;
# my %h2;
# my %h11;
# my %h22;
# my $i=1;
# my $j=1;
# while(<IN>){
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#     my @temp=split("\t",$_);
#     if(!$h1{$temp[0]})
#     {
#         $h1{$temp[0]}=$i;
#         $h11{$i}=$temp[0];
#         $i++;
#         print OUT1 $h1{$temp[0]}."\n";
#     }
#     else {
#         print OUT1 $h1{$temp[0]}."\n";
#     }
#     if(!$h1{$temp[2]})
#     {
#         $h1{$temp[2]}=$i;
#         $h11{$i}=$temp[2];
#         $i++;
#         print OUT2 $h1{$temp[2]}."\n";
#     }
#     else {
#         print OUT2 $h1{$temp[2]}."\n";
#     }
#     if(!$h2{$temp[1]})
#     {
#         $h2{$temp[1]}=$j;
#         $h22{$i}=$temp[1];
#         $j++;
#         print OUT3 $h2{$temp[1]}."\n";
#     }
#     else {
#         print OUT3 $h2{$temp[1]}."\n";
#     }
#     }

# }

# close(IN);
# close(OUT1);
# close(OUT2);
# close(OUT3);

## 45 
open(IN,"C:/Users/15382/Desktop/predict/head23/RAW_HERB_G_D.txt") || die "$!";
open(OUT1,">C:/Users/15382/Desktop/predict/head23/pr_04_head.txt") || die "$!";
open(OUT2,">C:/Users/15382/Desktop/predict/head23/pr_04_tail.txt") || die "$!";
open(OUT3,">C:/Users/15382/Desktop/predict/head23/pr_04_rel.txt") || die "$!";

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
        print OUT1 $h1{$temp[0]}."\n";
    }
    else {
        print OUT1 $h1{$temp[0]}."\n";
    }
    if(!$h1{$temp[2]})
    {
        $h1{$temp[2]}=$i;
        $h11{$i}=$temp[2];
        $i++;
        print OUT2 $h1{$temp[2]}."\n";
    }
    else {
        print OUT2 $h1{$temp[2]}."\n";
    }
    if(!$h2{$temp[1]})
    {
        $h2{$temp[1]}=$j;
        $h22{$i}=$temp[1];
        $j++;
        print OUT3 $h2{$temp[1]}."\n";
    }
    else {
        print OUT3 $h2{$temp[1]}."\n";
    }
    }

}

close(IN);
close(OUT1);
close(OUT2);
close(OUT3);
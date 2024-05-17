open(IN,"C:/Users/15382/Desktop/1.txt") || die "$!";
open(OUT,">C:/Users/15382/Desktop/2.txt") || die "$!";
while(<IN>){
    chomp($_);
    if(!$_){
        next;
    }
    else  {
        my $out0 = $_;
        my @temp=split("\t",$_);
        $_  = $temp[2];
        s/(^"|"$)//g;
        my $t1 = $_;
        # print $t1."\n";
        my @temp1=split(",",$t1);
        # print $temp1[0]."\n";
        if (grep { $_ eq "HuangLian" } @temp1) {
            my @index = (grep { $temp1[$_] eq "HuangLian"} 0..$#temp1);
            print $index[0]."\n";
            if ($index[0] > 0){
                next;
                }
            else  {print OUT $out0."\n";}
        } 
        else {
            print "no index\n";
            next;}
    }
}
close(IN);
close(OUT);


# my $hh = '"hello"';
# $hh = s/(^"|"$)//g;
# # my $hh = $_;
# print $hh
# # #!/usr/bin/perl
# # my @array = (1, 2, 3, 4, 5);
# # my $element = 3;
# # # 使用 grep 函数判断元素是否在数组中
# # my @result = grep { $_ == $element } @array;
# # if (@result) {
# # print "元素 $element 存在于数组中\n";
# # } else {
# # print "元素 $element 不存在于数组中\n";
# my $a ="Jishiteng,Sharen,Renshen,Shanyao,Shechuangzi,Huanglian,Huangbai,Baixianpi,Kushen,Huzhang,Zihuadiding,Difuzi,Bianxu,Yinchen,";
# my @temp1=split(",",$a);
# my @index = (grep { $temp1[$_] eq "Huanglian"} 0..$#temp1);
# # my $index = index(@temp1, "Huanglian");
# print $index[0]."\n";
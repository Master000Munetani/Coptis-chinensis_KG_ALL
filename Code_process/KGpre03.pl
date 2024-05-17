# # 01 GOterm-Gene 
# open(IN,"C:/Users/15382/Desktop/process/gene_entrezID.txt") || die "$!";
# my %hash0=();
# while(<IN>){
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#         my @temp = split("\t",$_);
#         $hash0{$temp[0]}=$temp[1];
#     }
# }
# close(IN);
# open(IN1,"C:/Users/15382/Desktop/process/GOterm-badian.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/process/GOterm-Gene.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#         my @temp1 = split("\t",$_);
#         if(exists($hash0{$temp1[2]})){
#             print OUT "Gene::".$hash0{$temp1[2]}."\t".$temp1[1]."\t"."Biological Process::".$temp1[0]."\n";
#         }
#         else  {
#             next;
#         }
#     }
# }
# close(IN1);
# close(OUT);

# # 02 GOterm-Gene 
# open(IN,"C:/Users/15382/Desktop/process/gene_entrezID.txt") || die "$!";
# my %hash0=();
# while(<IN>){
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#         my @temp = split("\t",$_);
#         $hash0{$temp[0]}=$temp[1];
#     }
# }
# close(IN);
# open(IN1,"C:/Users/15382/Desktop/process/gene-gujifangji.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/process/Gene-TraditionalFomula.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#         my @temp1 = split("\t",$_);
#         if(exists($hash0{$temp1[0]})){
#             print OUT "Gene::".$hash0{$temp1[0]}."\t"."TraditionalFomula::".$temp1[1]."\n";
#         }
#         else  {
#             next;
#         }
#     }
# }
# close(IN1);
# close(OUT);

# # 03 Gene-ChinesePatentDrugs 
# open(IN,"C:/Users/15382/Desktop/process/gene_entrezID.txt") || die "$!";
# my %hash0=();
# while(<IN>){
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#         my @temp = split("\t",$_);
#         $hash0{$temp[0]}=$temp[1];
#     }
# }
# close(IN);
# open(IN1,"C:/Users/15382/Desktop/process/gene-drugs.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/process/Gene-ChinesePatentDrugs.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#         my @temp1 = split("\t",$_);
#         if(exists($hash0{$temp1[0]})){
#             print OUT "Gene::".$hash0{$temp1[0]}."\t"."ChinesePatentDrugs::".$temp1[1]."\n";
#         }
#         else  {
#             next;
#         }
#     }
# }
# close(IN1);
# close(OUT);

# # 04 Gene-compound
# open(IN,"C:/Users/15382/Desktop/process/gene_entrezID.txt") || die "$!";
# my %hash0=();
# while(<IN>){
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#         my @temp = split("\t",$_);
#         $hash0{$temp[0]}=$temp[1];
#     }
# }
# close(IN);
# open(IN1,"C:/Users/15382/Desktop/process/gene-compound.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/process/Gene-compound0.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#         my @temp1 = split("\t",$_);
#         if(exists($hash0{$temp1[0]})){
#             print OUT "Gene::".$hash0{$temp1[0]}."\t".$temp1[1]."\n";
#         }
#         else  {
#             next;
#         }
#     }
# }
# close(IN1);
# close(OUT);

# 05 compound-Gene
# open(IN,"C:/Users/15382/Desktop/process/gene_entrezID.txt") || die "$!";
# my %hash0=();
# while(<IN>){
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#         my @temp = split("\t",$_);
#         $hash0{$temp[0]}=$temp[1];
#     }
# }
# close(IN);
# open(IN1,"C:/Users/15382/Desktop/process/compound-gene.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/process/compound-Gene0.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#         my @temp1 = split("\t",$_);
#         if(exists($hash0{$temp1[1]})){
#             print OUT $temp1[0]."\t"."Gene::".$hash0{$temp1[1]}."\n";
#         }
#         else  {
#             next;
#         }
#     }
# }
# close(IN1);
# close(OUT);

# #06 HuangLian-Gene
# open(IN,"C:/Users/15382/Desktop/process/symptomID.txt") || die "$!";
# my %hash0=();
# while(<IN>){ 
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else  {
#         my @temp = split("\t",$_);
#         $hash0{$temp[0]}=$temp[1];
#     }
# }
# close(IN);
# open(IN1,"C:/Users/15382/Desktop/process/zhenghouzhengzhuang.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/process/Syndrome-Symptom.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#         my @temp1 = split("\t",$_);
#         if(exists($hash0{$temp1[1]})){
#             print OUT "Syndrome::".$temp1[0]."\t"."Symptom::".$hash0{$temp1[1]}."\n";
#         }
#         else  {
#             next;
#         }
#     }
# }
# close(IN1);
# close(OUT);

#06 HuangLian-Gene
open(IN,"C:/Users/15382/Desktop/process/symptomID.txt") || die "$!";
my %hash0=();
while(<IN>){ 
    chomp($_);
    if(!$_){
        next;
    }
    else  {
        my @temp = split("\t",$_);
        $hash0{$temp[0]}=$temp[1];
    }
}
close(IN);
open(IN2,"C:/Users/15382/Desktop/process/gene_entrezID.txt") || die "$!";
my %hash1=();
while(<IN2>){ 
    chomp($_);
    if(!$_){
        next;
    }
    else  {
        my @temp = split("\t",$_);
        $hash1{$temp[0]}=$temp[1];
    }
}
close(IN2);
open(IN1,"C:/Users/15382/Desktop/process/symptom-gene0.txt") || die "$!";
open(OUT,">C:/Users/15382/Desktop/process/Symptom-Gene.txt") || die "$!";
while (<IN1>) {
    chomp($_);
    if(!$_){
        next;
    }
    else {
        my @temp1 = split("\t",$_);
        if(exists($hash0{$temp1[0]})){
            print OUT "Symptom::".$hash0{$temp1[0]}."\t";
        }
        else  {
            next;
        }
        if (exists($hash1{$temp1[1]})) {
            print OUT "Gene::".$hash1{$temp1[1]}."\n";
        }
        else  {
            next;
        }
    }
}
close(IN1);
close(OUT);

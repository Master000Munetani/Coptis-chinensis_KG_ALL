# ## 01 Gene - Compound
# open(IN,"C:/Users/15382/Desktop/process/CompoundID.txt") || die "$!";
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
# open(IN1,"C:/Users/15382/Desktop/process/Gene-compound0.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/process/Compound-Gene0.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#         my @temp1 = split("\t",$_);
#         if(exists($hash0{$temp1[1]})){
#             print OUT "Compound::".$hash0{$temp1[1]}."\t".$temp1[0]."\n";
#         }
#         else  {
#             next;
#         }
#     }
# }
# close(IN1);
# close(OUT);

## 02 HuangLian-BiologicalProcess\HuangLian-TraditionalFomula
open(IN1,"C:/Users/15382/Desktop/process/locus.txt") || die "$!";
open(OUT,">C:/Users/15382/Desktop/process/TCMsymptom-TCMlocus.txt") || die "$!";
while (<IN1>) {
    chomp($_);
    if(!$_){
        next;
    }
    else {
            my @temp1=split("\t",$_);
            print OUT "TCMsymptom::".$temp1[0]."\t"."TCMlocus::".$temp1[1]."\n";
        }
        
    
}
close(IN1);
close(OUT);